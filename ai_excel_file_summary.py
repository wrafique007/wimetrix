from langchain_experimental.agents import create_csv_agent, create_pandas_dataframe_agent
from langchain_openai import OpenAI, ChatOpenAI
from langchain.agents.agent_types import AgentType
import os
import pandas as pd
from langchain_core.tools import tool

os.environ["OPENAI_API_KEY"] = ""

df = pd.read_csv("Portal_Entry_data_report.csv")

llm = OpenAI(model="gpt-4", temperature=0)


PREFIX = """
You are working with a pandas dataframe in Python. The name of the dataframe is `df`.
You should use the tools below to answer the question posed of you:

python_repl_ast: A Python shell. Use this to execute python commands. Input should be a
validpython command. When using this tool, sometimes output is abbreviated - make sure it
does not look abbreviated before using it in your answer."""

FORMAT_INSTRUCTIONS = """Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [python_repl_ast]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question


This is the result of `print(df.head())`:
{df}

Begin!
Question: {input}
{agent_scratchpad}
"""

SUFFIX = """Begin!

Question: {input}
Thought:{agent_scratchpad}"""



agent = create_csv_agent(
    llm,
    "Portal_Entry_data_report.csv",
    agent_type="openai-tools",
    verbose=True,
    allow_dangerous_code=True
)
# agent_kwargs={
#         'prefix':PREFIX,
#         'format_instructions':FORMAT_INSTRUCTIONS,
#         'suffix':SUFFIX
#     }

# agent_executor = create_pandas_dataframe_agent(
#     llm,
#     df,
#     agent_type="openai-tools",
#     verbose=True,
#     allow_dangerous_code=True
# )

print(agent.invoke("how many number of rows are there in the dataframe").content)
