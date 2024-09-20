## DHCP

### What is DHCP?

**DHCP (Dynamic Host Configuration Protocol)** is a network management protocol used to automate the process of configuring devices on IP networks. This protocol dynamically assigns IP addresses and other network configuration parameters to devices, enabling them to communicate on an IP network without manual configuration.

### Key Functions:

1. **Automatic IP Address Assignment**:
   - DHCP automatically assigns IP addresses to devices on a network, eliminating the need for manual configuration by network administrators. This simplifies network management and reduces the risk of IP address conflicts.

2. **Configuration of Network Parameters**:
   - In addition to IP addresses, DHCP can assign other network configuration parameters such as:
     - Subnet mask
     - Default gateway
     - DNS servers
     - Lease time for the IP address

3. **Lease Management**:
   - DHCP assigns IP addresses on a lease basis, meaning each IP address is assigned for a specific period. This ensures efficient use of IP addresses and allows addresses to be reassigned when devices disconnect from the network.

### How DHCP Works:

1. **DHCP Discover**:
   - A client device that joins a network sends a DHCP Discover message to locate a DHCP server.

2. **DHCP Offer**:
   - The DHCP server responds with a DHCP Offer message, which includes an available IP address and other network configuration parameters.

3. **DHCP Request**:
   - The client responds with a DHCP Request message, indicating its acceptance of the offered IP address and parameters.

4. **DHCP Acknowledgment**:
   - The DHCP server sends a DHCP Acknowledgment (ACK) message, confirming the lease and assigning the IP address to the client.

### Benefits of DHCP:

1. **Simplified Network Management**:
   - DHCP automates the configuration process, making it easier for network administrators to manage large networks.

2. **Efficient IP Address Utilization**:
   - By dynamically assigning IP addresses, DHCP ensures efficient use of available IP addresses and reduces the risk of conflicts.

3. **Flexibility**:
   - DHCP supports both static and dynamic IP address assignment, providing flexibility for different network environments.

DHCP is a protocol in IP networking that simplifies the configuration and management of network devices by dynamically assigning IP addresses and other necessary parameters. This improves network efficiency and reduces the administrative overhead associated with manual IP address assignment.

DHCP reservation, also sometimes called static DHCP assignment or DHCP static mapping.

1. Instead of configuring a static IP address on the host device itself, you configure the DHCP server to always assign a specific IP address to that device.

2. This is  done by associating the device's MAC address with a particular IP address in the DHCP server's configuration.

3. When the device requests an IP address from the DHCP server, the server recognizes its MAC address and assigns it the pre-configured IP address.

This approach combines the benefits of static IP addressing (consistent, known IP addresses for specific devices) with the convenience of DHCP (centralized management, automatic configuration on the client side).

DHCP reservation is useful in environments where you want to maintain centralized control over IP addressing while ensuring certain devices (like servers, printers, or network equipment) always receive the same IP address.

The term that refers to establishing a TCP session is "handshake" or more specifically, the "three-way handshake."

The TCP three-way handshake is the process used to establish a connection between two devices using the TCP (Transmission Control Protocol) protocol. It's called a "three-way" handshake because it involves three steps:

1. SYN (Synchronize): The client sends a SYN packet to the server to initiate the connection.

2. SYN-ACK (Synchronize-Acknowledge): The server responds with a SYN-ACK packet to acknowledge the client's request.

3. ACK (Acknowledge): The client sends an ACK packet back to the server to acknowledge the server's response.

After these three steps are completed successfully, a TCP connection is established and data can begin to flow between the client and server.

This process ensures that both sides are ready to communicate and helps to synchronize sequence numbers used for tracking the conversation.

When configuring a DHCP server for a Small Office/Home Office (SOHO) network, you have some flexibility in choosing IP addresses, but there are guidelines and best practices to follow.

1. Private IP Address Ranges:
   For SOHO networks, you should use private IP address ranges as defined by RFC 1918. These are:

   - 10.0.0.0 to 10.255.255.255 (10.0.0.0/8)
   - 172.16.0.0 to 172.31.255.255 (172.16.0.0/12)
   - 192.168.0.0 to 192.168.255.255 (192.168.0.0/16)

2. Common SOHO Choices:
   Most SOHO routers default to using:
   - 192.168.0.0/24 (255.255.255.0)
   - 192.168.1.0/24 (255.255.255.0)

3. Avoiding Conflicts:
   - Ensure the range you choose doesn't conflict with other networks you might connect to (e.g., via VPN).
   - If you're using multiple subnets, make sure they don't overlap.

4. Size Considerations:
   - For most SOHO networks, a /24 subnet (providing 254 usable IP addresses) is sufficient.
   - If you need more addresses, you could use a larger subnet like /23 or /22.

5. Router/Server IP:
   - Typically, you'd assign a static IP to your router/DHCP server at the beginning or end of the range.
   - Common choices are x.x.x.1 or x.x.x.254

6. DHCP Range:
   - Set your DHCP range to leave some IPs available for static assignment.
   - For example, if using 192.168.1.0/24:
     - Router: 192.168.1.1
     - DHCP range: 192.168.1.50 to 192.168.1.200
     - Static IPs: Can use 2-49 and 201-254

Given your previous configuration using 172.18.0.0/16, this is a valid choice for a SOHO network, although it provides far more addresses than  needed (65,534 usable addresses). If you want to stick with this range, you could consider:

- Server/Router IP: 172.18.0.1
- DHCP Range: 172.18.0.10 to 172.18.0.254
- Subnet Mask: 255.255.0.0

While you can choose any IP within the private ranges, it's often best to stick with common practices unless you have a specific reason to do otherwise. This makes troubleshooting easier and reduces the likelihood of conflicts if connecting to other networks.
