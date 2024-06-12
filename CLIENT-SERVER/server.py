import socket
import threading

connected_clients = []
client_lock = threading.Lock()

def broadcast(message, client_socket):
    with client_lock:
        for client in connected_clients:
            if client != client_socket:
                try:
                    client.send(message)
                except Exception as e:
                    print(f"Error sending message: {e}")
                    client.close()
                    connected_clients.remove(client)

def manage_client(client_socket, client_addr):
    print(f"New connection from {client_addr}")
    with client_lock:
        connected_clients.append(client_socket)
    client_socket.send(b"Welcome to the chat server!")

    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            broadcast(message, client_socket)
        except Exception as e:
            print(f"Error handling message from {client_addr}: {e}")
            break

    print(f"Connection closed from {client_addr}")
    with client_lock:
       connected_clients.remove(client_socket)
    client_socket.close()

def run_server(ip='127.0.0.2', port_num=12346):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((ip, port_num))
    server_socket.listen(5)
    print(f"Server started on {ip}:{port_num}")

    while True:
        client_socket, client_addr = server_socket.accept()
        threading.Thread(target=manage_client, args=(client_socket, client_addr)).start()

if __name__ == "__main__":
    run_server()