

- Allocate an Elastic IP address for Amazon EC2 (same as this:)
- [Associate an Elastic IP address with an Amazon EC2 instance](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/python/example_code/ec2/elastic_ip.py)


- Create an Amazon EC2 security group
- [Create a security key pair for Amazon EC2](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/python/example_code/ec2/key_pair.py)

- [Create security group](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/python/example_code/ec2/security_group.py)
- Create and run an Amazon EC2 instance
- Set inbound rules for an Amazon EC2 security group
- Using the AWS docs for boto, add error handing and idemptotency to boto3 project

- [Complete Scenario](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/python/example_code/ec2/scenario_get_started_instances.py)

https://rick-hightower.blogspot.com/2017/03/setting-up-ansible-ssh-to-configure-aws.html

Look at Claude answers for boto questions

https://github.com/bparanj/learning-nuxt/blob/main/iac/docs/ansible/custom-ami.md
https://github.com/bparanj/learning-nuxt/blob/main/iac/docs/ansible/ec2.md
https://github.com/bparanj/learning-nuxt/blob/main/iac/docs/ansible/one-box.md


Packer Template to Boto3 Tasks

- Review docs/boto/customize-ami.md

- Run the master playbook:

```
playbook_file   = "../ansible/playbooks/master_playbook.yml"
```

- Copy and include all the playbooks in the playbooks directory.

- Establish SSH connection from Ansible control node to EC2 instance. [Done]

- Identify the AMI with unique name. Review ami-name.md
	
- Extract the latest Ubuntu 22.04 AMI name from the AWS EC2 AMI search using Ansible. [Done]

- Review docs/boto/public-ami.md

- Review docs/boto/tag-ami.md

- Review and extract action items from Boto3 equivalent of post-processor in Packer /docs/boto/post-processor.md


Pending claude

- Should I use this flag in boto3:

```
"ANSIBLE_HOST_KEY_CHECKING=False"
```

Terraform Template to Boto3 Tasks

- In boto3, how to retrieve the custom AMI I have created using the tag filter:
	tag name and tag version 

- How to allocate static IP to EC2 instance when it is created in boto3?

- How to store PEM file in AWS secrets manager in boto3

- Using boto3, create RailsVPC

resource "aws_vpc" "rails_vpc" {
  cidr_block           = var.vpc_cidr_block
  enable_dns_support   = true
  enable_dns_hostnames = true
  tags = {
    Name = "rails-vpc"
  }
}

- Using boto3, create RailsPublicSubnet

resource "aws_subnet" "rails_public_subnet" {
  vpc_id                  = aws_vpc.rails_vpc.id
  cidr_block              = "10.0.10.0/24"
  map_public_ip_on_launch = true
  availability_zone       = "us-west-2a"
  tags = {
    Name = "rails-public-subnet"
  }
}

- Using boto3, create RailsIGW

resource "aws_internet_gateway" "rails_igw" {
  vpc_id = aws_vpc.rails_vpc.id
  tags = {
    Name = "rails-igw"
  }
}

- Using boto3, create route table

resource "aws_route_table" "rails_public_rt" {
  vpc_id = aws_vpc.rails_vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.rails_igw.id
  }

  tags = {
    Name = "rails-public-rt"
  }
}

Why do we need the route table?

- Using boto3, associate the route table to the rails public subnet

- Using boto3, create Rails security group:

resource "aws_security_group" "rails_sg" {
  name        = var.security_group_name
  description = "Allow inbound traffic for PostgreSQL, Rails, Redis, and SSH"
  vpc_id      = aws_vpc.rails_vpc.id

  ingress {
    description = "SSH"
    from_port   = 2222
    to_port     = 2222
    protocol    = "tcp"
    cidr_blocks = var.ssh_cidr_blocks
  }

  ingress {
    description = "Rails HTTP"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = var.http_cidr_blocks
  }

  ingress {
    description = "Rails HTTPS"
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = var.https_cidr_blocks
  }

  # Only allow PostgreSQL and Redis access within the VPC
  ingress {
    description = "PostgreSQL"
    from_port   = 5432
    to_port     = 5432
    protocol    = "tcp"
    cidr_blocks = var.postgres_cidr_blocks
  }

  ingress {
    description = "Redis"
    from_port   = 6379
    to_port     = 6379
    protocol    = "tcp"
    cidr_blocks = var.redis_cidr_blocks
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = var.security_group_name
  }
}

Why do we need egress rule?

- Using boto3, create Rails EC2 instance:

resource "aws_instance" "rails_instance" {
  ami                         = data.aws_ami.latest_ami.id
  instance_type               = var.instance_type
  subnet_id                   = aws_subnet.rails_public_subnet.id
  vpc_security_group_ids      = [aws_security_group.rails_sg.id]
  key_name                    = var.key_name
  associate_public_ip_address = true

  tags = {
    Name = "RailsApplication"
  }
}


Note:

The playbooks:
	iac/prototype/experiments/ansible/experiments/ec2.yml
	iac/prototype/experiments/ansible/experiments/test.yml

have issues with SSH connection. See boto3 project for alternate way to accomplish the same task.
