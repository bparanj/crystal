Creating a VPC with an internet gateway, subnet, security groups, and routing configurations using Ansible involves multiple steps. This playbook demonstrates how to set up a simple VPC environment with these components. Adjustments might be needed based on your specific AWS setup and security requirements.

```yaml
---
- name: Create VPC infrastructure
  hosts: localhost
  gather_facts: false
  vars:
    region: us-east-1
    vpc_cidr_block: 10.10.0.0/16
    subnet_cidr_block: 10.10.1.0/24
    project_name: MyProject

  tasks:
    - name: Create a VPC
      amazon.aws.ec2_vpc_net:
        name: "{{ project_name }}-VPC"
        cidr_block: "{{ vpc_cidr_block }}"
        region: "{{ region }}"
        state: present
      register: vpc

    - name: Create an Internet Gateway
      amazon.aws.ec2_vpc_igw:
        vpc_id: "{{ vpc.vpc.id }}"
        state: present
        region: "{{ region }}"
      register: igw

    - name: Create a Subnet
      amazon.aws.ec2_vpc_subnet:
        vpc_id: "{{ vpc.vpc.id }}"
        cidr: "{{ subnet_cidr_block }}"
        az: "{{ region }}a" # Adjust the availability zone as needed
        state: present
        map_public: yes
        region: "{{ region }}"
      register: subnet

    - name: Create a Route Table
      amazon.aws.ec2_vpc_route_table:
        vpc_id: "{{ vpc.vpc.id }}"
        routes:
          - dest: 0.0.0.0/0
            gateway_id: "{{ igw.gateway_id }}"
        subnets:
          - "{{ subnet.subnet.id }}"
        region: "{{ region }}"
      register: route_table

    - name: Create Security Group for Web to DB traffic
      amazon.aws.ec2_group:
        name: "{{ project_name }}-web-to-db"
        description: "Allow web servers to connect to the database"
        vpc_id: "{{ vpc.vpc.id }}"
        rules:
          - proto: tcp
            from_port: 5432 # PostgreSQL port, adjust if using a different DB
            to_port: 5432
            cidr_ip: "{{ subnet_cidr_block }}"
        region: "{{ region }}"

    - name: Create Security Group for Internet to Web
      amazon.aws.ec2_group:
        name: "{{ project_name }}-internet-to-web"
        description: "Allow internet access to web servers"
        vpc_id: "{{ vpc.vpc.id }}"
        rules:
          - proto: tcp
            from_port: 80
            to_port: 80
            cidr_ip: 0.0.0.0/0
          - proto: tcp
            from_port: 443
            to_port: 443
            cidr_ip: 0.0.0.0/0
        region: "{{ region }}"

    - name: Create Security Group for SSH Access
      amazon.aws.ec2_group:
        name: "{{ project_name }}-ssh-access"
        description: "Allow SSH access from a specific IP"
        vpc_id: "{{ vpc.vpc.id }}"
        rules:
          - proto: tcp
            from_port: 22
            to_port: 22
            cidr_ip: YOUR_SSH_ACCESS_IP_HERE/32 # Replace with your IP
        region: "{{ region }}"

    - name: Create Security Group for Outbound Rules
      amazon.aws.ec2_group:
        name: "{{ project_name }}-outbound-rules"
        description: "Security Group with outbound rules to install packages"
        vpc_id: "{{ vpc.vpc.id }}"
        rules_egress:
          - proto: all
            cidr_ip: 0.0.0.0/0
        region: "{{ region }}"
```

### Key Points:

- This playbook creates a VPC, an internet gateway, a subnet, and a route table for outbound connections through the internet gateway.
- It also sets up security groups for different purposes: one for traffic from web servers to the database, one for internet access to web servers, one for SSH access, and one with outbound rules to allow installing packages.
- Replace `YOUR_SSH_ACCESS_IP_HERE` with your actual IP address for SSH access.
- The `amazon.aws.ec2_group` module is used for creating security groups with specific ingress and egress rules based on the requirements.
- Ensure the `amazon.aws` collection is installed (`ansible-galaxy collection install amazon.aws`), and your AWS credentials are configured for Ansible to use.

This playbook is a foundation; tailor it to fit your project's specific AWS environment and security needs.
