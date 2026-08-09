
import streamlit as st
from Backend import chatbot
from langchain_core.messages import HumanMessage



CONFIG = {"configurable": {"thread_id": "thread-1"}}
## St.session-state  -> Dict -> 
if "messsage_history" not in st.session_state:
    st.session_state["messsage_history"]=[]


## Laoding the conversation history ! 

for message in st.session_state["messsage_history"]:
    with st.chat_message(message["role"]):
        st.text(message["content"])



user_input = st.chat_input("Type Here")



if user_input:
    ## Add message to message history ! 
    st.session_state["messsage_history"].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.text(user_input)
    
    ## Call the chatbot 
    response = chatbot.invoke({"message": [HumanMessage(content= user_input)]},config=CONFIG)
    # send response to llm 
    ai_message = response["message"][-1].content
    
    
    ## Add message to message history ! 
    st.session_state["messsage_history"].append({"role": "ai", "content": ai_message})
    with st.chat_message("ai"):
        st.text(ai_message)