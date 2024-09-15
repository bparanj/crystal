To set the name of an EC2 instance using Boto3, you can add a tag with the key "Name" and the desired value. Here's an example of how you can modify your code to include the instance name:

```python
import boto3
from datetime import datetime

ec2_client = boto3.client('ec2')

# Generate the AMI name with timestamp
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
ami_name = f"hive-ubuntu-aws-{timestamp}"

# Define the tags for the EC2 instance
tags = [
    {
        'ResourceType': 'instance',
        'Tags': [
            {
                'Key': 'Name',
                'Value': ami_name
            },
            # Add other tags as needed
        ]
    }
]

response = ec2_client.run_instances(
    ImageId='ami-0c55b159cbfafe1f0',  # Replace with your desired AMI ID
    InstanceType='t2.micro',  # Replace with your desired instance type
    MinCount=1,
    MaxCount=1,
    TagSpecifications=tags
)

instance_id = response['Instances'][0]['InstanceId']
print(f"EC2 instance created with ID: {instance_id}")
print(f"Instance name: {ami_name}")
```

In this code:

1. We import the `datetime` module to generate a timestamp for the AMI name.

2. We generate the AMI name by concatenating the prefix "hive-ubuntu-aws-" with the current timestamp using string formatting. The timestamp is obtained using `datetime.now().strftime("%Y%m%d%H%M%S")`, which formats the current date and time as a string in the format "YYYYMMDDHHMMSS".

3. We define the tags for the EC2 instance in the `tags` list. The first tag has the key "Name" and the value set to `ami_name`, which is the generated AMI name with the timestamp.

4. We pass the `TagSpecifications` parameter to the `run_instances` method, specifying the `tags` list.

5. The `run_instances` method creates the EC2 instance with the specified tags,  the "Name" tag.

6. Finally, we retrieve the instance ID from the response and print it along with the AMI name.

When the EC2 instance is created, it will have the specified name tag associated with it. The name tag will be visible in the AWS Management Console and can be used to easily identify and manage the instance.

Make sure to replace `'ami-0c55b159cbfafe1f0'` with the  AMI ID you want to use for the EC2 instance.

By using the timestamp in the AMI name, each instance created with this code will have a unique name based on the creation time. This can be helpful for tracking and identifying instances based on when they were created.

In Boto3, when launching an EC2 instance, you don't directly specify an `ami_name` because the name attribute isn't part of the instance launch parameters. Instead, you assign a name to an EC2 instance by creating a tag with the key `Name`. This tag's value can be any string you choose,  dynamic content like a timestamp.

Here's how you can launch an EC2 instance with a dynamically generated name that includes a timestamp, using Boto3:

```python
import boto3
from datetime import datetime

# Initialize the Boto3 EC2 resource
ec2 = boto3.resource('ec2')

# Generate a timestamp
timestamp = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

# Define the instance name
instance_name = f"hive-ubuntu-aws-{timestamp}"

# Specify the AMI ID and instance type
ami_id = 'ami-xxxxxxxxxxxxxxxxx'  # Replace with your AMI ID
instance_type = 't2.micro'

# Launch the instance
instances = ec2.create_instances(
    ImageId=ami_id,
    InstanceType=instance_type,
    MinCount=1,
    MaxCount=1,
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': instance_name
                }
            ]
        }
    ]
)

print(f"Launched EC2 instance with ID: {instances[0].id}")
```

In this script:
- The `datetime.now().strftime('%Y-%m-%d-%H-%M-%S')` function generates a string representation of the current timestamp.
- This timestamp is incorporated into the `instance_name` variable using an f-string: `f"hive-ubuntu-aws-{timestamp}"`.
- The `ec2.create_instances` method launches a new EC2 instance with the specified AMI ID and instance type. The `TagSpecifications` parameter includes a tag with the key `Name` and the dynamically generated `instance_name` as its value.
- Finally, the script prints the ID of the launched instance.

Replace `'ami-xxxxxxxxxxxxxxxxx'` with the  AMI ID you wish to use for launching your instance. This approach allows you to dynamically name your EC2 instances with a unique identifier based on the current timestamp, facilitating better management and identification of your instances.

