import base64
import requests
import json
import pprint

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

payload = {
  "model": "gpt-4o",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "The picture shows a table with numerical and non numerical data. organize the information present in the picture in a json format"
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{base64_image}"
          }
        }
      ]
    }
  ],
  "max_tokens": 300
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
#print(response.json()['choices'][0]['message']['content'])
#print(response.content)

with open('image_content.json','w') as file:
    #file.write(response.json()['choices'][0]['message']['content'])
    #file.write(response.json())
    json.dump(response.json(),file,ensure_ascii=False, indent=4)

json_data = None
with open('image_content.json', 'r') as f:
    data = f.read()
    json_data = json.loads(data)

# print json to screen with human-friendly formatting
pprint.pprint(json_data, compact=True)