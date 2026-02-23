from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM

# chat roles: system, ai and human
template = ChatPromptTemplate.from_messages([
    ("system", "you are an agent that identifies songs by lyrics"),
    ("human", "answer this question: which song starts with 'I found a love for me\nDarling just dive right in'?"),
    ("ai", "I think that's **\"Perfect\"** by Ed Sheeran"),
    ("human", "answer this question: {question}")
])

# initialize the model
model = OllamaLLM(model="gemma2:2b")

# create a chain to pass the prompt template into the LLM.
# a chain connects calls to different components
llm_chain = template | model 
# print(llm_chain.to_json())

# invoke this chain on the question variable
response = llm_chain.invoke(
    {"question": "which song starts with 'Well, you only need the light when it's burnin' low\nOnly miss the sun when it starts to snow'?"}
)
print(response)
