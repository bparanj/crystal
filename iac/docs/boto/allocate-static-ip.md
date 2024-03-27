To allocate a static IP address to an Amazon EC2 instance at creation time using boto3, you need to allocate an Elastic IP (EIP) and then associate it with your EC2 instance after the instance has been launched. This process involves a few steps:

1. **Launch an EC2 Instance**: First, launch your EC2 instance without specifying any IP address. You will get an instance ID upon successful launch.
2. **Allocate an Elastic IP (EIP)**: Allocate a new EIP for your account.
3. **Associate the Elastic IP with Your Instance**: Once you have both the instance ID and the allocation ID of the EIP, you can associate the EIP with the instance.

Here's how you can do it using boto3:

```python
import boto3

# Create an EC2 resource and EC2 client
ec2_resource = boto3.resource('ec2')
ec2_client = boto3.client('ec2')

# Launch an EC2 instance
instance = ec2_resource.create_instances(
    ImageId='ami-12345678',  # Replace with your AMI ID
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',  # Replace with your instance type
    KeyName='your-key-pair'  # Replace with your key pair name
)[0]

# Wait for the instance to be in a running state
instance.wait_until_running()

# Refresh instance attributes
instance.load()

# Allocate an Elastic IP
eip = ec2_client.allocate_address(Domain='vpc')  # 'vpc' for VPCs or 'standard' for EC2-Classic

# Associate the Elastic IP with the EC2 instance
association = ec2_client.associate_address(
    InstanceId=instance.id,
    AllocationId=eip['AllocationId']
)

print(f"Elastic IP {eip['PublicIp']} has been allocated and associated with instance {instance.id}")
```

### Notes:

- **AMI ID and Instance Type**: You need to replace `'ami-12345678'` with the AMI ID of the image you want to use for your instance, and `'t2.micro'` with the instance type that suits your needs.
- **Key Pair**: Ensure you replace `'your-key-pair'` with the name of an existing key pair for SSH access. If you don't need SSH access or are handling it differently, you can adjust the parameters accordingly.
- **EIP Domain**: When allocating an EIP, specify the `Domain` as `'vpc'` for instances in a VPC (which is the common scenario these days). If you are working within EC2-Classic (much less common now), you would use `'standard'`.

This script covers the basics of launching an instance and assigning it a static IP address. Remember, AWS charges for Elastic IPs that are allocated but not associated with a running instance, so be sure to release any Elastic IPs you no longer need to avoid unnecessary charges.

