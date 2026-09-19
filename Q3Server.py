import socket

def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_socket.bind(("localhost", 30072))
        server_socket.listen(1)
        print("Server is listening on port 12345...")

        conn, addr = server_socket.accept()
        print(f"Connected by {addr}")

        try:
            message = conn.recv(1024).decode()
            print("Received:", message)
        except Exception as e:
            print("Error receiving data:", e)
        finally:
            conn.close()

    except Exception as e:
        print("Server error:", e)
    finally:
        server_socket.close()

if __name__ == "__main__":
    run_server()
