variable "region" {
  type    = string
  default = "us-west-2"
}

variable "appname" {
  type        = string
  description = "Application Name"
}

provider "aws" {
  region = var.region
}

data "aws_ami" "packer_image" {
  most_recent = true

  filter {
    name   = "tag:Created-by"
    values = ["Packer"]
  }

  owners = ["self"]
}

resource "aws_security_group" "allow_static_website" {
  name        = "allow_static_website"
  description = "Allow inbound traffic to static website"

  ingress {
    description = "Static Website Inbound Traffic"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = var.appname
  }
}
resource "aws_instance" "test_ami" {
  instance_type          = "t2.micro"
  vpc_security_group_ids = [aws_security_group.allow_static_website.id]

  ami = data.aws_ami.packer_image.id

  tags = {
    "Name" = var.appname
  }
}

output "public_ip" {
  value = aws_instance.test_ami.public_ip
}

output "public_dns" {
  value = aws_instance.test_ami.public_dns
}

output "static_website" {
  value = "http://${aws_instance.test_ami.public_dns}:80"
}
