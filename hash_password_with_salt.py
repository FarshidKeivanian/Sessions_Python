import hashlib
import os

# Function to hash a password with salt using SHA-256
def hash_password_with_salt(password):
    # Generate a 16-byte random salt
    salt = os.urandom(16)
    
    # Combine the salt and password, then hash
    hash_object = hashlib.sha256(salt + password.encode())
    hashed_password = hash_object.hexdigest()
    
    return salt.hex(), hashed_password

# Example usage:
password = 'my$ecureP@ssw0rd'
salt, hashed_password = hash_password_with_salt(password)

print(f"Salt (hex): {salt}")
print(f"Hashed password: {hashed_password}")
