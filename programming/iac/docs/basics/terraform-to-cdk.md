Here's the converted AWS CDK code in Python based on the provided Terraform HCL template:

```python
from aws_cdk import (
    aws_ec2 as ec2,
    aws_secretsmanager as secretsmanager,
    core,
    aws_iam as iam,
)
import boto3

class RailsAppStack(core.Stack):
    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Get the current AWS account ID
        aws_account_id = boto3.client('sts').get_caller_identity().get('Account')

        # Get the latest AMI with the specified filters
        latest_ami = ec2.MachineImage.lookup(
            name="UbuntuImage",
            filters={
                "tag:Name": ["UbuntuImage"],
                "tag:Version": ["0.0.26"],
            },
            owners=[aws_account_id],
            most_recent=True,
        )

        # Create an Elastic IP
        static_ip = ec2.CfnEIP(self, "StaticIP", tags={"Name": "RailsAppEIP"})

        # Create a VPC
        vpc = ec2.Vpc(
            self,
            "RailsVPC",
            cidr="10.0.0.0/16",
            enable_dns_support=True,
            enable_dns_hostnames=True,
        )

        # Create a public subnet
        public_subnet = vpc.public_subnet(
            "RailsPublicSubnet",
            cidr_block="10.0.10.0/24",
            map_public_ip_on_launch=True,
            availability_zone="us-west-2a",
        )

        # Create a security group
        security_group = ec2.SecurityGroup(
            self,
            "RailsSecurityGroup",
            vpc=vpc,
            allow_all_outbound=True,
            description="Allow inbound traffic for PostgreSQL, Rails, Redis, and SSH",
        )

        # Add inbound rules to the security group
        security_group.add_ingress_rule(
            ec2.Peer.ipv4("0.0.0.0/0"), ec2.Port.tcp(2222), "SSH"
        )
        security_group.add_ingress_rule(
            ec2.Peer.ipv4("0.0.0.0/0"), ec2.Port.tcp(80), "Rails HTTP"
        )
        security_group.add_ingress_rule(
            ec2.Peer.ipv4("0.0.0.0/0"), ec2.Port.tcp(443), "Rails HTTPS"
        )
        security_group.add_ingress_rule(
            ec2.Peer.ipv4("10.0.0.0/16"), ec2.Port.tcp(5432), "PostgreSQL"
        )
        security_group.add_ingress_rule(
            ec2.Peer.ipv4("10.0.0.0/16"), ec2.Port.tcp(6379), "Redis"
        )

        # Generate a key pair
        key_pair = ec2.KeyPair(self, "RailsKeyPair", name="rails-key-pair")

        # Store the private key in Secrets Manager
        secret = secretsmanager.Secret(
            self, "RORKeySecret", secret_name=f"ror_key_secret-{core.Token.as_string()}"
        )
        secret.attach_secret_string(key_pair.private_key)

        # Create an EC2 instance
        instance = ec2.Instance(
            self,
            "RailsInstance",
            instance_type=ec2.InstanceType("t2.micro"),
            machine_image=latest_ami,
            vpc=vpc,
            vpc_subnets=ec2.SubnetSelection(subnets=[public_subnet]),
            security_group=security_group,
            key_name=key_pair.key_pair_name,
            associate_public_ip_address=True,
        )

        # Associate the Elastic IP with the EC2 instance
        ec2.CfnEIPAssociation(
            self,
            "StaticIPAssociation",
            eip=static_ip.ref,
            instance_id=instance.instance_id,
        )

        # Output the public IP of the EC2 instance
        core.CfnOutput(
            self,
            "RailsInstancePublicIP",
            value=instance.instance_public_ip,
            description="Public IP of the Rails EC2 instance",
        )

app = core.App()
RailsAppStack(app, "RailsAppStack")
app.synth()
```

In this converted code:

1. The necessary AWS CDK modules are imported,  `aws_ec2` for EC2 resources, `aws_secretsmanager` for Secrets Manager, `core` for CDK core constructs, and `aws_iam` for IAM.

2. The `RailsAppStack` class is defined, which represents the stack for the Rails application.

3. The current AWS account ID is retrieved using the boto3 client.

4. The latest AMI with the specified filters is looked up using `ec2.MachineImage.lookup()`.

5. An Elastic IP is created using `ec2.CfnEIP()`.

6. A VPC is created using `ec2.Vpc()`, and a public subnet is added to the VPC using `vpc.public_subnet()`.

7. A security group is created using `ec2.SecurityGroup()`, and inbound rules are added using `security_group.add_ingress_rule()`.

8. A key pair is generated using `ec2.KeyPair()`, and the private key is stored in Secrets Manager using `secretsmanager.Secret()`.

9. An EC2 instance is created using `ec2.Instance()`, specifying the instance type, machine image, VPC, subnet, security group, and key pair.

10. The Elastic IP is associated with the EC2 instance using `ec2.CfnEIPAssociation()`.

11. The public IP of the EC2 instance is outputted using `core.CfnOutput()`.

12. The CDK app is created, and the `RailsAppStack` is instantiated.

13. The app is synthesized using `app.synth()`.

Note: Make sure to have the necessary AWS CDK dependencies installed and the AWS credentials properly configured before running the code.

This conversion provides a starting point for deploying the Rails application using AWS CDK with Python. You may need to further customize and extend the code based on your specific requirements and any additional resources or configurations needed for your Rails application.
