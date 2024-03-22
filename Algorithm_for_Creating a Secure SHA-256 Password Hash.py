import hashlib

# Function to hash a password
def hash_password(password):
    # Create a new sha256 hash object
    hash_object = hashlib.sha256()
    
    # Update the hash object with the bytes of the password
    hash_object.update(password.encode())
    
    # Return the hexadecimal representation of the digest
    return hash_object.hexdigest()

# Example usage:
# Hash a password
password = 'my$ecureP@ssw0rd'
hashed_password = hash_password(password)

print(f"The hashed password is: {hashed_password}")
