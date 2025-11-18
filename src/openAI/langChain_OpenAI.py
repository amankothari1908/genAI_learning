# pip3 install -U langchain langchain-community langchain-openai
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_KEY")

# Instatiate your language model
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7 , api_key=OPENAI_API_KEY)

# You will be more often than not be work with complex strings but for now lets start with a simple one!
my_text = "Explain a Large Language Model in one line?"

# Getting response for the question from the language model
response = llm.invoke("Hello, what can you do?")

print(response)