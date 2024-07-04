import getpass
import os

#os.environ["OPENAI_API_KEY"] = getpass.getpass()



# Uncomment the below to use LangSmith. Not required.
# os.environ["LANGCHAIN_API_KEY"] = getpass.getpass()
# os.environ["LANGCHAIN_TRACING_V2"] = "true"


from langchain_community.utilities import SQLDatabase
from sqlalchemy import create_engine

from langchain.chains import create_sql_query_chain
from langchain_openai import ChatOpenAI

cs = "mssql+pymssql://waleed1:Q!123@localhost/ai_agent_testing"
db_engine = create_engine(cs)
db = SQLDatabase(db_engine)

llm = ChatOpenAI(model="gpt-4", temperature=0)
chain = create_sql_query_chain(llm, db)
response = chain.invoke({"question": "How many employees are there. only generate sql query"})
print(f"response is {response}")



names = db.get_usable_table_names()
#employees = db.run(f"select * from [dbo].[{names[0]}];")
employees = db.run(response)
print(names)
print(type(employees))
print(f"there are {employees[2]} employees in the company")


