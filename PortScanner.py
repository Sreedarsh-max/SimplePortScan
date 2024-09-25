import socket
from IPy import IP

def scan_port(ipaddress, port):
    """Scan a single port on the specified IP address."""
    try:
        sock = socket.socket()
        sock.settimeout(0.5)  # Set a timeout for the connection attempt
        sock.connect((ipaddress, port))
        print(f'[+] Port {port} is Open')
    except (socket.timeout, ConnectionRefusedError):
        print(f'[-] Port {port} is Closed')
    except Exception as e:
        print(f'Error scanning port {port}: {e}')
    finally:
        sock.close()  # Close the socket to free resources

def main():
    ipaddress = input('[+] Enter Target To Scan: ')
    
    # Validate IP address
    try:
        IP(ipaddress)  # This will raise an error if the IP is invalid
    except ValueError:
        print("[-] Invalid IP address format.")
        return
    
    print(f"[+] Scanning {ipaddress}...")
    for port in range(70, 90):
        scan_port(ipaddress, port)

if __name__ == "__main__":
    main()

