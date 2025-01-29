#  Ping Sweep: Develop  a script that pings a list of IP address to identify active device on the network. Utilize the ping module for this task\
import ping3
def ping_sweep(subnet):
    ''' 
    Sweeps a subnet for active hosts using ping3 library.
    Args: 
         subnet: The subnet address in CIDR notation (e.g. , "192.168.1.0/24").
    '''
    print(f"Pinig sweeping subnet: {subnet}")
    # Create an IP network object from the subnet address
    network = ipaddress.ip_network(subnet)
    # List to store alive hosts
    alive_host = []
    # Loop through each host in the network
    for ip in network.hosts():
        # Convert IP address to string
        ip_str = str(ip)

        # Send a ping request with a count of 1 and timeout of 1 second
        response = ping3.ping(ip_str, count = 1, timeout = 1)

        # Check if ping was successful
        if response:
            alive_host.append(ip_str)
            print(f" {ip_str} - Alive")
        else:
            print(f"  {ip_str} - No response")
    # Print summary of alive hosts
    print(f"\nFound {len(alive_host)} alive hosts: ")
    for host in alive_host:
        print(f"  -{host}")

if __name__ == "__main__":
    # Get subnet address from user input
    subnet = input("Enter subnet address in CIDR notation (e.g.,192.168.1.0/24): ")
    ping_sweep(subnet)