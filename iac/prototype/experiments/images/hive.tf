provider "aws" {
  region = var.aws_region
}

data "aws_caller_identity" "current" {}

resource "tls_private_key" "hive_key" {
  algorithm = "RSA"
  rsa_bits  = 2048
}

resource "random_string" "hive_key_suffix" {
  length  = 8
  special = false
  upper   = false
}

resource "aws_secretsmanager_secret" "hive_key_secret" {
  name = "hive_key_secret-${random_string.hive_key_suffix.result}"
}

resource "aws_secretsmanager_secret_version" "hive_key_version" {
  secret_id     = aws_secretsmanager_secret.hive_key_secret.id
  secret_string = tls_private_key.hive_key.private_key_pem
}

resource "aws_key_pair" "deployer" {
  key_name   = var.key_name
  public_key = tls_private_key.hive_key.public_key_openssh
}

resource "aws_vpc" "hive_vpc" {
  cidr_block           = var.vpc_cidr_block
  enable_dns_support   = true
  enable_dns_hostnames = true
  tags = {
    Name = "hive-vpc"
  }
}

resource "aws_subnet" "hive_public_subnet" {
  vpc_id                  = aws_vpc.hive_vpc.id
  cidr_block              = "10.0.10.0/24"
  map_public_ip_on_launch = true
  availability_zone       = "us-west-2a"
  tags = {
    Name = "hive-public-subnet"
  }
}

resource "aws_internet_gateway" "hive_igw" {
  vpc_id = aws_vpc.hive_vpc.id
  tags = {
    Name = "hive-igw"
  }
}

resource "aws_route_table" "hive_public_rt" {
  vpc_id = aws_vpc.hive_vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.hive_igw.id
  }

  tags = {
    Name = "hive-public-rt"
  }
}

resource "aws_route_table_association" "hive_public_rt_association" {
  subnet_id      = aws_subnet.hive_public_subnet.id
  route_table_id = aws_route_table.hive_public_rt.id
}

resource "aws_security_group" "hive_sg" {
  name        = var.security_group_name
  description = "Allow inbound traffic for SSH"
  vpc_id      = aws_vpc.hive_vpc.id

  ingress {
    description = "SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = var.ssh_cidr_blocks
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

resource "aws_instance" "rails_instance" {
  ami                    = var.source_ami_name
  instance_type          = var.instance_type
  subnet_id              = aws_subnet.hive_public_subnet.id
  vpc_security_group_ids = [aws_security_group.hive_sg.id]
  key_name               = var.key_name

  tags = {
    Name = "HiveImage"
  }
}
