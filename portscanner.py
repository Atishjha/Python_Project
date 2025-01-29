import socket
def is_port_open(hostname , port):
    """
    Check if a specific port is open on a host.
    Args:
        hostname: The hostname or IP address of the target machine.
        port: The port number to be scanned.
    Return:
        True if the port is open, False otherwise.
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5) #Set atimeout for faster scans
        s.connect((hostname , port))
        return True
    except socket.error:
        return False

def main():
        """
        Prompts user for hostname/IP and port range, then scans the ports.
        """ 
        hostname = input("Enter hostname or IP address: ")
        port_start = int(input("Enter starting port number: "))
        port_end = int(input("Enter ending port number: "))
        print("Scanning ports", port_start,"to", port_end,"on",hostname)
        for port in range(port_start , port_end+1):
            if is_port_open(hostname , port):
                print(f"Port {port} is OPEN")
            else:
                print(f"Port {port} is CLOSED")
if __name__ == "__main__":
            main() 