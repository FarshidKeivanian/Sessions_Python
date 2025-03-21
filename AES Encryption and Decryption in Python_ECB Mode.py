from Crypto.Cipher import AES
import base64

def pad(text):
    return text + (16 - len(text) % 16) * ' '

key = "thisisasecretkey"  # Must be 16, 24, or 32 bytes
message = "Hello from Farshid!"

cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
encrypted_text = base64.b64encode(cipher.encrypt(pad(message).encode('utf-8')))
print(f"Encrypted: {encrypted_text.decode()}")

decrypted_text = cipher.decrypt(base64.b64decode(encrypted_text)).decode().strip()
print(f"Decrypted: {decrypted_text}")
