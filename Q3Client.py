import socket
def run_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect(("localhost", 30072))
        client_socket.sendall("Hello from client!".encode())
        print("Message sent to server.")
    except Exception as e:
        print("Client error:", e)
    finally:
        client_socket.close()
if __name__ == "__main__":
    run_client()
