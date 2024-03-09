import socket
import threading

# This function handles incoming client connections
def client_thread(conn, addr):
    while True:
        try:
            # Receive data from the client
            data = conn.recv(1024).decode()
            if not data:
                print(f"Connection with {addr} ended.")
                break
            print(f"Received {data} from {addr}")
            # Send a response back to the client
            conn.sendall("Received your choice".encode())
        except:
            break
    conn.close()

# Modified start_server function to try multiple ports
def start_server():
    ports_to_try = [12345, 54321, 65432]  # List of ports to try
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    for port in ports_to_try:
        try:
            server.bind(('localhost', port))
            print(f"Server started on port {port}")
            break  # Successfully bound to the port
        except OSError as e:
            if e.winerror == 10048:  # Port already in use
                print(f"Port {port} is in use, trying next port.")
                continue  # Try the next port
            else:
                raise  # Reraise any other OSError that isn't related to port binding
    else:
        print("Failed to bind to any port. Please check the port availability.")
        return

    server.listen()

    while True:
        conn, addr = server.accept()
        print(f"Connected by {addr}")
        thread = threading.Thread(target=client_thread, args=(conn, addr))
        thread.start()

# This function is used to start the server in a thread
def run_server():
    start_server()

# Start the server in a separate thread
server_thread = threading.Thread(target=run_server)
server_thread.start()
