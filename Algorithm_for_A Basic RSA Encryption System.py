#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
from sympy import isprime, mod_inverse

def generate_prime_candidate(length):
    # Generate random prime number of given bit length
    p = random.getrandbits(length)
    p |= (1 << length - 1) | 1
    return p

def generate_prime_number(length=1024):
    p = 4
    # Ensure p is prime
    while not isprime(p):
        p = generate_prime_candidate(length)
    return p

def encrypt(plaintext, public_key):
    n, e = public_key
    plaintext_integers = [ord(char) for char in plaintext]
    ciphertext = [pow(char, e, n) for char in plaintext_integers]
    return ciphertext

def decrypt(ciphertext, private_key):
    n, d = private_key
    plaintext_integers = [pow(char, d, n) for char in ciphertext]
    plaintext = ''.join(chr(char) for char in plaintext_integers)
    return plaintext

# Generate prime numbers p and q
p = generate_prime_number(128)
q = generate_prime_number(128)

n = p * q
phi_n = (p-1) * (q-1)

# Choose e
e = 65537 # Common choice for e

# Compute d
d = mod_inverse(e, phi_n)

# Public and private keys
public_key = (n, e)
private_key = (n, d)

# Encrypt and decrypt a message
message = "Hello RSA!"
ciphertext = encrypt(message, public_key)
decrypted_message = decrypt(ciphertext, private_key)

print("Original message:", message)
print("Encrypted message:", ciphertext)
print("Decrypted message:", decrypted_message)


# In[ ]:




