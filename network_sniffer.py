"""
CodeAlpha Internship - Task 1
Basic Network Sniffer (No Scapy Dependency)
Author: [Your Name]
Description:
    Captures network packets using Python's socket library and extracts:
    Source IP, Destination IP, Protocol, and Packet Length.
"""

import socket
import struct

def main():
    # Create a raw socket to capture packets
    # AF_INET = IPv4, SOCK_RAW = raw packets
    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)

    # Bind to your machine's IP (replace with your system IP)
    host_ip = socket.gethostbyname(socket.gethostname())
    sniffer.bind((host_ip, 0))

    # Include IP headers
    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    print(f"Starting packet capture on {host_ip}... Press Ctrl+C to stop.\n")
    while True:
        raw_data, addr = sniffer.recvfrom(65535)
        # Extract IP header (first 20 bytes)
        ip_header = raw_data[0:20]
        iph = struct.unpack('!BBHHHBBH4s4s', ip_header)
        version_ihl = iph[0]
        protocol = iph[6]
        src_ip = socket.inet_ntoa(iph[8])
        dst_ip = socket.inet_ntoa(iph[9])
        length = len(raw_data)

        print(f"Source: {src_ip}  -->  Destination: {dst_ip} | Protocol: {protocol} | Length: {length}")

if __name__ == "__main__":
    main()
