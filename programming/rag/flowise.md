Below is an example **Packer** template in **HCL2 format** (recommended for Packer 1.7+) that will create an **Amazon Linux 2** AMI with **Flowise** installed and configured to run via **PM2** at boot. Once built, you can use the resulting AMI in your **Terraform** configuration to spin up an EC2 instance that is ready to serve Flowise on port 3000.

> **Notes**  
> 1. This example uses **Amazon Linux 2**. You can switch to a different base AMI if you prefer Ubuntu or another OS.  
> 2. By default, Flowise listens on port **3000**. To make Flowise accessible, ensure this port is opened in your AWS Security Group.  
> 3. This template includes a basic **systemd** unit for **PM2** so that Flowise starts on reboot.  
> 4. Adjust IAM instance profile, region, subnet_id, vpc_id, etc., in the builders section per your environment requirements.  
> 5. Make sure that your AWS credentials are properly configured in your environment variables or credentials file so Packer can authenticate.

---

```hcl
packer {
  # We use the HCL Packer templates. For older versions, you may use JSON.
  required_plugins {
    amazon = {
      version = ">= 1.0.0"
      source  = "hashicorp/amazon"
    }
  }
}

# -------------------------
# VARIABLES
# -------------------------
variable "aws_region" {
  type    = string
  default = "us-east-1"
}

variable "flowise_repo" {
  type    = string
  default = "https://github.com/FlowiseAI/Flowise.git"
}

variable "instance_type" {
  type    = string
  default = "t3.micro"
}

variable "ami_name" {
  type    = string
  default = "flowise-ami"
}

# Use the latest Amazon Linux 2 AMI in your region
data "amazon-amis" "amzn2" {
  owners      = ["amazon"]
  most_recent = true

  filters = {
    name                = "amzn2-ami-kernel-*-hvm-*-x86_64-gp2"
    state               = "available"
    root-device-type    = "ebs"
    virtualization-type = "hvm"
  }
  region = var.aws_region
}

# -------------------------
# BUILDERS
# -------------------------
source "amazon-ebs" "flowise" {
  region                    = var.aws_region
  instance_type            = var.instance_type
  ami_name                 = "${var.ami_name}-${timestamp()}"
  source_ami               = data.amazon-amis.amzn2.ids[0]
  ssh_username             = "ec2-user"

  # If you have a specific subnet_id or vpc_id, set them here, for example:
  # subnet_id = "subnet-123456"
  # vpc_id    = "vpc-abcdef"
  
  # Add your temporary keypair name if needed
  # temporary_key_pair_name = "packer-temp-key"

  # By default, Packer uses an ephemeral security group with all inbound blocked.
  # If you need to further customize the security group, you can define a custom one here.
  
  # If your account has a required IAM Instance Profile, specify:
  # iam_instance_profile = "MyIamProfile"

  # Increase or decrease these timeouts as needed, especially if building Flowise or
  # installing Node takes longer than the default.
  launch_block_device_mappings {
    device_name = "/dev/xvda"
    volume_size = 20
    volume_type = "gp2"
    delete_on_termination = true
  }
}

# -------------------------
# PROVISIONERS
# -------------------------
build {
  name    = "build-flowise-ami"
  sources = [
    "source.amazon-ebs.flowise"
  ]

  provisioner "shell" {
    inline = [
      # Update OS
      "sudo yum update -y",

      # Install Node.js 18.x (example) + Git + other dependencies
      "curl -fsSL https://rpm.nodesource.com/setup_18.x | sudo bash -",
      "sudo yum install -y nodejs git",

      # Install pm2 globally
      "sudo npm install -g pm2",

      # Clone Flowise
      "cd /home/ec2-user",
      "git clone ${var.flowise_repo} flowise",
      "sudo chown -R ec2-user:ec2-user flowise",

      # Install dependencies and build
      "cd /home/ec2-user/flowise",
      "npm install",
      "npm run build",
      
      # Use pm2 to run Flowise as a service
      "pm2 start npm --name flowise -- run start",
      "pm2 save",

      # Create a systemd service to manage PM2 so it restarts on reboot
      "sudo tee /etc/systemd/system/pm2-ec2-user.service > /dev/null <<EOF",
      "[Unit]",
      "Description=PM2 for ec2-user",
      "After=network.target",
      "",
      "[Service]",
      "Type=simple",
      "User=ec2-user",
      "LimitNOFILE=infinity",
      "PIDFile=/home/ec2-user/.pm2/pm2.pid",
      "Restart=on-failure",
      "ExecStart=/usr/bin/pm2 resurrect",
      "ExecReload=/usr/bin/pm2 reload all",
      "ExecStop=/usr/bin/pm2 kill",
      "",
      "[Install]",
      "WantedBy=multi-user.target",
      "EOF",

      "sudo systemctl daemon-reload",
      "sudo systemctl enable pm2-ec2-user",
      "sudo systemctl start pm2-ec2-user"
    ]
  }

  # (Optional) Clean up commands, remove build artifacts, logs, etc.
  # Or additional validations can be added here.

  post-processor "manifest" {
    output = "manifest.json"
  }
}
```

## How to Use this Packer Template

1. **Install Packer** if you haven’t already.  
2. Save the above HCL template to a file, e.g., `flowise.pkr.hcl`.  
3. (Optional) Adjust any variables (like `aws_region`, `flowise_repo`, etc.) in the file or via the command line.  
4. Run `packer init flowise.pkr.hcl` to initialize the required plugins.  
5. Run `packer validate flowise.pkr.hcl` to ensure there are no syntax or configuration issues.  
6. Run `packer build flowise.pkr.hcl` to build the AMI.  

Packer will output something similar to:

```
...
amazon-ebs.flowise: AMI: ami-0123456789abcdef
Build 'build-flowise-ami' finished.
...
```

Take note of the **AMI** ID (e.g., `ami-0123456789abcdef`).

---

## Using This AMI in Terraform

Below is a simplified example Terraform snippet that uses the AMI built by Packer. It assumes:

- You have the same region defined in your Terraform.
- You open port **3000** on a security group so that Flowise is accessible.

```hcl
provider "aws" {
  region = "us-east-1"
}

variable "flowise_ami_id" {
  type    = string
  default = "ami-0123456789abcdef"  # Replace with the AMI ID from Packer
}

resource "aws_security_group" "flowise_sg" {
  name        = "flowise-sg"
  description = "Allow port 3000 inbound"
  vpc_id      = "vpc-12345678"  # replace with your VPC ID

  ingress {
    description      = "Flowise inbound"
    from_port        = 3000
    to_port          = 3000
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "flowise_ec2" {
  ami                         = var.flowise_ami_id
  instance_type               = "t3.micro"
  vpc_security_group_ids      = [aws_security_group.flowise_sg.id]
  subnet_id                   = "subnet-abc12345"  # replace with your subnet

  tags = {
    Name = "Flowise-EC2-Instance"
  }
}
```

1. Replace **`ami-0123456789abcdef`** with the AMI ID that Packer created.  
2. Replace **`vpc-12345678`** and **`subnet-abc12345`** with your actual VPC and subnet IDs.  
3. Apply this Terraform configuration, and Terraform will launch an EC2 instance from the Flowise AMI.

---

You now have a **Packer** template that creates a ready-to-go **Flowise** AMI on AWS, along with a sample **Terraform** snippet to deploy that AMI. Adjust and customize as needed for your environment (e.g., more robust IAM roles, different instance sizes, public/private subnets, etc.).
