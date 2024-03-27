
## Tasks

- Complete Copilot training: https://github.com/bparanj/skills-copilot-codespaces-vscode?tab=readme-ov-file

- Create a new Nuxt app and setup NuxtUI
- Create a layout with nav bar, main and footer sections
- Create a dashboard layout for logged in users. Tabs: Billers, Bills, Cash etc
- Follow the steps in magic-link.md and get the feature to work locally.
- Test the instructions in [Securing Rails API](./securing-rails-api.md)

## Learning

- Learn about Vue 3 Forms (watch Pluralsight course)

## Followups

- Handling callbacks in Nuxt https://www.reddit.com/r/Nuxt/comments/18hosy4/handling_authentication_callback/
- Using Auth0 with magic link in Rails API backend: https://community.auth0.com/t/ruby-on-rails-api-authorization-complete-developer-guide/99144/2
- Securing Rails API with Vue frontend: https://www.reddit.com/r/Supabase/comments/18g1cea/comment/kd24dpj/?context=3

## Articles

- [Auth0 with Rails Backend](https://developer.auth0.com/resources/guides/api/rails/basic-authorization)

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
