import hashlib

def hash_password(password):
    # Convert the password to bytes
    password_bytes = password.encode('utf-8')
    # Create a hash object
    hashed_password = hashlib.sha256(password_bytes).hexdigest()
    return hashed_password

# Example usage
password = input("Enter your password: ")
print("Hashed Password:", hash_password(password))
