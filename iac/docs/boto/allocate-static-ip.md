To allocate a static IP address to an Amazon EC2 instance at creation time using boto3, you need to allocate an Elastic IP (EIP) and then associate it with your EC2 instance after the instance has been launched. This process involves a few steps:

1. **Launch an EC2 Instance**: First, launch your EC2 instance without specifying any IP address. You will get an instance ID upon successful launch.
2. **Allocate an Elastic IP (EIP)**: Allocate a new EIP for your account.
3. **Associate the Elastic IP with Your Instance**: Once you have both the instance ID and the allocation ID of the EIP, you can associate the EIP with the instance.

Here's the code using boto3:

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

- **AMI ID and Instance Type**: Replace `'ami-12345678'` with the AMI ID of the image you want to use for your instance, and `'t2.micro'` with the instance type that suits your needs.
- **Key Pair**: Replace `'your-key-pair'` with the name of an existing key pair for SSH access. If you don't need SSH access or are handling it differently, you can adjust the parameters accordingly.
- **EIP Domain**: When allocating an EIP, specify the `Domain` as `'vpc'` for instances in a VPC (which is the common scenario these days). If you are working within EC2-Classic (much less common now), you would use `'standard'`.

This covers the basics of launching an instance and assigning it a static IP address. Remember, AWS charges for Elastic IPs that are allocated but not associated with a running instance, so be sure to release any Elastic IPs you no longer need to avoid unnecessary charges.

To allocate a static IP (Elastic IP) to an EC2 instance when it is created using boto3, you can follow these steps:

1. Allocate an Elastic IP address using the `allocate_address()` method of the EC2 client.
2. Create the EC2 instance using the `run_instances()` method.
3. Associate the Elastic IP address with the EC2 instance using the `associate_address()` method.

Here's an example code snippet that demonstrates this process:

```python
import boto3

def create_ec2_instance_with_elastic_ip():
    ec2_client = boto3.client('ec2')
    
    # Allocate Elastic IP address
    allocation = ec2_client.allocate_address(Domain='vpc')
    elastic_ip = allocation['PublicIp']
    allocation_id = allocation['AllocationId']
    
    # Create EC2 instance
    response = ec2_client.run_instances(
        ImageId='ami-xxxxxxxx',  # Replace with your desired AMI ID
        InstanceType='t2.micro',  # Replace with your desired instance type
        MinCount=1,
        MaxCount=1,
        KeyName='my-key-pair',  # Replace with your key pair name
        SecurityGroupIds=['sg-xxxxxxxx']  # Replace with your security group ID
    )
    
    instance_id = response['Instances'][0]['InstanceId']
    
    # Wait for the instance to be in a running state
    waiter = ec2_client.get_waiter('instance_running')
    waiter.wait(InstanceIds=[instance_id])
    
    # Associate Elastic IP with the instance
    ec2_client.associate_address(
        AllocationId=allocation_id,
        InstanceId=instance_id
    )
    
    print(f"EC2 instance created with ID: {instance_id}")
    print(f"Elastic IP {elastic_ip} associated with the instance")

# Example usage
create_ec2_instance_with_elastic_ip()
```

In this example, we define a function `create_ec2_instance_with_elastic_ip()` that performs the following steps:

1. We create an EC2 client using `boto3.client('ec2')`.

2. We allocate an Elastic IP address using the `allocate_address()` method, specifying the `Domain` as `'vpc'`. We store the allocated public IP address in the `elastic_ip` variable and the allocation ID in the `allocation_id` variable.

3. We create an EC2 instance using the `run_instances()` method, providing the desired AMI ID, instance type, key pair name, and security group ID. Adjust these parameters according to your requirements.

4. We retrieve the instance ID from the response of the `run_instances()` method.

5. We use a waiter to wait for the instance to be in a running state before proceeding.

6. We associate the Elastic IP address with the EC2 instance using the `associate_address()` method, passing the `allocation_id` and the `instance_id`.

7. Finally, we print the instance ID and the associated Elastic IP address.

In the example usage, we simply call the `create_ec2_instance_with_elastic_ip()` function to create an EC2 instance with an associated Elastic IP address.

Note: Make sure to replace the placeholders (`'ami-xxxxxxxx'`, `'my-key-pair'`, `'sg-xxxxxxxx'`) with the appropriate values for your AMI ID, key pair name, and security group ID.

Ensure that you have the necessary permissions to allocate Elastic IP addresses and create EC2 instances in your AWS account.
