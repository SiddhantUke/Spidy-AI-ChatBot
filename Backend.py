from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage, HumanMessage
from langchain_groq import ChatGroq
from langgraph.checkpoint.memory import InMemorySaver
from dotenv import load_dotenv
from langgraph.graph.message import add_messages


load_dotenv()


## Refer Day 9 or 9 file of chatbot for better understanding ! 

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.5
)

class ChatState(TypedDict):
    
    message : Annotated[list[BaseMessage], add_messages]
    
    
    ## Creating a chat_node function ! 

def chat_node(state: ChatState):

    message = state['message']

    response = llm.invoke(message)

    return {"message" : response}


checkpointer = InMemorySaver()


graph = StateGraph(ChatState)


graph.add_node("chat_node", chat_node)

graph.add_edge(START , "chat_node")
graph.add_edge("chat_node" , END)


chatbot = graph.compile(checkpointer=checkpointer)


