# import streamlit as st
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an assistant who can answer every question."),
    ("user", "{question}")
])

# st.title("Langchain Demo with Gemma ")
# input_text = st.text_input("Your question: ")

model = OllamaLLM(model="gemma2:2b")      # your model name goes here

output_parser = StrOutputParser()

# chaining
chain = prompt | model | output_parser

response = chain.invoke({"question": "What is the latest model by Anthropic."})
print(response)
