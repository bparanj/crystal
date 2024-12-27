Here's the updated **HCL template** to use **Ubuntu 24.04** as the base image:

---

### Updated `packer-template.pkr.hcl`

```hcl
packer {
  required_plugins {
    amazon = {
      version = ">= 1.5.0"
      source  = "hashicorp/amazon"
    }
    ansible = {
      version = ">= 1.0.0"
      source  = "hashicorp/ansible"
    }
  }
}

variable "aws_region" {
  default = "us-east-1"
}

variable "ami_name" {
  default = "streamlit-app-{{timestamp}}"
}

source "amazon-ebs" "ubuntu" {
  region                 = var.aws_region
  source_ami_filter {
    filters = {
      name                = "ubuntu/images/*ubuntu-24.04*"
      virtualization-type = "hvm"
      root-device-type    = "ebs"
    }
    owners = ["099720109477"] # Canonical's owner ID for Ubuntu AMIs
    most_recent = true
  }
  instance_type          = "t2.micro"
  ssh_username           = "ubuntu"
  ami_name               = var.ami_name
}

build {
  sources = ["source.amazon-ebs.ubuntu"]

  provisioner "ansible" {
    playbook_file = "playbook.yml"
  }
}
```

---

### Key Changes:
1. **Ubuntu Version Update**:
   - The `name` filter for `source_ami_filter` now includes `ubuntu-24.04`.

2. **Region and Other Fields**:
   - Remain the same but are adaptable if further customization is needed.

3. **Canonical Owner ID**:
   - `099720109477` ensures only official Ubuntu images are used.

---

### Steps After Updating:
1. Reinitialize Packer:
   ```bash
   packer init .
   ```
2. Validate the updated template:
   ```bash
   packer validate .
   ```
3. Build the image:
   ```bash
   packer build .
   ```

This template will use the most recent **Ubuntu 24.04** AMI as the base for your custom image.

## Terraform

Here’s a **Terraform HCL template** to deploy the Packer-built AMI on an AWS EC2 Free Tier instance:

---

### Directory Structure
Organize your files like this:
```
terraform-ec2/
├── main.tf         # Main Terraform configuration
├── variables.tf    # Variables definition (optional)
├── outputs.tf      # Outputs configuration
```

---

### 1. **`main.tf`**
The main Terraform configuration:

```hcl
provider "aws" {
  region = var.aws_region
}

resource "aws_instance" "ec2_free_tier" {
  ami           = var.ami_id
  instance_type = "t2.micro" # Free tier eligible instance type
  key_name      = var.key_name

  tags = {
    Name = "Streamlit-EC2"
  }

  provisioner "remote-exec" {
    inline = [
      "sudo apt update && sudo apt install -y python3-pip",
      "pip3 install streamlit",
      "nohup streamlit run app.py --server.port=80 --server.address=0.0.0.0 &"
    ]

    connection {
      type        = "ssh"
      user        = "ubuntu"
      private_key = file(var.private_key_path)
      host        = self.public_ip
    }
  }

  # Allow HTTP traffic for Streamlit
  vpc_security_group_ids = [aws_security_group.streamlit_sg.id]
}

resource "aws_security_group" "streamlit_sg" {
  name_prefix = "streamlit-sg"

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
```

---

### 2. **`variables.tf`**
Define variables for reusability:

```hcl
variable "aws_region" {
  default = "us-east-1"
}

variable "ami_id" {
  description = "AMI ID of the Packer image"
}

variable "key_name" {
  description = "Name of the EC2 key pair"
}

variable "private_key_path" {
  description = "Path to the private key file (.pem)"
}
```

---

### 3. **`outputs.tf`**
Outputs to provide key information after deployment:

```hcl
output "public_ip" {
  description = "Public IP of the deployed EC2 instance"
  value       = aws_instance.ec2_free_tier.public_ip
}

output "public_dns" {
  description = "Public DNS of the deployed EC2 instance"
  value       = aws_instance.ec2_free_tier.public_dns
}
```

---

### Steps to Deploy:
1. **Export the Packer AMI ID**:
   After building the AMI with Packer, note the AMI ID and pass it to `var.ami_id`.

2. **Initialize Terraform**:
   ```bash
   terraform init
   ```

3. **Validate Configuration**:
   ```bash
   terraform validate
   ```

4. **Plan Deployment**:
   ```bash
   terraform plan -var "ami_id=<packer-ami-id>" -var "key_name=<your-key-name>" -var "private_key_path=~/.ssh/<your-key.pem>"
   ```

5. **Apply Configuration**:
   ```bash
   terraform apply -var "ami_id=<packer-ami-id>" -var "key_name=<your-key-name>" -var "private_key_path=~/.ssh/<your-key.pem>"
   ```

---

### Result:
- A **free-tier eligible EC2 instance** will be deployed using your Packer-built AMI.
- Streamlit will run and be accessible via the instance's public IP or DNS on port 80.
- Security groups ensure SSH and HTTP traffic is allowed.
