# pip3 install openai
# pip3 install python-dotenv

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_KEY")
)

text = "Sun rises in the"
messages = [
    {"role": "system", "content": "Act as a helpful assistant."},
    {"role": "user", "content": text},
]

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages,
    temperature=0,
    max_tokens=20,
    n=2  # Number of response completions
)

response_message = response.choices[0].message.content
print(response_message)


