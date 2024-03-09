import socket
import threading
import random

def analyze_user_choices(user_choices):
    # Analyze previous user choices to find patterns
    # This is a simplified example; a more complex algorithm could be implemented here
    if len(user_choices) < 3:
        return random.choice(["rock", "paper", "scissors"])
    else:
        return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, server_choice):
    if user_choice == server_choice:
        return "Draw!"
    elif (user_choice == "rock" and server_choice == "scissors") or \
         (user_choice == "paper" and server_choice == "rock") or \
         (user_choice == "scissors" and server_choice == "paper"):
        return "You win!"
    else:
        return "Server wins!"

def client_thread(conn, addr, difficulty="easy"):
    user_choices = []

    while True:
        try:
            data = conn.recv(1024).decode()
            if not data or data.lower() == 'exit':
                print(f"Connection with {addr} ended.")
                break
            print(f"Received {data} from {addr}")

            user_choices.append(data)
            if difficulty == "hard":
                server_choice = analyze_user_choices(user_choices)
            else:
                server_choice = random.choice(["rock", "paper", "scissors"])

            outcome = determine_winner(data, server_choice)
            response = f"Server chose: {server_choice}. {outcome}"
            conn.sendall(response.encode())
        except Exception as e:
            print(f"Error: {e}")
            break
    conn.close()

def start_server():
    ports_to_try = [12345, 54321, 65432]
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    for port in ports_to_try:
        try:
            server.bind(('localhost', port))
            print(f"Server started on port {port}")
            break
        except OSError as e:
            if e.winerror == 10048:
                print(f"Port {port} is in use, trying next port.")
                continue
            else:
                raise
    else:
        print("Failed to bind to any port. Please check the port availability.")
        return

    server.listen()

    while True:
        conn, addr = server.accept()
        print(f"Connected by {addr}")
        # Here you could eventually parse a message from the client to set the difficulty
        thread = threading.Thread(target=client_thread, args=(conn, addr, "easy"))  # Defaulting to easy for simplicity
        thread.start()

if __name__ == '__main__':
    run_server = threading.Thread(target=start_server)
    run_server.start()
