## Backlog Review

- Allocate an Elastic IP address for Amazon EC2 (same as this:)
- [Associate an Elastic IP address with an Amazon EC2 instance](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/python/example_code/ec2/elastic_ip.py)

- Create an Amazon EC2 security group
- [Create a security key pair for Amazon EC2](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/python/example_code/ec2/key_pair.py)

- [Create security group](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/python/example_code/ec2/security_group.py)
- Create and run an Amazon EC2 instance
- Set inbound rules for an Amazon EC2 security group
- Using the AWS docs for boto, add error handing and idemptotency to boto3 project

- [Complete Scenario](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/python/example_code/ec2/scenario_get_started_instances.py)

- https://rick-hightower.blogspot.com/2017/03/setting-up-ansible-ssh-to-configure-aws.html
- https://github.com/bparanj/learning-nuxt/blob/main/iac/docs/ansible/custom-ami.md
- https://github.com/bparanj/learning-nuxt/blob/main/iac/docs/ansible/ec2.md
- https://github.com/bparanj/learning-nuxt/blob/main/iac/docs/ansible/one-box.md
- https://github.com/Apress/practicle-ansible/blob/main/code/ch6_2_roles_splunk_server_tasks_main.yml
- https://docs.aws.amazon.com/code-library/latest/ug/python_3_ec2_code_examples.html
- https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/python/example_code/iam/user_wrapper.py


## Packer Template to Boto3 Tasks

- Review docs/boto/customize-ami.md
- Run the master playbook:

```
playbook_file   = "../ansible/playbooks/master_playbook.yml"
```

- Identify the AMI with unique name. Review ami-name.md
- Copy and include all the playbooks in the playbooks directory.
- Review docs/boto/public-ami.md
- Review docs/boto/tag-ami.md
- Review and extract action items from Boto3 equivalent of post-processor in Packer /docs/boto/post-processor.md

## Done

- Establish SSH connection from Ansible control node to EC2 instance. 	
- Extract the latest Ubuntu 22.04 AMI name from the AWS EC2 AMI search using Ansible. 

## John's Notes

Create a VPC:

```python
import boto3

# Initialize a boto3 client
ec2 = boto3.resource('ec2', region_name='us-west-2')  # Use your desired region

# Create a VPC
vpc = ec2.create_vpc(CidrBlock='10.0.0.0/16')  # Your VPC CIDR block
vpc.create_tags(Tags=[{"Key": "Name", "Value": "BalasVPC"}])
vpc.wait_until_available()

# Enable DNS support and DNS hostnames
ec2_client = boto3.client('ec2', region_name='us-west-2')
ec2_client.modify_vpc_attribute(VpcId=vpc.id, EnableDnsSupport={'Value': True})
ec2_client.modify_vpc_attribute(VpcId=vpc.id, EnableDnsHostnames={'Value': True})

print(f"Created VPC: {vpc.id}")
```

Create Subnets:

```python
# Define your subnet configurations
public_subnets_cidr = ["10.0.0.0/24", "10.0.1.0/24"]
private_subnets_cidr = ["10.0.2.0/24", "10.0.3.0/24"]

# Fetch availability zones
zones = ec2_client.describe_availability_zones()['AvailabilityZones']
zone_names = [zone['ZoneName'] for zone in zones]

# Create public subnets
public_subnet_ids = []
for idx, cidr_block in enumerate(public_subnets_cidr):
    subnet = ec2.create_subnet(CidrBlock=cidr_block, VpcId=vpc.id, AvailabilityZone=zone_names[idx % len(zone_names)], MapPublicIpOnLaunch=True)
    subnet.create_tags(Tags=[{"Key": "Name", "Value": f"PublicSubnet-{idx}"}])
    public_subnet_ids.append(subnet.id)

# Create private subnets
private_subnet_ids = []
for idx, cidr_block in enumerate(private_subnets_cidr):
    subnet = ec2.create_subnet(CidrBlock=cidr_block, VpcId=vpc.id, AvailabilityZone=zone_names[idx % len(zone_names)])
    subnet.create_tags(Tags=[{"Key": "Name", "Value": f"PrivateSubnet-{idx}"}])
    private_subnet_ids.append(subnet.id)

print(f"Public Subnets: {public_subnet_ids}")
print(f"Private Subnets: {private_subnet_ids}")

Create Security Group and Rules

# Create Security Group
security_group = ec2.create_security_group(
    GroupName='allow_ssh', 
    Description='Allow SSH access', 
    VpcId=vpc.id
)

# Add Ingress Rule to allow SSH
security_group.authorize_ingress(
    CidrIp='76.43.33.4/32',  # Replace with your IP
    IpProtocol='tcp',
    FromPort=22,
    ToPort=22
)

# Add Egress Rule to allow all outbound traffic
security_group.authorize_egress(
    IpPermissions=[
        {
            'IpProtocol': '-1',
            'IpRanges': [{'CidrIp': '0.0.0.0/0'}],
            'UserIdGroupPairs': [],
            'PrefixListIds': [],
        },
    ]
)

print(f"Created Security Group: {security_group.id}")
```

Launch EC2 Instance:

```python
# Launch EC2 Instance
instances = ec2.create_instances(
    ImageId='ami-0fe7e11d0d4fdbdbf',  # Replace with a valid AMI ID for your region
    InstanceType='t3.small',
    MaxCount=1,
    MinCount=1,
    NetworkInterfaces=[{
        'SubnetId': public_subnet_ids[0],  # Attach to first public subnet
        'DeviceIndex': 0,
        'AssociatePublicIpAddress': True,
        'Groups': [security_group.id]
    }],
    KeyName='your-key-pair-name',  # Replace with your key pair name
    UserData='''#!/bin/bash
                echo 'your-public-ssh-key' >> /home/ubuntu/.ssh/authorized_keys
                ''',  # Customize as needed
)

# Wait for the instance to be running
instances[0].wait_until_running()

# Reload to get public IP address
instances[0].reload()

print(f"Launched EC2 Instance: {instances[0].id}")
print(f"Instance Public IP: {instances[0].public_ip_address}")

# Associate Elastic IP (if needed)
eip = ec2_client.allocate_address(Domain='vpc')
ec2_client.associate_address(InstanceId=instances[0].id, AllocationId=eip['AllocationId'])

print(f"Associated Elastic IP: {eip['PublicIp']}")
```

Note:

The playbooks:
	iac/prototype/experiments/ansible/experiments/ec2.yml
	iac/prototype/experiments/ansible/experiments/test.yml

have issues with SSH connection. See boto3 project for alternate way to accomplish the same task. These playbooks are no longer required.