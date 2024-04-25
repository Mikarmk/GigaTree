import streamlit as st

# Функция для отображения страницы входа
def login_page():
    st.title("Login")
    username = st.text_input("Enter your username")
    password = st.text_input("Enter your password", type="password")
    if st.button("Log in"):
        if username == st.secrets["username"] and password == st.secrets["password"]:
            st.session_state.username = username
            st.session_state.logged_in = True
            st.success("Login successful! You can now use the chat bot.")
        else:
            st.error("Invalid username or password. Please try again.")

# Функция для отображения страницы чата
def chat_page():
    st.title("LabTree Chat")
    st.write("Welcome, " + st.session_state.username)

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("What is up?"):
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        response = f"Echo: {prompt}"
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

# Проверка, зарегистрирован ли или авторизован пользователь
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    login_page()
    if "logged_in" not in st.session_state or not st.session_state.logged_in:
        registration_page()
else:
    chat_page()
