# pip3 install -U langchain langchain-community langchain-openai
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_KEY")

# Instatiate your language model
chat = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7 , api_key=OPENAI_API_KEY)

# You will be more often than not be work with complex strings but for now lets start with a simple one!
my_text = "Explain a Large Language Model in one line?"

# Getting response for the question from the language model
chat(
    [
        SystemMessage(content="You are a dumb AI bot that is unhelpful and makes jokes at whatever the user says"),
        HumanMessage(content="how do I navigate maps?")
    ]
)
