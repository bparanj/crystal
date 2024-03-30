When using Packer by HashiCorp to create an Amazon Machine Image (AMI) on AWS EC2, the following tasks are performed:

1. Configuration: You define a Packer configuration file (usually in JSON format) that specifies the desired image configuration, including the base AMI, provisioning steps, and post-processing actions.

2. Launching an EC2 instance: Packer launches a new EC2 instance based on the specified base AMI. This instance serves as a temporary build environment.

3. Provisioning: Packer connects to the launched instance and performs the provisioning steps defined in the configuration file. This may include tasks such as installing software, configuring settings, and running scripts. Packer supports various provisioners like shell scripts, Ansible, Chef, Puppet, etc.

4. System configuration: Packer executes any additional system configuration tasks specified in the configuration file, such as setting up users, configuring network settings, or modifying system files.

5. Cleanup: After the provisioning and configuration steps are complete, Packer performs cleanup tasks to prepare the instance for creating an AMI. This may involve actions like stopping services, clearing logs, or removing temporary files.

6. Creating the AMI: Packer takes a snapshot of the configured instance's root volume and registers it as a new AMI in your AWS account. This AMI captures the desired state of the system.

7. Post-processing: Packer can perform post-processing actions on the created AMI, such as tagging the AMI with metadata, encrypting the AMI, or copying the AMI to different regions.

8. Termination: After the AMI creation process is complete, Packer terminates the temporary EC2 instance used for building the image.

By using Packer, you can automate the process of creating custom AMIs with pre-configured software and settings. This allows for consistent and reproducible deployments of EC2 instances based on the created AMI.

Here's an example program using the boto3 Python library to perform steps 1, 2, and 3 of creating an AMI on AWS EC2:

```python
import boto3

# Step 1: Configuration
ami_id = 'ami-0c55b159cbfafe1f0'  # Replace with your desired base AMI ID
instance_type = 't2.micro'
key_name = 'your-key-pair-name'  # Replace with your key pair name
security_group_id = 'sg-0123456789abcdef0'  # Replace with your security group ID
subnet_id = 'subnet-0123456789abcdef0'  # Replace with your subnet ID

# Step 2: Launching an EC2 instance
ec2_client = boto3.client('ec2')

# Launch the EC2 instance
response = ec2_client.run_instances(
    ImageId=ami_id,
    InstanceType=instance_type,
    KeyName=key_name,
    SecurityGroupIds=[security_group_id],
    SubnetId=subnet_id,
    MinCount=1,
    MaxCount=1
)

# Get the instance ID of the launched instance
instance_id = response['Instances'][0]['InstanceId']
print(f"Launched EC2 instance with ID: {instance_id}")

# Wait for the instance to be running
ec2_resource = boto3.resource('ec2')
instance = ec2_resource.Instance(instance_id)
instance.wait_until_running()
print("EC2 instance is now running")

# Step 3: Provisioning
# Install dependencies
install_dependencies_script = '''
#!/bin/bash
sudo apt-get update
sudo apt-get install -y apache2
'''

# Run the provisioning script on the instance
ssm_client = boto3.client('ssm')
response = ssm_client.send_command(
    InstanceIds=[instance_id],
    DocumentName='AWS-RunShellScript',
    Parameters={'commands': [install_dependencies_script]}
)

command_id = response['Command']['CommandId']
print(f"Provisioning command sent with ID: {command_id}")
```

In this program:

1. Configuration:
   - We define the desired configuration parameters, such as the base AMI ID, instance type, key pair name, security group ID, and subnet ID.

2. Launching an EC2 instance:
   - We create an EC2 client using `boto3.client('ec2')`.
   - We launch a new EC2 instance using the `run_instances` method, specifying the configured parameters.
   - We retrieve the instance ID of the launched instance.
   - We wait for the instance to reach the 'running' state using `instance.wait_until_running()`.

3. Provisioning:
   - We define a shell script (`install_dependencies_script`) that updates the package manager and installs Apache2 as an example.
   - We use the AWS Systems Manager (SSM) to send the provisioning script to the instance for execution.
   - We create an SSM client using `boto3.client('ssm')`.
   - We send the provisioning command to the instance using the `send_command` method, specifying the instance ID and the shell script.
   - We retrieve the command ID for reference.

Note: Make sure to replace the placeholders (`ami-0c55b159cbfafe1f0`, `'your-key-pair-name'`, `'sg-0123456789abcdef0'`, `'subnet-0123456789abcdef0'`) with your actual values.

This program demonstrates the basic steps of launching an EC2 instance and provisioning it using a shell script. You can extend this program to include additional provisioning steps, system configuration, and post-processing actions as needed.
