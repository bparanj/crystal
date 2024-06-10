To tag an EC2 instance while creating it using Boto3, you can pass the tags as part of the `TagSpecifications` parameter in the `run_instances` method. Here's an example of how you can modify your code to include the tags:

```python
import boto3

ec2_client = boto3.client('ec2')

tags = {
    "Name": "UbuntuImage",
    "Environment": "Production",
    "OS_Version": "Ubuntu 22.04",
    "Release": "Latest",
    "Created-by": "Hive",
    "Version": "0.0.30"
}

tag_specifications = [
    {
        'ResourceType': 'instance',
        'Tags': [{'Key': k, 'Value': v} for k, v in tags.items()]
    }
]

response = ec2_client.run_instances(
    ImageId='ami-0c55b159cbfafe1f0',  # Replace with your desired AMI ID
    InstanceType='t2.micro',  # Replace with your desired instance type
    MinCount=1,
    MaxCount=1,
    TagSpecifications=tag_specifications
)

instance_id = response['Instances'][0]['InstanceId']
print(f"EC2 instance created with ID: {instance_id}")
```

In this code:

1. We define the `tags` dictionary with the desired key-value pairs for the tags.

2. We create a `tag_specifications` list that specifies the resource type as 'instance' and converts the `tags` dictionary into a list of dictionaries in the format required by the `TagSpecifications` parameter.

3. We pass the `TagSpecifications` parameter to the `run_instances` method along with other necessary parameters such as `ImageId` and `InstanceType`.

4. The `run_instances` method creates the EC2 instance with the specified tags.

5. Finally, we retrieve the instance ID from the response and print it.

Make sure to replace `'ami-0c55b159cbfafe1f0'` with the actual AMI ID you want to use for the EC2 instance.

With this code, when the EC2 instance is created, it will have the specified tags associated with it. The tags will be visible in the AWS Management Console and can be used for various purposes, such as identifying and filtering instances based on tags.

In Boto3, tagging an Amazon Machine Image (AMI) directly at the moment of its creation during an EC2 instance launch isn't possible. The process involves two steps: first, launching the EC2 instance, and then creating an AMI from that instance. The tags can be applied when creating the AMI.

Here's how you can create an EC2 instance and then create an AMI from that instance with the specified tags using Boto3:

```python
import boto3

# Initialize a boto3 EC2 client
ec2 = boto3.client('ec2')

# Launch an EC2 instance (simplified for example purposes)
response = ec2.run_instances(
    ImageId='ami-1234567890abcdef0',  # Example AMI ID
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=1
    # Add additional parameters as needed
)

# Assuming the instance launches successfully, get the Instance ID
instance_id = response['Instances'][0]['InstanceId']

# Wait for the instance to be in a running state (optional but recommended)
waiter = ec2.get_waiter('instance_running')
waiter.wait(InstanceIds=[instance_id])

# Create tags list in the format required by Boto3
tags = [
    {"Key": "Name", "Value": "UbuntuImage"},
    {"Key": "Environment", "Value": "Production"},
    {"Key": "OS_Version", "Value": "Ubuntu 22.04"},
    {"Key": "Release", "Value": "Latest"},
    {"Key": "Created-by", "Value": "Hive"},
    {"Key": "Version", "Value": "0.0.30"}
]

# Create an AMI from the instance
ami_response = ec2.create_image(InstanceId=instance_id, Name='UbuntuImage', TagSpecifications=[
    {
        'ResourceType': 'image',
        'Tags': tags
    },
    {
        'ResourceType': 'snapshot',
        'Tags': tags
    }
])

print(f"AMI ID: {ami_response['ImageId']}")
```

This script does the following:
1. **Launches an EC2 instance** using `run_instances`. You'll need to replace `ImageId` with the AMI ID you wish to use for the instance. This example assumes you're launching one `t2.micro` instance.
2. **Waits for the instance to enter the "running" state**. This step is optional but recommended to ensure that the instance is fully initialized and ready.
3. **Defines tags** in the format expected by Boto3 for tagging operations.
4. **Creates an AMI from the running instance** with `create_image`, applying the tags to both the image and its snapshots via the `TagSpecifications` parameter. This is where you specify the tags you wish to apply.

### Note:

- Replace `ImageId` with the actual AMI ID you want to use for launching the instance.
- The instance is launched immediately and runs until you stop or terminate it, which may incur AWS charges.
- Adjust the instance type and other parameters as needed for your specific use case.
