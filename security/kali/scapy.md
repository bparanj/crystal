**Scapy** is a powerful **Python-based network tool** used for packet crafting, sending, sniffing, and analysis. It allows users to create and manipulate network packets, making it highly useful for network security testing, troubleshooting, and research. Scapy is often used in **penetration testing, network discovery, and packet injection**.

### Key Features of Scapy:
1. **Packet Crafting**: Scapy allows users to construct custom packets for various protocols (e.g., IP, TCP, UDP, ICMP).
2. **Packet Sniffing**: It can capture and analyze packets from live network traffic.
3. **Protocol Support**: It supports a wide range of protocols such as Ethernet, ARP, IP, TCP, UDP, ICMP, DNS, and more.
4. **Network Testing**: Scapy is often used to test firewalls, intrusion detection systems (IDS), and network configurations.
5. **Automation**: Being a Python library, Scapy can be scripted for automated tasks like scanning, probing, or stress testing.

### Example Uses:
- **Penetration Testing**: Crafting packets to test network defenses.
- **Network Forensics**: Capturing and analyzing suspicious traffic.
- **Fuzzing**: Sending malformed packets to test how robust a network service is under unexpected input.

Scapy is a versatile tool, making it valuable for both network administrators and security professionals. It's often included in penetration testing distributions like **Kali Linux**.

In **Scapy**, you can use the **`sr()`** or **`sr1()`** functions to send and receive packets. Here's an example of how you would send a packet and print details from the packet header that is received.

### Example using `sr1()`:
```python
from scapy.all import *

# Create a simple ICMP (ping) packet
packet = IP(dst="8.8.8.8")/ICMP()

# Send the packet and receive the first response
response = sr1(packet)

# Print details from the received packet header
if response:
    print("Source IP:", response[IP].src)
    print("Destination IP:", response[IP].dst)
    print("Protocol:", response[IP].proto)
    print("TTL:", response[IP].ttl)
else:
    print("No response received")
```

### Explanation:
- **`sr1()`**: Sends a packet and waits for one reply. It is used when you expect a single response, like with a ping (ICMP echo request).
- **`response[IP]`**: Accesses the IP layer of the received packet.
- **`response[IP].src`**: Extracts the source IP address from the response.
- **`response[IP].dst`**: Extracts the destination IP address from the response.
- **`response[IP].proto`**: Displays the protocol used (e.g., ICMP, TCP).
- **`response[IP].ttl`**: Prints the Time to Live (TTL) value from the IP header.

This is a basic example for sending and receiving a packet using Scapy and extracting header information from the received packet.
