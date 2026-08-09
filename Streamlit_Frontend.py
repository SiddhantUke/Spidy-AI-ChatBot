import streamlit as st

# with st.chat_message("user"): ## User messgae 
#     st.text("Hi")
    
# with st.chat_message("assistant"): ## AI Message display
#     st.text("How can i help you?")
    
# user_input = st.chat_input("Type Here") ## Input Box Below 

# if user_input:
#     with st.chat_message("user"):
#         st.text(user_input) ## Not in string wrna uper wala hi aa jaenga ! 


## Same Feedback and  Same Input chatbot 

## Creating a Python List 

# message_history = []  
## ye show in ho rha save krne k baad bhi ! yeh automatic reset ho rha hai ! dictionary ! 


## To hm yaha session state dal denge ! jo ki hoti hai ! dictionary hi ! 

if "messsage_history" not in st.session_state:
    st.session_state["messsage_history"]=[]
    
    
## yaha save  hone k baad dusri chize chale uske liye loop chala rhe ! 

for message in st.session_state["messsage_history"]:
    with st.chat_message(message["role"]):
        st.text(message["content"])
    


## Save nh ho rhe yaha message sidha aa rahe dono message and then wo next chat me ud jaa rhe ! 
## To save krne k liye hm isko ! Dictionary me save krte hai !




# {"role: "user", "content": "Hi"}
# {"role: "assisstant", "content": "Hello"}


user_input = st.chat_input("Type Here")

if user_input:
    
    ## Add message to message history ! 
    st.session_state["messsage_history"].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.text(user_input)
    
    ## Add message to message history ! 
    st.session_state["messsage_history"].append({"role": "ai", "content": user_input})
    with st.chat_message("ai"):
        st.text(user_input)

        
        