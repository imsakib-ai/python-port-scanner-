#!/usr/bin/env python3

import socket
import sys

def scan_port(host, port):
    """Scan a single port on the target host"""
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # 1 second timeout
        
        # Attempt connection
        result = sock.connect_ex((host, port))
        
        if result == 0:
            print(f"[+] Port {port}: OPEN")
            
            # Try to grab banner (service identification)
            try:
                sock.send(b'HEAD / HTTP/1.0\r\n\r\n')
                banner = sock.recv(1024).decode().strip()
                print(f"    Service: {banner[:50]}")  # First 50 chars only
            except:
                print(f"    Service: Unknown")
        
        sock.close()
        
    except socket.error:
        pass
    except KeyboardInterrupt:
        print("\n[!] Scan interrupted by user")
        sys.exit(0)

def main():
    """Main function"""
    print("=" * 50)
    print("    Simple Port Scanner v1.0")
    print("=" * 50)
    
    # Get target from user
    target = input("Enter target IP or hostname: ")
    
    # Get port range
    start_port = int(input("Enter start port (default 1): ") or "1")
    end_port = int(input("Enter end port (default 1024): ") or "1024")
    
    print(f"\n[*] Scanning target: {target}")
    print(f"[*] Port range: {start_port} - {end_port}")
    print("[*] Press Ctrl+C to stop\n")
    
    # Scan ports
    try:
        for port in range(start_port, end_port + 1):
            scan_port(target, port)
    except KeyboardInterrupt:
        print("\n[!] Scan stopped by user")
    
    print("\n[*] Scan complete!")

if __name__ == "__main__":
    main()