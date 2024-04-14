import base64
import os
# A folder for storing diary entries
diary_dir = 'diary_entries'
# Ensure the folder exists
if not os.path.exists(diary_dir):
    os.makedirs(diary_dir)

def encrypt_text(plain_text):
    # Convert text to base64 encoding
    return base64.b64encode(plain_text.encode('utf-8'))

def decrypt_text(encrypted_text):
    # Convert encoded base64 text back to plain text
    return base64.b64decode(encrypted_text).decode('utf-8')

def save_diary_entry(entry_title, entry_content):
    # Encrypt the diary content
    encrypted_content = encrypt_text(entry_content)
    # Write the encrypted content to a file
    with open(os.path.join(diary_dir, f"{entry_title}.txt"), 'wb') as file:
        file.write(encrypted_content)

def read_diary_entry(entry_title):
    # Read the encrypted content from a file
    try:
        with open(os.path.join(diary_dir, f"{entry_title}.txt"), 'rb') as file:
            encrypted_content = file.read()
            # Decrypt and display the content
            return decrypt_text(encrypted_content)
    except FileNotFoundError:
        return "Diary entry not found!"

# Usage example:
# save_diary_entry('First Day', 'Today I had piano class.')
# print(read_diary_entry('First Day'))
