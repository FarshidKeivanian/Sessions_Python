import socket

def start_client():
    ports_to_try = [12345, 54321, 65432]  # Should match the server's ports
    connection_established = False

    for port in ports_to_try:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(('localhost', port))
            print(f"Connected to server on port {port}")
            connection_established = True
            break  # Exit the loop once a connection is established
        except ConnectionRefusedError:
            print(f"Could not connect to server on port {port}. Trying next port...")
            continue  # Try the next port
    if not connection_established:
        print("Failed to connect to server. Please check the server status and port availability.")
        return

    try:
        while True:
            message = input("Enter your choice or 'exit' to quit: ")
            if message.lower() == 'exit':
                break
            s.sendall(message.encode())
            data = s.recv(1024)
            print(f"Received from server: {data.decode()}")
    finally:
        s.close()

if __name__ == '__main__':
    start_client()
