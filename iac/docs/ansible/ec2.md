Here's a basic example of an Ansible playbook that uses the `amazon.aws.ec2_instance` module to launch new EC2 instances in AWS. Before running this playbook, ensure you have the required AWS credentials set up in your environment or in your Ansible configuration, and the `amazon.aws` collection installed.

```yaml
---
- name: Launch EC2 Instances
  hosts: localhost
  gather_facts: false
  tasks:
    - name: Launch a new EC2 instance
      amazon.aws.ec2_instance:
        name: "MyEC2Instance"
        key_name: "my-keypair"
        image_id: "ami-1234567890abcdef0" # Use the appropriate AMI for your region and OS
        instance_type: "t2.micro"
        network:
          subnet_id: "subnet-12345678" # Your subnet ID
          assign_public_ip: true
        wait: true
        state: present
        tags:
          Name: "MyEC2Instance"
      register: ec2

    - name: Print the instance ID and IP
      debug:
        msg: "Instance ID is {{ ec2.instance.id }} and public IP is {{ ec2.instance.public_ip_address }}"
```

### Key Points:
- **`name`**: A unique name for the EC2 instance.
- **`key_name`**: The name of the key pair to use. Ensure this key pair exists in your AWS account.
- **`image_id`**: The AMI ID of the image you want to use. This varies by region and your requirements.
- **`instance_type`**: The type of instance (e.g., t2.micro). This determines the hardware of the host computer used for your instance.
- **`network`**: Network configuration, including the subnet ID. Optionally, `assign_public_ip` can be set to `true` to assign a public IP address.
- **`wait`**: If set to `true`, Ansible waits until the instance is in the running state.
- **`state`**: `present` to create the instance, `absent` to terminate it.
- **`tags`**: Optional tags to assign to the instance for identification and management purposes.

Before executing this playbook, replace placeholder values (e.g., `"ami-1234567890abcdef0"`, `"subnet-12345678"`, `"my-keypair"`) with actual values from your AWS account. Ensure the `amazon.aws` collection is installed by running `ansible-galaxy collection install amazon.aws`, and configure your AWS access credentials (e.g., via environment variables, `~/.aws/credentials`, or Ansible vault).

No, you cannot directly use a local PEM file by replacing the `key_name` in the playbook with the PEM file's name. The `key_name` parameter requires the name of an SSH key pair that is already registered with your AWS account. To use your local PEM file, you first need to import it into AWS EC2 as a key pair and then use the name you assigned it during the import in your playbook.

# Create AWS EC2 using Ansible Galaxy

## Environment Setup

Before running the `create_ec2.yml` Ansible playbook to create an EC2 instance, you should complete several preparatory tasks to ensure everything works smoothly. Here’s a list of things to do:

1. **Install Ansible**:
   - Ensure Ansible is installed on your machine. If not, install it using your system's package manager or Python's pip. For example, using pip:
     ```shell
     pip install ansible
     ```

2. **Install Python**:
   - Ansible requires Python. Make sure Python is installed on your system.

3. **Set Up AWS Credentials**:
   - Obtain your AWS Access Key ID and Secret Access Key by creating an IAM user in your AWS account with programmatic access and sufficient permissions to manage EC2 instances.
   - Set these credentials as environment variables for security:
     ```shell
     export AWS_ACCESS_KEY_ID='your_access_key'
     export AWS_SECRET_ACCESS_KEY='your_secret_key'
     ```

4. **Configure SSH Key Pair for EC2**:
   - If you don’t already have an SSH key pair, generate one in the AWS EC2 console. This key pair will be used to securely connect to your EC2 instance after it's launched.
   - Make sure the private key file is securely stored on your system and its permissions are set to be accessible only by you (e.g., `chmod 400 mykey.pem`).

5. **Choose an AMI and Instance Type**:
   - Decide on the Amazon Machine Image (AMI) ID that your EC2 instance will use. The AMI determines the OS and software that will be pre-installed on your instance.
   - Choose an instance type (e.g., `t2.micro`). This determines the hardware specifications of your instance.

6. **Define Security Group and Subnet**:
   - Identify the security group to assign to your EC2 instance. The security group acts as a virtual firewall controlling the traffic to and from the instance.
   - If you're using VPC, determine which subnet to launch your instance into.

7. **Ansible Galaxy Collection**:
   - Install the required Ansible Galaxy collection (`amazon.aws`) if you haven't done so already:
     ```shell
     ansible-galaxy collection install amazon.aws
     ```

8. **Review and Update the Playbook**:
   - Make sure your playbook (`create_ec2.yml`) is updated with the correct key pair name, security group, subnet ID, AMI ID, and any other parameters specific to your setup.

9. **Testing Connectivity**:
   - Ensure you have internet connectivity and the ability to reach AWS endpoints from the machine where you're running Ansible.

10. **Ansible Inventory File**:
    - Although in this case, you're likely running the playbook on localhost, ensure your Ansible inventory file is correctly set up if you plan to manage remote hosts.

By completing these tasks, you ensure that the necessary prerequisites are met for a successful execution of your Ansible playbook to create an EC2 instance on AWS.

## Create EC2 Instance Using Ansible

To use Ansible for creating an Amazon EC2 instance, first, you need to install the `amazon.aws` collection from Ansible Galaxy. Here's a step-by-step guide to get you started:

1. **Install the `amazon.aws` Collection**:
   
   Open your terminal and run the following command to install the `amazon.aws` collection. This collection includes modules and plugins required to interact with AWS services, including EC2.

   ```shell
   ansible-galaxy collection install amazon.aws
   ```

2. **Set Up Your AWS Access Credentials**:

   Before you proceed, ensure you have your AWS access key and secret key available. You can set these up as environment variables for better security and convenience.

   ```shell
   export AWS_ACCESS_KEY_ID='your_access_key'
   export AWS_SECRET_ACCESS_KEY='your_secret_key'
   ```

3. **Create a Playbook for EC2 Instance**:

   A playbook in Ansible defines the tasks you want to automate. Here’s a simple example of a playbook (`create_ec2.yml`) that creates an EC2 instance:

   ```yaml
   ---
   - name: Create an EC2 instance
     hosts: localhost
     gather_facts: no
     collections:
       - amazon.aws
     tasks:
     - name: Launch an instance
       ec2:
         key_name: your_keypair_name
         instance_type: t2.micro
         image: ami-12345678
         wait: yes
         region: us-east-1
         group: your_security_group
         vpc_subnet_id: your_subnet_id
         assign_public_ip: yes
       register: ec2
   ```

   Replace `your_keypair_name`, `ami-12345678`, `your_security_group`, and `your_subnet_id` with your actual AWS key pair name, AMI ID, security group ID, and subnet ID, respectively.

4. **Run the Playbook**:

   Execute your playbook with the following command. This will start the process of creating an EC2 instance based on the configurations you’ve provided.

   ```shell
   ansible-playbook create_ec2.yml
   ```

**Key Takeaways**:

- The `amazon.aws` collection from Ansible Galaxy provides the necessary modules to interact with AWS services.
- Always handle your AWS credentials securely. Using environment variables is one recommended way.
- An Ansible playbook allows you to define and automate tasks, such as creating an EC2 instance.
- Modify the playbook parameters according to your requirements, like instance type, region, and AMI ID.

## Creating Security Group and Subnet

To address item #6, which involves defining a security group and subnet for your EC2 instance, we'll create a simplified Ansible playbook. This playbook will include tasks to create a new security group (if one doesn't already exist) and specify the subnet ID for launching the EC2 instance. We'll assume you already have a VPC where you want to create your security group and instance.

### Ansible Playbook: Setup EC2 with Security Group and Subnet

Below is a sample playbook called `setup_ec2_with_sg_and_subnet.yml`. This playbook demonstrates how to create a security group, allowing SSH access, and then launch an EC2 instance within a specified subnet and security group.

```yaml
---
- name: Setup EC2 instance with a Security Group and Subnet
  hosts: localhost
  gather_facts: no
  collections:
    - amazon.aws

  vars:
    region: us-east-1
    vpc_id: vpc-xxxxxxx
    subnet_id: subnet-yyyyyyy
    security_group_name: MyAnsibleSG
    security_group_description: Security Group created by Ansible
    instance_type: t2.micro
    ami_id: ami-xxxxxxxxxxxx
    key_name: your_keypair_name

  tasks:
    - name: Ensure Security Group exists
      ec2_group:
        name: "{{ security_group_name }}"
        description: "{{ security_group_description }}"
        region: "{{ region }}"
        vpc_id: "{{ vpc_id }}"
        rules:
          - proto: tcp
            ports:
              - 22
            cidr_ip: 0.0.0.0/0
      register: sg

    - name: Launch an EC2 instance
      ec2:
        key_name: "{{ key_name }}"
        instance_type: "{{ instance_type }}"
        image: "{{ ami_id }}"
        wait: yes
        region: "{{ region }}"
        group_id: "{{ sg.group_id }}"
        vpc_subnet_id: "{{ subnet_id }}"
        assign_public_ip: yes
      register: ec2
```

### Key Points to Customize in Your Playbook:
- `region`: AWS region where your resources will be created.
- `vpc_id`: ID of your VPC.
- `subnet_id`: ID of your subnet where the EC2 instance will be launched.
- `security_group_name`: The name for the security group.
- `instance_type`: The type of instance (e.g., `t2.micro`).
- `ami_id`: The AMI ID for the instance.
- `key_name`: Name of your SSH key pair.

This playbook starts by ensuring there's a security group with the specified name allowing SSH access. It then launches an EC2 instance within the defined subnet and security group. Customize the variables to match your AWS environment before running the playbook.

No, you don't necessarily have to create the VPC and subnet manually if you're willing to use Ansible for automation. Ansible allows you to automate the creation of VPCs and subnets using its modules, specifically designed for AWS resource management. Here's how you can extend the playbook to include tasks for creating a VPC and a subnet if they do not already exist:

### Extending the Playbook for VPC and Subnet Creation

```yaml
---
- name: Setup VPC, Subnet, Security Group, and Launch EC2 Instance
  hosts: localhost
  gather_facts: no
  collections:
    - amazon.aws

  vars:
    region: us-east-1
    vpc_cidr_block: "10.10.0.0/16"
    subnet_cidr_block: "10.10.1.0/24"
    availability_zone: us-east-1a
    security_group_name: MyAnsibleSG
    security_group_description: Security Group created by Ansible for EC2
    instance_type: t2.micro
    ami_id: ami-xxxxxxxxxxxx
    key_name: your_keypair_name

  tasks:
    - name: Create a VPC
      ec2_vpc_net:
        name: "MyVPC"
        cidr_block: "{{ vpc_cidr_block }}"
        region: "{{ region }}"
        tags:
          Name: MyVPC
      register: vpc

    - name: Create a Subnet
      ec2_vpc_subnet:
        state: present
        vpc_id: "{{ vpc.vpc.id }}"
        cidr: "{{ subnet_cidr_block }}"
        az: "{{ availability_zone }}"
        tags:
          Name: MySubnet
      register: subnet

    - name: Create Security Group
      ec2_group:
        name: "{{ security_group_name }}"
        description: "{{ security_group_description }}"
        vpc_id: "{{ vpc.vpc.id }}"
        rules:
          - proto: tcp
            ports:
              - 22
            cidr_ip: 0.0.0.0/0
      register: sg

    - name: Launch an EC2 instance
      ec2:
        key_name: "{{ key_name }}"
        instance_type: "{{ instance_type }}"
        image: "{{ ami_id }}"
        wait: yes
        region: "{{ region }}"
        group_id: "{{ sg.group_id }}"
        vpc_subnet_id: "{{ subnet.subnet.id }}"
        assign_public_ip: yes
```

### Key Aspects to Note:

- **VPC and Subnet Creation**: This playbook begins by creating a VPC with the specified CIDR block. It then creates a subnet within this VPC. You can adjust the `vpc_cidr_block` and `subnet_cidr_block` to fit your network design.
- **Security Group**: After setting up the network infrastructure, the playbook creates a security group within the new VPC, allowing SSH access.
- **EC2 Instance Launch**: Finally, it launches an EC2 instance within the newly created subnet and security group.

### Customization:

- **Region, CIDR Blocks, and Availability Zone**: Customize the region, VPC and subnet CIDR blocks, and the availability zone according to your requirements.
- **AMI ID and Instance Type**: Specify the appropriate AMI ID and instance type.
- **Key Pair**: Ensure you have an SSH key pair created in the specified AWS region and provide its name in the playbook.

Using this approach, you can fully automate your AWS environment setup, including network and instance creation, with Ansible. This is particularly useful for creating reproducible environments or for managing infrastructure as code.

## Creating the AWS Resources

For creating AWS resources like a Virtual Private Cloud (VPC) and subnets, you have two main options: manual creation through the AWS Management Console or automated creation using tools like Ansible or AWS CloudFormation. Automating with Ansible can be very efficient and repeatable, especially for software engineers looking to manage infrastructure as code.

If you prefer to automate the creation of a VPC and subnets, you would use Ansible modules like `ec2_vpc_net` and `ec2_vpc_subnet`. However, if you're setting up a simple environment or doing it for the first time, creating them manually via the AWS Console might be a straightforward approach to understand the concepts.

Regarding the AMI ID `ami-12345678`, this is a placeholder value. AMI IDs are region-specific and change over time as new images are released. To find the AMI ID for Ubuntu 22.04 (Jammy Jellyfish) for your specific region:

1. Go to the EC2 Dashboard in the AWS Management Console.
2. Navigate to "Instances" > "Launch Instance".
3. In the "AMI" section, search for "Ubuntu" and filter by your desired version, like "22.04".
4. Ensure you select an AMI based on your region and requirements (e.g., HVM, EBS-optimized instances).

For automation or script use, you can also use the AWS CLI to query for the latest Ubuntu 22.04 AMI ID:

```bash
aws ec2 describe-images --filters "Name=name,Values=ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*" "Name=state,Values=available" --query 'Images[*].[ImageId,CreationDate]' --output text --region your-region | sort -k2 -r | head -n1
```

Replace `your-region` with your actual AWS region. This command filters available images for Ubuntu 22.04, sorts them by the creation date to get the latest one, and outputs the most recent AMI ID.

For tasks like creating a VPC, subnets, or finding the correct AMI ID, automating these can save time and reduce the potential for human error, making it a good practice for software engineers interested in infrastructure automation and cloud computing.

Here's the conversion of the Terraform configuration to an Ansible playbook:

```yaml
---
- name: Provision Rails Infrastructure
  hosts: localhost
  connection: local
  gather_facts: false

  vars:
    aws_region: "us-west-2"
    vpc_cidr_block: "10.0.0.0/16"
    subnet_cidr_block: "10.0.10.0/24"
    availability_zone: "us-west-2a"
    security_group_name: "rails-sg"
    instance_type: "t2.micro"
    key_name: "rails-key"

  tasks:
    - name: Get latest AMI
      ec2_ami_info:
        region: "{{ aws_region }}"
        owners: ["self"]
        filters:
          name: "UbuntuImage"
          "tag:Version": "0.0.26"
      register: latest_ami

    - name: Create Elastic IP
      ec2_eip:
        region: "{{ aws_region }}"
        tags:
          Name: "RailsAppEIP"
      register: static_ip

    - name: Generate RSA private key
      community.crypto.openssh_keypair:
        path: "{{ playbook_dir }}/rails-key.pem"
        size: 2048
        type: rsa

    - name: Create random suffix for secret name
      set_fact:
        secret_suffix: "{{ lookup('password', '/dev/null length=8 chars=ascii_lowercase,digits') }}"

    - name: Create Secrets Manager secret
      aws_secret:
        name: "ror_key_secret-{{ secret_suffix }}"
        state: present

    - name: Store private key in Secrets Manager
      aws_secret:
        name: "ror_key_secret-{{ secret_suffix }}"
        state: present
        secret_type: 'string'
        secret: "{{ lookup('file', '{{ playbook_dir }}/rails-key.pem') }}"

    - name: Create key pair
      ec2_key:
        name: "{{ key_name }}"
        key_material: "{{ lookup('file', '{{ playbook_dir }}/rails-key.pem.pub') }}"
        region: "{{ aws_region }}"

    - name: Create VPC
      ec2_vpc_net:
        name: "rails-vpc"
        cidr_block: "{{ vpc_cidr_block }}"
        region: "{{ aws_region }}"
        tags:
          Name: "rails-vpc"
      register: rails_vpc

    - name: Create public subnet
      ec2_vpc_subnet:
        vpc_id: "{{ rails_vpc.vpc.id }}"
        cidr: "{{ subnet_cidr_block }}"
        az: "{{ availability_zone }}"
        region: "{{ aws_region }}"
        tags:
          Name: "rails-public-subnet"
      register: rails_public_subnet

    - name: Create internet gateway
      ec2_vpc_igw:
        vpc_id: "{{ rails_vpc.vpc.id }}"
        region: "{{ aws_region }}"
        tags:
          Name: "rails-igw"
      register: rails_igw

    - name: Create public route table
      ec2_vpc_route_table:
        vpc_id: "{{ rails_vpc.vpc.id }}"
        region: "{{ aws_region }}"
        subnets:
          - "{{ rails_public_subnet.subnet.id }}"
        routes:
          - dest: 0.0.0.0/0
            gateway_id: "{{ rails_igw.gateway_id }}"
        tags:
          Name: "rails-public-rt"

    - name: Create security group
      ec2_group:
        name: "{{ security_group_name }}"
        description: "Allow inbound traffic for PostgreSQL, Rails, Redis, and SSH"
        vpc_id: "{{ rails_vpc.vpc.id }}"
        region: "{{ aws_region }}"
        rules:
          - proto: tcp
            from_port: 2222
            to_port: 2222
            cidr_ip: "{{ ssh_cidr_blocks }}"
          - proto: tcp
            from_port: 80
            to_port: 80
            cidr_ip: "{{ http_cidr_blocks }}"
          - proto: tcp
            from_port: 443
            to_port: 443
            cidr_ip: "{{ https_cidr_blocks }}"
          - proto: tcp
            from_port: 5432
            to_port: 5432
            cidr_ip: "{{ postgres_cidr_blocks }}"
          - proto: tcp
            from_port: 6379
            to_port: 6379
            cidr_ip: "{{ redis_cidr_blocks }}"
        rules_egress:
          - proto: all
            cidr_ip: 0.0.0.0/0
      register: rails_sg

    - name: Launch Rails EC2 instance
      ec2_instance:
        image_id: "{{ latest_ami.images[0].image_id }}"
        instance_type: "{{ instance_type }}"
        vpc_subnet_id: "{{ rails_public_subnet.subnet.id }}"
        security_group: "{{ rails_sg.group_id }}"
        key_name: "{{ key_name }}"
        assign_public_ip: yes
        region: "{{ aws_region }}"
        tags:
          Name: "RailsApplication"
      register: rails_instance

    - name: Associate Elastic IP with Rails instance
      ec2_eip:
        device_id: "{{ rails_instance.instance_ids[0] }}"
        ip: "{{ static_ip.public_ip }}"
        region: "{{ aws_region }}"
      register: eip_association
```

This playbook performs the following tasks:

1. Retrieves the latest AMI based on the specified filters.
2. Creates an Elastic IP.
3. Generates an RSA private key.
4. Creates a random suffix for the secret name.
5. Creates a Secrets Manager secret.
6. Stores the private key in the Secrets Manager secret.
7. Creates a key pair using the public key.
8. Creates a VPC.
9. Creates a public subnet within the VPC.
10. Creates an internet gateway and attaches it to the VPC.
11. Creates a public route table and associates it with the public subnet.
12. Creates a security group with the specified inbound and outbound rules.
13. Launches an EC2 instance for the Rails application using the latest AMI, subnet, security group, and key pair.
14. Associates the Elastic IP with the Rails EC2 instance.

Replace the placeholders (e.g., `{{ ssh_cidr_blocks }}`, `{{ http_cidr_blocks }}`, etc.) with the appropriate values based on your requirements.

Also, ensure that you have the necessary Ansible modules installed (`community.crypto`, `amazon.aws`) and the AWS credentials properly configured for authentication.
