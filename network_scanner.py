import ipaddress
import subprocess
import platform

def ping(ip):
    """Ping an IP address to see if it's active"""
    
    param = "-n" if platform.system().lower() == "windows" else "-c"
    
    command = ["ping", param, "1", str(ip)]
    
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    return result.returncode == 0


def scan_network(network):
    """Scan a network range for active hosts"""
    
    net = ipaddress.ip_network(network, strict=False)
    
    print(f"\nScanning network: {network}\n")
    
    active_hosts = []
    
    for ip in net.hosts():
        if ping(ip):
            print(f"{ip} is active")
            active_hosts.append(str(ip))
    
    print("\nScan complete.")
    
    if active_hosts:
        print("\nActive devices found:")
        for host in active_hosts:
            print(host)
    else:
        print("No active devices found.")


if __name__ == "__main__":
    
    network = input("Enter network range (example: 192.168.1.0/24): ")
    
    scan_network(network)
