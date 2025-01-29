import socket
import os

HOST = "localhost"
PORT = 65432

def send_file(filename, sock):
    """
    Sends a file to the connected server.

    Args:
      filename: The filename to be sent from the client.
      sock: The socket object for communication with the server.
    """
    with open(filename, "rb") as f:
        data = f.read(1024)
        while data:
            sock.sendall(data)
            data = f.read(1024)

def main():
    '''
    Prompts user for filename, connects to server, and sends the files.
    '''
    filename = input("Enter filename to transfer: ")
    if not os.path.exists(filename):
        print(f"Error: File {filename} does not exist.")
        return 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(filename.encode()) # Send filename to server
        print(f"Sending file: {filename}")
        send_file(filename, s)
if __name__ == "__main__":
    main()
