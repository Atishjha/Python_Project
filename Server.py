import socket
import os

HOST = "localhost"
PORT = 65432

def receive_file(filename, sock):
    """
  Receives a file from the connected client.

  Args:
      filename: The filename to be saved on the server.
      sock: The socket object for communication with the client.
  """
    with open(filename, "wb") as f:
        while True:
            data = sock.recv(1024)
            if not data:
                break
            f.write(data)

def main():
    """
    Starts the server, listens for connections, and receives files."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            filename = conn.recv(1024).decode()
            print(f"Receiving file: {filename}")
            receive_file(filename,conn)
            print("File transfer complete.")

if __name__ == "__main__":
    main()
