import sqlite3
import hashlib
from getpass import getpass

# Create database and table
def db():
    conn = sqlite3.connect("user.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user (
            username TEXT PRIMARY KEY,
            password TEXT,
            is_logged_in INTEGER
        )
    ''')
    conn.commit()
    conn.close()

# Hash password function
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Register new user
def register_user():
    conn = sqlite3.connect("user.db")
    cursor = conn.cursor()

    username = input("Enter a username: ")
    print("Enter password (note: nothing will be visible while typing):")
    password = getpass()

    cursor.execute("SELECT * FROM user WHERE username=?", (username,))
    if cursor.fetchone():
        print("Username already exists. Try a different one.")
        conn.close()
        return

    hashed_password = hash_password(password)
    cursor.execute("INSERT INTO user VALUES (?, ?, 0)", (username, hashed_password))
    conn.commit()
    conn.close()
    print("Registration successful!")

# Login user
def login_user():
    conn = sqlite3.connect("user.db")
    cursor = conn.cursor()

    username = input("Enter username: ")
    print("Enter password (note: nothing will be visible while typing):")
    password = getpass()
    hashed = hash_password(password)

    cursor.execute("SELECT * FROM user WHERE username=?", (username,))
    user = cursor.fetchone()

    if user:
        if user[1] == hashed:
            if user[2] == 1:
                print("User already logged in.")
            else:
                cursor.execute("UPDATE user SET is_logged_in=1 WHERE username=?", (username,))
                conn.commit()
                print("Login successful!")
        else:
            print("Incorrect password.")
    else:
        print("User not found.")

    conn.close()

# Logout user
def logout_user():
    conn = sqlite3.connect("user.db")
    cursor = conn.cursor()

    username = input("Enter username: ")
    print("Enter password (note: nothing will be visible while typing):")
    password = getpass()
    hashed = hash_password(password)

    cursor.execute("SELECT * FROM user WHERE username=?", (username,))
    user = cursor.fetchone()

    if user:
        if user[1] == hashed:
            if user[2] == 1:
                cursor.execute("UPDATE user SET is_logged_in=0 WHERE username=?", (username,))
                conn.commit()
                print("Logout successful!")
            else:
                print("User is already logged out.")
        else:
            print("Incorrect password.")
    else:
        print("User not found.")

    conn.close()


# Change password
def change_password():
    conn = sqlite3.connect("user.db")
    cursor = conn.cursor()

    username = input("Enter your username: ")
    old_pass = getpass("Enter your current password: ")

    cursor.execute("SELECT * FROM user WHERE username=?", (username,))
    user = cursor.fetchone()

    if user:
        if user[2] == 1:  # logged in check
            if user[1] == hash_password(old_pass):
                new_pass = getpass("Enter new password: ")
                hashed = hash_password(new_pass)
                cursor.execute("UPDATE user SET password=? WHERE username=?", (hashed, username))
                conn.commit()
                print("Password changed successfully.")
            else:
                print("Incorrect current password.")
        else:
            print("Please login first to change your password.")
    else:
        print("User not found.")

    conn.close()

# Menu to call functions
def main():
    db()
    while True:
        print("\n==== User Management Menu ====")
        print("1. Register")
        print("2. Login")
        print("3. Logout")
        print("4. Change Password")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            register_user()
        elif choice == "2":
            login_user()
        elif choice == "3":
            logout_user()
        elif choice == "4":
            change_password()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# Run the main menu
main()
