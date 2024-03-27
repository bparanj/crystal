To create an Internet Gateway (IGW) and attach it to your VPC named "RailsVPC" using boto3, you'll follow these steps. This process involves creating the internet gateway, then attaching it to the specified VPC. It mirrors the Terraform configuration for creating and tagging an internet gateway.

Here’s how you can do it in Python with boto3:

```python
import boto3

# Assuming you have the VPC ID from the previous operation
# vpc_id = 'your-vpc-id-here'

# For demonstration, let's fetch the VPC ID by its name (e.g., "rails-vpc")
ec2 = boto3.resource('ec2')
vpcs = list(ec2.vpcs.filter(Filters=[{'Name': 'tag:Name', 'Values': ['rails-vpc']}]))

if not vpcs:
    print("No VPC found with the name 'rails-vpc'. Please check the VPC name and try again.")
else:
    vpc_id = vpcs[0].id
    print(f"Using VPC ID: {vpc_id}")

    # Create an EC2 client
    ec2_client = boto3.client('ec2')

    # Create an Internet Gateway
    igw_response = ec2_client.create_internet_gateway(
        TagSpecifications=[
            {
                'ResourceType': 'internet-gateway',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': 'rails-igw'
                    }
                ]
            }
        ]
    )

    # Extract Internet Gateway ID from response
    igw_id = igw_response['InternetGateway']['InternetGatewayId']

    # Attach the Internet Gateway to the VPC
    attach_response = ec2_client.attach_internet_gateway(
        InternetGatewayId=igw_id,
        VpcId=vpc_id
    )

    print(f"Internet Gateway ID: {igw_id} has been created and attached to VPC ID: {vpc_id}")
```

### Key Steps:

1. **Fetch the VPC ID**: This code snippet includes an example of how to fetch the VPC ID by the VPC's name ('rails-vpc'). This assumes you have already created a VPC named "rails-vpc" and that it's uniquely named within your AWS account.
   
2. **Create the Internet Gateway**: We create an internet gateway and tag it with the name 'rails-igw'. 

3. **Attach the Internet Gateway to the VPC**: After creating the internet gateway, we attach it to the specified VPC using its ID.

### Important Notes:

- Make sure to replace `'your-vpc-id-here'` with the actual ID of your VPC if you already know it, or use the provided method to fetch it based on the VPC's name.
- This script assumes that your VPC is uniquely identifiable by its name. If you have multiple VPCs with the same name, you'll need to refine the selection logic.
- AWS charges for some resources and actions. While there's typically no charge for creating and attaching an internet gateway, it's always a good idea to review the current AWS pricing details.