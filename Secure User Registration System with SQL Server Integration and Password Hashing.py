import hashlib
import os
import pyodbc

# Database connection setup
def connect_to_db():
    # Define connection parameters
    server = 'DESKTOP-2UAHBMR\\SQLSERVER2022'  # Use your actual server name with the correct instance name
    database = 'TestDB'  # Your database name
    driver = '{ODBC Driver 17 for SQL Server}'  # Ensure you have the correct ODBC driver installed

    # Establish the connection using Windows Authentication (Trusted Connection)
    connection = pyodbc.connect(
        f'DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
    )
    return connection

# Function to generate a password hash with salt
def hash_password(password):
    salt = os.urandom(16)  # Generate a random 16-byte salt
    password_bytes = password.encode('utf-8')
    hashed_password = hashlib.pbkdf2_hmac('sha256', password_bytes, salt, 100000)
    return hashed_password, salt

# Function to insert user data into the database
def save_user_to_db(username, password_hash, salt):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        
        # Insert the user's data into the database
        cursor.execute(
            "INSERT INTO Users (Username, PasswordHash, Salt) VALUES (?, ?, ?)",
            username, password_hash, salt
        )
        conn.commit()
        print("User saved successfully!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()

# Main function to handle user sign-up
def sign_up():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    
    # Hash the password
    password_hash, salt = hash_password(password)
    
    # Save user data to the database
    save_user_to_db(username, password_hash, salt)

if __name__ == "__main__":
    sign_up()
