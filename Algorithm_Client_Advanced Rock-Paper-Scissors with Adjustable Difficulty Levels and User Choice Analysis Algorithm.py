#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket

def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', 12345))
        while True:
            message = input("Enter your choice (rock, paper, scissors) or 'exit' to quit: ")
            if message == 'exit':
                break
            s.sendall(message.encode())
            data = s.recv(1024)
            print(f"Received from server: {data.decode()}")

if __name__ == '__main__':
    # This replaces the comment in File 1
    start_client()

