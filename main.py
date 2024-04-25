import streamlit as st
import sqlite3

# Подключение к базе данных SQLite
conn = sqlite3.connect('users.db')
c = conn.cursor()

# Создание таблицы пользователей, если она не существует
c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT
    )
''')
conn.commit()

# Функция для регистрации пользователя
def register_user(username, password):
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()

# Функция для проверки существования пользователя в базе данных
def authenticate_user(username, password):
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    if c.fetchone():
        return True
    return False

# Главная страница приложения
def main():
    st.title("Chat Bot App")

    # Проверка, авторизован ли пользователь
    if "logged_in" not in st.session_state or not st.session_state.logged_in:
        register = st.sidebar.checkbox("Register")
        if register:
            username = st.text_input("Enter username")
            password = st.text_input("Enter password", type="password")
            if st.button("Register"):
                register_user(username, password)
                st.success("Registration successful! Please log in.")
        else:
            username = st.text_input("Enter username")
            password = st.text_input("Enter password", type="password")
            if st.button("Log in"):
                if authenticate_user(username, password):
                    st.session_state.username = username
                    st.session_state.logged_in = True
                    st.success("Login successful! You can now use the chat bot.")
                else:
                    st.error("Invalid username or password. Please try again.")

    # Отображение чат-бота
    if st.session_state.logged_in:
        st.write("Welcome, " + st.session_state.username)
        message = st.text_input("What is up?")
        st.write("Echo: " + message)

# Запускаем главную страницу
if __name__ == "__main__":
    main()

# Закрытие подключения к базе данных
conn.close()
