#!/usr/bin/env python
# coding: utf-8

# In[1]:


import socket
import threading

# This is the client handling function from File 1
def client_thread(conn, addr):
    while True:
        try:
            # Receive choice from client
            data = conn.recv(1024).decode()
            if not data:
                print(f"Connection with {addr} ended.")
                break
            print(f"Received {data} from {addr}")
            # Send response to client (logic to determine outcome should be added here)
            conn.sendall("Received your choice".encode())
        except:
            break
    conn.close()

# This is the server start function from File 1
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 12345))
    server.listen()
    print("Server started. Listening for connections...")

    while True:
        conn, addr = server.accept()
        print(f"Connected by {addr}")
        thread = threading.Thread(target=client_thread, args=(conn, addr))
        thread.start()

# Integration of running the server in a thread, inspired by File 2
if __name__ == '__main__':
    server_thread = threading.Thread(target=start_server)
    server_thread.start()

    # The main program continues here
    # You can add any other code you want to run in the main thread
    # For example, a GUI for the server, logging, or other non-blocking tasks


# In[ ]:




