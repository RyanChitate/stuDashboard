import sqlite3
import bcrypt

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Create the users table (run once)
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT
)
''')

# Add user 'kegan' with password 'kegan123', hash the password
password = bcrypt.hashpw("kegan123".encode('utf-8'), bcrypt.gensalt())  # Hash the password 'kegan123'
cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("kegan", password))

# Commit and close
conn.commit()
conn.close()
