Table of **Host-Only**, **Bridged**, and **NAT** network types in virtualization networking:

| Network Type | Function                                                 | IP Assignment                 | Use Case                                         |
|--------------|-----------------------------------------------------------|-------------------------------|-------------------------------------------------|
| Host-Only    | Isolates VMs from external network; connects only to host | Host assigns private IP        | Testing or private network between VM and host  |
| Bridged      | Direct access to the external network through host's NIC  | VM gets IP from physical network | VM acts like a physical device on the network    |
| NAT          | VMs use host's IP to access external network via translation | Host provides private IP; uses NAT | VMs access internet but isolated from external devices |

This table summarizes the differences and use cases for Host-Only, Bridged, and NAT networks.

Problems each network type solves:

| Network Type | Problem Solved                                                                 |
|--------------|--------------------------------------------------------------------------------|
| Host-Only    | Provides an isolated environment where VMs communicate only with the host, ensuring no external network interference. |
| Bridged      | Allows VMs to behave like physical devices on the network, solving the problem of integrating VMs into the same network as the host for full network access. |
| NAT          | Enables VMs to access the external internet while keeping them isolated from the physical network, solving the issue of external visibility while allowing internet access. |

Each type addresses different connectivity needs based on isolation, integration, and security.

Networking Terms:

| Concept      | Term                          | Definition                                                                                  |
|--------------|-------------------------------|----------------------------------------------------------------------------------------------|
| Isolation    | **Network Segmentation**       | Dividing a network into segments to control access and communication between systems.         |
| Integration  | **Network Bridging**           | Connecting different network segments to allow seamless communication between them.           |
| Security     | **Network Security**           | Measures to protect network integrity, confidentiality, and availability (e.g., firewalls, encryption). |

These terms reflect key principles in network design and management.

## Network Architecture

Is there one term that represents isolation, integration and security?

Yes, the term **network architecture** can encompass **isolation, integration, and security**. 

- **Isolation** is achieved through techniques like segmentation and VLANs.
- **Integration** refers to the seamless communication between different network components.
- **Security** is built into the architecture to protect data and resources.

**Network architecture** refers to the overall design and organization of a network,  how isolation, integration, and security measures are implemented to meet specific requirements.
