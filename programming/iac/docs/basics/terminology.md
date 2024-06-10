## Terminology

### Heuristic

The term for a rule that helps you to choose between potential solutions is a "Heuristic." 

Heuristics are strategies or approaches that guide problem-solving, decision-making, or discovery. They simplify the processes of finding solutions through practical methods not guaranteed to be optimal or perfect but sufficient for reaching an immediate, short-term goal or approximation. In various contexts, including design, engineering, and everyday decision-making, heuristics serve as valuable tools for navigating complex or uncertain situations by providing a framework for making choices without exhaustive analysis.

### Approach

The term for a way of implementing something that is not necessarily the only or the best way for a particular situation is an "Approach."

## Cloud Resource Management

What is the term for managing collections of infrastructure resources provisioned from cloud platforms?

## Terms

- Cloud Service 
- Server Image
- Container Orchestration Service
- Cloud Resource Tool (Terraform)
- Server Configuration Tool (Ansible - Configuration Management Tool) 

### Stack

The term for a collection of infrastructure resources that are defined and changed together is "Infrastructure as Code" (IaC). However, when specifically referring to a collection of resources treated as a single unit, the term "Stack" is often used within the context of IaC. A "stack" can be understood as a group of infrastructure components—such as networks, servers, and services—that are managed together as a unit, based on templates or definitions provided in code form. This approach allows for the entire infrastructure setup to be versioned, replicated, and managed with the same control and efficiency as application code.

AWS uses several specific terminologies related to networking in the AWS cloud. Here are some of the key terms:

1. Virtual Private Cloud (VPC):
   - A virtual network dedicated to your AWS account.
   - It allows you to launch AWS resources in a logically isolated virtual network environment.

2. Subnet:
   - A range of IP addresses within a VPC.
   - Subnets can be classified as public or private.

3. Internet Gateway (IGW):
   - A horizontally scalable and highly available VPC component that allows communication between instances in your VPC and the internet.
   - It provides a target in your VPC route tables for internet-routable traffic.

4. NAT Gateway:
   - A managed service that allows instances in a private subnet to connect to the internet or other AWS services while preventing the internet from initiating connections to those instances.
   - It provides outbound internet access for instances in private subnets.

5. Elastic IP (EIP):
   - A static IPv4 address allocated to your AWS account.
   - EIPs can be dynamically remapped to any EC2 instance or network interface in the same region.

6. Security Group:
   - A virtual firewall that controls inbound and outbound traffic at the instance level.
   - It acts as a permissive rule set, allowing specified traffic to reach or leave the associated instances.

7. Network Access Control List (NACL):
   - An optional layer of security for your VPC that acts as a firewall for controlling traffic in and out of one or more subnets.
   - It operates at the subnet level and provides a rule set that can allow or deny traffic.

8. VPC Peering:
   - A networking connection between two VPCs that enables you to route traffic between them using private IPv4 or IPv6 addresses.
   - It allows instances in different VPCs to communicate with each other as if they were in the same network.

9. Direct Connect:
   - A dedicated network connection that you can establish between your on-premises network and AWS.
   - It provides a private, high-bandwidth, and low-latency connection to AWS services.

10. Route Table:
    - A set of rules, called routes, that determine where network traffic from your subnet or gateway is directed.
    - Each route specifies a destination and a target, such as an Internet Gateway, NAT Gateway, or another subnet.

11. Elastic Network Interface (ENI):
    - A virtual network interface that you can attach to an EC2 instance.
    - It represents a logical networking component in a VPC that can include attributes such as an IP address, security groups, and MAC address.

12. VPC Endpoint:
    - A scalable and highly available networking component that allows you to privately connect your VPC to supported AWS services without requiring an Internet Gateway, NAT device, VPN connection, or AWS Direct Connect.
    - It enables instances in your VPC to use their private IP addresses to communicate with resources in other services.

These are some of the core networking terms used in AWS. Understanding these concepts is essential for designing and managing secure and scalable network architectures in the AWS cloud.
