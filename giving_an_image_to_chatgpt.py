import base64
import requests
import json
import pprint
import csv

# OpenAI API Key
api_key = ""

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
image_path = "test2.jpg"

# Getting the base64 string
base64_image = encode_image(image_path)

headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {api_key}"
}
prompt = input("Please enter the prompt")
print(f"the prompt is \n {prompt}")
payload = {
  "model": "gpt-4o",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": f"{prompt}"
        #   "text": """The picture shows a table with numerical and non numerical values.
        #              organize the information present in the picture in a csv form with headers correctly specified
        #              without any space in between the header names. order of the values should be maintained with respect to
        #              header names.
        #              Also do not include any  other thing in output other than the data present in the picture"""
        #   """The picture shows a table with numerical and non numerical values.
        #   organize the information present in the picture in a tabular form with headers correctly specified without any space 
        #   in between the header names"""
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{base64_image}",
            "detail": "high"
          }
        }
      ]
    }
  ],
  "max_tokens": 2000
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
#print(response.json()['choices'][0]['message'])
#print(response.content)

with open('image_content.json','w') as file:
    #file.write(response.json()['choices'][0]['message'])
    json.dump(response.json()['choices'][0]['message'],file,ensure_ascii=False, indent=4)

import reading_from_a_json_file
import displaying_on_plotly
