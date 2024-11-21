#to see users and password
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Retrieve all users from the users table
cursor.execute("SELECT username, password FROM users")

# Fetch all rows
users = cursor.fetchall()

# Print the user details
for user in users:
    print(f"Username: {user[0]}, Password Hash: {user[1]}")

# Close the connection
conn.close()
