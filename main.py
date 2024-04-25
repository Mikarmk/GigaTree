import streamlit as st
import gigachat
from langchain.chat_models.gigachat import GigaChat

st.title("GigaLabTree")

gigachat_creds = gigachat.Credentials(token=st.secrets["GIGACHAT_API_KEY"])
chat_client = GigaChat(credentials=gigachat_creds)

if "gigachat_model" not in st.session_state:
    st.session_state["gigachat_model"] = "GigaChat Lite"  

# История сообщений 
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    st.write(f"{message['role'].title()}: {message['content']}")

user_input = st.text_input("Start the conversation...")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    gigachat_response = chat_client.get_response(st.session_state.messages)
    st.session_state.messages.append({"role": "assistant", "content": gigachat_response})

    st.write("Assistant: " + gigachat_response)
