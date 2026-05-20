This project is a Python-based Network Sniffer developed as part of a cybersecurity internship task. It utilizes the scapy library to capture and analyze network packets in real-time. The tool is designed to help understand network protocols and data flow by displaying key information from captured packets.

Features
•Real-time Packet Capture: Sniffs live network traffic on the local interface.
•Protocol Analysis: Identifies and displays IP, TCP, and UDP protocols.
•Data Extraction: Extracts and displays source/destination IP addresses and port numbers.
•Lightweight: Minimal dependencies and easy-to-read output.

Prerequisites
•Python 3.x
•scapy library
•Root/Administrator privileges (required for raw socket access)

Installation
1Clone the repository:
git clone https://github.com/Leharish-07/CodeAlpha_Tasks.git
cd CodeAlpha_Tasks
2Install dependencies:
pip install scapy

Usage
Run the script with administrative privileges:
sudo python3 network_sniffer.py
Once running, the sniffer will display captured packet details in the console. Press Ctrl+C to stop the sniffing process.

Sample Output
Starting network sniffer... Press Ctrl+C to stop.
Source IP: 192.168.1.5, Destination IP: 142.250.190.46, Protocol: 6
    Source Port: 54321, Destination Port: 443
Source IP: 142.250.190.46, Destination IP: 192.168.1.5, Protocol: 6
    Source Port: 443, Destination Port: 54321

Ethical Use Disclaimer
This tool is for educational and authorized testing purposes only. Unauthorized sniffing of network traffic is illegal and unethical. Ensure you have explicit permission before using this tool on any network.

License
This project is licensed under the MIT License.
