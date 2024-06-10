## Provisioning with Terraform

### Hello Terraform

Create main.tf:

```hcl
variable "ami" {
  type        = string
  description = "Application Image to Deploy"
}

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
    Name = "allow_static_website"
  }
}

resource "aws_instance" "test_ami" {
  ami                    = "ami-0844feea1591c1bcf"
  instance_type          = "t2.micro"
  vpc_security_group_ids = [aws_security_group.allow_static_website.id]

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
```

The AMI id is hardcoded in this file.

```
terraform init
terraform plan
```

```
terraform apply
```

Cleanup:

```
terraform destroy
```

Modify the template to pull the latest image without prompting for image id during apply:

```
data "aws_ami" "packer_image" {
  most_recent = true

  filter {
    name   = "tag:Created-by"
    values = ["Packer"]
  }

  owners = ["self"]
}
```

```
resource "aws_instance" "test_ami" {
  instance_type          = "t2.micro"
  vpc_security_group_ids = [aws_security_group.allow_static_website.id]

  ami = data.aws_ami.packer_image.id

  tags = {
    "Name" = var.appname
  }
}
```

Remove the ami variable:

```
variable "ami" {
  type = string
  description = "Application Image to Deploy"
}
```

.gitignore for Terraform:

```
# Local .terraform directories
**/.terraform/*

# .tfstate files
*.tfstate
*.tfstate.*

# Crash log files
crash.log
crash.*.log

# Exclude all .tfvars files, which are likely to contain sensitive data, such as
# password, private keys, and other secrets. These should not be part of version
# control as they are data points which are potentially sensitive and subject 
# to change depending on the environment.
*.tfvars
*.tfvars.json

# Ignore override files as they are usually used to override resources locally and so
# are not checked in
override.tf
override.tf.json
*_override.tf
*_override.tf.json

# Include override files you do wish to add to version control using negated pattern
# !example_override.tf

# Include tfplan files to ignore the plan output of command: terraform plan -out=tfplan
# example: *tfplan*

# Ignore CLI configuration files
.terraformrc
terraform.rc


# Local .terraform directories
**/.terraform/*

# Ignore variables files
*.auto.tfvars

# Ignore override files
*.tfoverride

# Ignore environment-specific files
.envrc

# Ignore CLI configuration files
.terraformrc
terraform.rc
# Cache objects
packer_cache/
```
