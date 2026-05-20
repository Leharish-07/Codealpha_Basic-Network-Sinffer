from scapy.all import *

def packet_callback(packet):
    if packet.haslayer(IP):
        source_ip = packet[IP].src
        destination_ip = packet[IP].dst
        protocol = packet[IP].proto
        print(f"Source IP: {source_ip}, Destination IP: {destination_ip}, Protocol: {protocol}")

        if packet.haslayer(TCP):
            source_port = packet[TCP].sport
            destination_port = packet[TCP].dport
            print(f"    Source Port: {source_port}, Destination Port: {destination_port}")
        elif packet.haslayer(UDP):
            source_port = packet[UDP].sport
            destination_port = packet[UDP].dport
            print(f"    Source Port: {source_port}, Destination Port: {destination_port}")

print("Starting network sniffer... Press Ctrl+C to stop.")
sniff(prn=packet_callback, store=0)
