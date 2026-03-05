import socket

""" create function for ports """
def get_service_name(port):
    services = {
        21: "FTP",
        22: "SSH", 
        23: "Telnet", 
        25: "SMTP", 
        53: "DNS",
        80: "HTTP", 
        110: "POP3", 
        143: "IMAP",
        161: "SNMP",
        389: "LDAP",
        443: "HTTPS",
        636 : "LDAPS",
        1723: "PPTP", 
        3306: "MySQL", 
        3389: "RDP"
        }
    return services.get(port, "Unknown")

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.3)
        result = sock.connect_ex((target, port))
        sock.close()
        
        if result == 0:
            return True, get_service_name(port)
        return False, None
    except:
    
        return False, None

def main():
    print("=" * 60)
    print("     SIMPLE PORT SCANNER - Cybersecurity Tool")
    print("=" * 60)

    target = input("\n[*] Enter target IP or hostname: ")
    
    try:
        target_ip = socket.gethostbyname(target)
        print(f"[*] Target IP: {target_ip}")
    except:
        print("[!] Invalid target!")
        return
    
    # chose scan type 
    print("\n[+] Scan options:")
    print("  1. Common ports (21,22,23,25,53,80,110,143,161,389,443,636,1723,3306,3389)")
    print("  2. Custom range")
    
    choice = input("\n[*] Choose option (1/2): ")
    
    open_ports = {}
    
    if choice == "1":
        ports = [21,22,23,25,53,80,110,143,161,389,443,636,1723,3306,3389]
        print(f"\n[*] Scanning {len(ports)} common ports...")
        
        for port in ports:
            is_open, service = scan_port(target_ip, port)
            if is_open:
                open_ports[port] = service
                print(f"[+] Port {port}: {service}")
    
    elif choice == "2":
        start = int(input("[*] Start port: "))
        end = int(input("[*] End port: "))
        
        print(f"\n[*] Scanning ports {start}-{end}...")
        
        for port in range(start, end + 1):
            is_open, service = scan_port(target_ip, port)
            if is_open:
                open_ports[port] = service
                print(f"[+] Port {port}: {service}")
    
    else:
        print("[!] Invalid choice!")
        return
    
    print("\n" + "=" * 60)
    print("SCAN RESULTS SUMMARY")
    print("=" * 60)
    
    if open_ports:
        print(f"\n[✓] Found {len(open_ports)} open ports:")
        for port, service in open_ports.items():
            print(f"  - Port {port:<5} : {service}")
    else:
        print("\n[-] No open ports found")
    
    print("\n[✓] Scan completed!")
if __name__ == "__main__":
    main()