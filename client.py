import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                print("Disconnected from server")
                break
            print(data.decode())
        except Exception as e:
            print(f"Error receiving message: {e}")
            break
    client_socket.close()

def send_messages(client_socket):
    while True:
        message = input()
        if message.lower() == 'exit':
            client_socket.close()
            break
        try:
            client_socket.send(message.encode())
        except Exception as e:
            print(f"Error sending data: {e}")
            client_socket.close()
            break

def run_client(ip='127.0.0.2', port_num=12346):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ip, port_num))
    print("Connected to the server")

    threading.Thread(target=receive_messages, args=(client_socket,)).start()
    send_messages(client_socket)

if __name__ == "__main__":
    run_client()