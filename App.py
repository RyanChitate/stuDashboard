import streamlit as st
import sqlite3
import bcrypt

# Database setup
def create_database():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Add a user to the database (use this to pre-create the admin user)
def add_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    try:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
        conn.commit()
    except sqlite3.IntegrityError:
        st.error("User already exists.")
    conn.close()

# Authenticate user
def authenticate_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT password FROM users WHERE username = ?', (username,))
    record = cursor.fetchone()
    conn.close()
    if record and bcrypt.checkpw(password.encode('utf-8'), record[0].encode('utf-8')):
        return True
    return False

# Initialize database
create_database()

# Add admin user (uncomment to initialize admin user; comment after first run)
# add_user("admin", "securepassword123")

# Streamlit UI
st.title("Secure Login")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if authenticate_user(username, password):
        st.success(f"Welcome, {username}!")
        st.write("You are now logged in.")
    else:
        st.error("Invalid username or password.")

st.info("To set up a new admin account, run the `add_user` function in your code with the desired credentials.")
