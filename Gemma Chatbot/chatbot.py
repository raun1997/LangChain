import streamlit as st
import os
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

def get_gemma_response(country):
    response = llm_chain.invoke({"country":country})
    return response.content

prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a flag expert.\n"
     "Return ONLY a comma-separated list of colors.\n"
     "Do NOT explain."),
    ("human", "germany"),
    ("ai", "black, red, yellow"),
    ("human", "pakistan"),
    ("ai", "green, white"),
    ("human", "{country}")
])

# initialize model
model = ChatOllama(model="gemma2:2b",
                   # low temperature, more deterministic approach
                   temperature=0)
# print(llm)

# chain the chat prompt template, and then invoke the chain
llm_chain = prompt_template | model

st.header("What The Flag!")

if "history" not in st.session_state:
    st.session_state["history"] = []

country = st.chat_input("Country: ")
if country:
    st.session_state.history.append({
        "role":"user",
        "content": country
    })
    response = get_gemma_response(country)
    st.session_state.history.append({
        "role":"assistant",
        "content":response  
    })

for chat in st.session_state.history:
    if chat["role"] == "user":
        message = st.chat_message("user")
        message.write(f"**You:** {chat['content']}")
    else:
        message = st.chat_message("assistant")
        message.write(f"**Gemma:** {chat['content']}")
        






