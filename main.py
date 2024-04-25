import streamlit as st
from gigachat import GigaChat

# Настройка стилей
st.markdown(
    """
    <style>
    body {
        color: #333;
        background-color: #f0f0f0;
    }
    .sticky-footer {
        position: relative;
        bottom: 0;
        width: 100%;
        height: 60px; 
        background-color: #343a40;
        color: #ffffff;
        text-align: center;
        line-height: 60px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("GigaLabTree")
st.write("Welcome to GigaLabTree chat interface!")

gigachat_creds = Credentials(token=st.secrets["GIGACHAT_API_KEY"])
chat_client = GigaChat(credentials=gigachat_creds)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    st.write(f"{message['role'].title()}: {message['content']}")

user_input = st.text_input("Start the conversation...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    gigachat_response = chat_client.get_response(st.session_state.messages)
    st.session_state.messages.append({"role": "assistant", "content": gigachat_response})

    st.write("Assistant: " + f"Ответ нейронки: {gigachat_response} - Ваш запрос: {user_input}")

# Футер
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown('<div class="sticky-footer">GigaLabTree Chat Interface</div>', unsafe_allow_html=True)
