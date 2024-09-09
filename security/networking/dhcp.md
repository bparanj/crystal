### What is DHCP?

**DHCP (Dynamic Host Configuration Protocol)** is a network management protocol used to automate the process of configuring devices on IP networks. This protocol dynamically assigns IP addresses and other network configuration parameters to devices, enabling them to communicate on an IP network without manual configuration.

### Key Functions of DHCP:

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

### Sources:
- [Cisco: Understanding DHCP](https://www.cisco.com/c/en/us/support/docs/ip/dynamic-host-configuration-protocol-dhcp/13788-9.html)
- [Microsoft Docs: DHCP Overview](https://docs.microsoft.com/en-us/windows-server/networking/technologies/dhcp/dhcp-overview)
- [RFC 2131: Dynamic Host Configuration Protocol](https://tools.ietf.org/html/rfc2131)

DHCP is a protocol in IP networking that simplifies the configuration and management of network devices by dynamically assigning IP addresses and other necessary parameters. This improves network efficiency and reduces the administrative overhead associated with manual IP address assignment.

DHCP reservation, also sometimes called static DHCP assignment or DHCP static mapping.

Here's a brief explanation of how it works:

1. Instead of configuring a static IP address on the host device itself, you configure the DHCP server to always assign a specific IP address to that device.

2. This is typically done by associating the device's MAC address with a particular IP address in the DHCP server's configuration.

3. When the device requests an IP address from the DHCP server, the server recognizes its MAC address and assigns it the pre-configured IP address.

This approach combines the benefits of static IP addressing (consistent, known IP addresses for specific devices) with the convenience of DHCP (centralized management, automatic configuration on the client side).

DHCP reservation is particularly useful in environments where you want to maintain centralized control over IP addressing while ensuring certain devices (like servers, printers, or network equipment) always receive the same IP address.

The term that refers to establishing a TCP session is "handshake" or more specifically, the "three-way handshake."

The TCP three-way handshake is the process used to establish a connection between two devices using the TCP (Transmission Control Protocol) protocol. It's called a "three-way" handshake because it involves three steps:

1. SYN (Synchronize): The client sends a SYN packet to the server to initiate the connection.

2. SYN-ACK (Synchronize-Acknowledge): The server responds with a SYN-ACK packet to acknowledge the client's request.

3. ACK (Acknowledge): The client sends an ACK packet back to the server to acknowledge the server's response.

After these three steps are completed successfully, a TCP connection is established and data can begin to flow between the client and server.

This process ensures that both sides are ready to communicate and helps to synchronize sequence numbers used for tracking the conversation.
