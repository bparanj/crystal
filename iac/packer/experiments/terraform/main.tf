provider "aws" {
  region     = var.aws_region
  access_key = var.aws_access_key
  secret_key = var.aws_secret_key
}

resource "tls_private_key" "ror_key" {
  algorithm = "RSA"
  rsa_bits  = 2048
}

resource "random_string" "ror_key_suffix" {
  length  = 8
  special = false
  upper   = false
}

resource "aws_secretsmanager_secret" "ror_key_secret" {
  name = "ror_key_secret-${random_string.ror_key_suffix.result}"
}

resource "aws_secretsmanager_secret_version" "ror_key_version" {
  secret_id     = aws_secretsmanager_secret.ror_key_secret.id
  secret_string = tls_private_key.ror_key.private_key_pem
}

resource "aws_key_pair" "deployer" {
  key_name   = var.key_name
  public_key = tls_private_key.ror_key.public_key_openssh
}

resource "aws_vpc" "rails_vpc" {
  cidr_block           = var.vpc_cidr_block
  enable_dns_support   = true
  enable_dns_hostnames = true
  tags = {
    Name = "rails-vpc"
  }
}

resource "aws_subnet" "rails_public" {
  vpc_id                  = aws_vpc.rails_vpc.id
  cidr_block              = var.subnet_cidr_block
  map_public_ip_on_launch = true
  availability_zone       = var.availability_zone
  tags = {
    Name = "rails-public"
  }
}

resource "aws_internet_gateway" "rails_igw" {
  vpc_id = aws_vpc.rails_vpc.id
  tags = {
    Name = "rails-igw"
  }
}

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

resource "aws_route_table" "rails_public" {
  vpc_id = aws_vpc.rails_vpc.id

  route {
    cidr_block = var.route_table_cidr_block
    gateway_id = aws_internet_gateway.rails_igw.id
  }

  tags = {
    Name = var.route_table_name
  }
}

resource "aws_route_table_association" "rails_a" {
  subnet_id      = aws_subnet.rails_public.id
  route_table_id = aws_route_table.rails_public.id
}

resource "aws_instance" "rails" {
  ami                    = var.ami_id
  instance_type          = var.instance_type
  subnet_id              = aws_subnet.rails_public.id
  vpc_security_group_ids = [aws_security_group.rails_sg.id]
  key_name               = var.key_name

  tags = {
    Name = "RailsStack"
  }
}
