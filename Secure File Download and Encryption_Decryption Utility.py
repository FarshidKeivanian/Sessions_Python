import requests
from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()
cipher = Fernet(key)

def download_file(url, local_path):
    # Download the file from the given URL
    response = requests.get(url)
    if response.status_code == 200:
        with open(local_path, 'wb') as file:
            file.write(response.content)
        print(f"File downloaded successfully: {local_path}")
    else:
        raise Exception(f"Failed to download file. Status code: {response.status_code}")

def encrypt_file(file_path, encrypted_path):
    # Read file content
    with open(file_path, 'rb') as file:
        file_data = file.read()
    # Encrypt data
    encrypted_data = cipher.encrypt(file_data)
    # Write encrypted data to a new file
    with open(encrypted_path, 'wb') as file:
        file.write(encrypted_data)
    print(f"Encrypted file saved to: {encrypted_path}")

def decrypt_file(encrypted_path, decrypted_path):
    # Read encrypted content
    with open(encrypted_path, 'rb') as file:
        encrypted_data = file.read()
    # Decrypt data
    decrypted_data = cipher.decrypt(encrypted_data)
    # Write decrypted data to a new file
    with open(decrypted_path, 'wb') as file:
        file.write(decrypted_data)
    print(f"Decrypted file saved to: {decrypted_path}")

# URL of the file to be downloaded
url = "https://raw.githubusercontent.com/FarshidKeivanian/Sessions_Python/main/example_for_encryption.txt"
download_path = "example.txt"
encrypted_path = "example_encrypted.txt"
decrypted_path = "example_decrypted.txt"

# Download the file from the URL
download_file(url, download_path)

# Encrypt the file and save it locally
encrypt_file(download_path, encrypted_path)

# Decrypt the file and save it locally
decrypt_file(encrypted_path, decrypted_path)
