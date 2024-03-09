import socket

def start_client():
    ports_to_try = [12345, 54321, 65432]  # Should match the server's ports
    connected = False

    for port in ports_to_try:
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect(('localhost', port))
            print(f"Connected to server on port {port}.")
            connected = True
            break  # Exit loop on successful connection
        except ConnectionRefusedError:
            print(f"Could not connect to server on port {port}. Trying next port...")

    if not connected:
        print("Failed to connect to the server. Please ensure the server is running and ports are correct.")
        return

    print("Welcome to Rock-Paper-Scissors! Type 'exit' to quit.")
    try:
        while True:
            user_input = input("Choose rock, paper, or scissors: ").lower()
            if user_input not in ["rock", "paper", "scissors", "exit"]:
                print("Invalid choice. Please choose rock, paper, scissors, or type 'exit' to quit.")
                continue
            elif user_input == "exit":
                break

            client_socket.sendall(user_input.encode())
            response = client_socket.recv(1024).decode()
            print(response)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client_socket.close()
        print("Disconnected from server.")

if __name__ == '__main__':
    start_client()
