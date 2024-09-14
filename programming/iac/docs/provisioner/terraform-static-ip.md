Create a Terraform template to assign static IP for a EC2 image created by Packer

To use a single static IP (Elastic IP or EIP in AWS) across different Terraform runs, especially for experimentation, you can manually create the EIP in the AWS console and then reference it in your Terraform configurations using a data source. This approach allows you to keep the EIP constant across runs without Terraform trying to create or destroy it.

### Step 1: Create an Elastic IP in AWS

1. Go to the AWS Management Console.
2. Navigate to the EC2 dashboard.
3. In the "Network & Security" section, choose "Elastic IPs".
4. Click "Allocate new address" and follow the prompts to allocate a new EIP.
5. Note the Allocation ID or the EIP address once created.

### Step 2: Reference the Elastic IP in Terraform

Use the `aws_eip` data source to reference the existing EIP by its ID or IP address. You'll need the Allocation ID or the public IP you noted from the AWS console.

#### Using Allocation ID

If you have the Allocation ID (e.g., `eipalloc-1234567890abcdef0`), you can use it like this:

```hcl
data "aws_eip" "existing" {
  id = "eipalloc-1234567890abcdef0"
}

resource "aws_instance" "example" {
  ami           = "ami-123456"
  instance_type = "t2.micro"
  # other configurations...

  tags = {
    Name = "ExampleInstance"
  }
}

resource "aws_eip_association" "example" {
  instance_id   = aws_instance.example.id
  allocation_id = data.aws_eip.existing.id
}
```

#### Using Public IP

Alternatively, if you prefer to use the EIP's public IP:

```hcl
data "aws_eip" "existing" {
  public_ip = "1.2.3.4"
}

resource "aws_instance" "example" {
  ami           = "ami-123456"
  instance_type = "t2.micro"
  # other configurations...

  tags = {
    Name = "ExampleInstance"
  }
}

resource "aws_eip_association" "example" {
  instance_id   = aws_instance.example.id
  allocation_id = data.aws_eip.existing.id
}
```

### Step 3: Apply Your Terraform Configuration

Run `terraform apply` to apply your configuration. Terraform will use the existing EIP and associate it with the instance defined in your configuration.

### Important Considerations

- **Lifecycle Management**: Ensure that Terraform does not try to manage the lifecycle of the manually created EIP. Using it as a data source, as shown above, keeps Terraform from managing its lifecycle.
- **Clean Up**: Remember that manually created resources will not be cleaned up by Terraform. You'll need to manually release the EIP if it's no longer needed.
- **Billing**: AWS charges for EIPs that are allocated but not associated with a running instance. Ensure you associate it with an instance or release it when not in use to avoid unnecessary charges.

This approach allows you to maintain a consistent IP address across Terraform runs, which can be useful for development, testing, or when you have DNS records or whitelisting policies tied to specific IP addresses.

To achieve this task, you need to follow a two-step process: first, create an Amazon Machine Image (AMI) using Packer with your desired configuration, and second, use Terraform to deploy an EC2 instance using that AMI and assign it a static IP address, also known as an Elastic IP (EIP) in AWS terminology.

### Step 1: Create a Packer Template in HCL

Create a Packer template named `packer.pkr.hcl` for building your AMI. Here's a basic example using HCL:

```hcl
variable "aws_access_key" {
  type    = string
  default = "your-access-key"
}

variable "aws_secret_key" {
  type    = string
  default = "your-secret-key"
}

locals { timestamp = regex_replace(timestamp(), "[- TZ:]", "") }

source "amazon-ebs" "example" {
  access_key    = var.aws_access_key
  secret_key    = var.aws_secret_key
  region        = "us-east-1"
  source_ami_filter {
    filters = {
      virtualization-type = "hvm"
      name                = "amzn2-ami-hvm-*-x86_64-ebs"
      root-device-type    = "ebs"
    }
    owners      = ["137112412989"]
    most_recent = true
  }
  instance_type = "t2.micro"
  ssh_username  = "ec2-user"
  ami_name      = "packer-example-${local.timestamp}"
}

build {
  sources = [
    "source.amazon-ebs.example"
  ]
}
```

This Packer template defines a source configuration for an Amazon EBS-backed AMI, using Amazon Linux 2 as the base. It specifies the AWS credentials, region, and instance type, among other parameters. Note that you should replace `"your-access-key"` and `"your-secret-key"` with your actual AWS credentials or, preferably, use environment variables to avoid hardcoding sensitive information.

### Step 2: Use Terraform to Deploy an EC2 Instance and Assign a Static IP

Now, let's move on to deploying an EC2 instance with Terraform and assigning it a static IP address. The `main.tf` Terraform configuration remains the same as previously described:

```hcl
provider "aws" {
  region = "us-east-1"
}

resource "aws_eip" "example" {
  vpc = true
}

resource "aws_instance" "example" {
  ami           = "ami-123456" # Replace this with your actual AMI ID from Packer
  instance_type = "t2.micro"

  tags = {
    Name = "ExampleInstance"
  }
}

resource "aws_eip_association" "example" {
  instance_id   = aws_instance.example.id
  allocation_id = aws_eip.example.id
}
```

After creating your AMI with Packer, replace `"ami-123456"` with the actual AMI ID you receive. This Terraform configuration will create an EC2 instance from your custom AMI and associate an Elastic IP with it.

### Key Takeaways

- Using HCL for both Packer and Terraform configurations provides a consistent and readable way to define infrastructure as code.
- Packer's HCL format allows for more structured and modular template definitions.
- By separating the creation of the AMI and the deployment of infrastructure into two steps, you maintain flexibility and reusability in your infrastructure management.
- Always ensure your AWS credentials are managed securely, using environment variables or IAM roles where possible.

Here's a Terraform HCL template that demonstrates how to assign a static IP address to an EC2 instance, along with explanations. **Importantly, this assumes you have some pre-existing infrastructure setup by Packer.**

**Prerequisites**

- **Packer-created AMI:** You need an AMI produced by your Packer HCL template. This AMI will become the base image for your EC2 instance.
- **Existing VPC and Subnet:** Terraform needs a VPC and subnet within which to launch the EC2 instance.

**Terraform HCL Template**

```hcl
provider "aws" {
  region = "your-aws-region" # Replace with your actual region
}

# Data sources to fetch existing resources
data "aws_ami" "example_ami" {
  most_recent = true
  owners      = ["self"]  # Assumes Packer AMI is owned by your account
  filter {
    name   = "name"
    values = ["ami-name-from-packer*"]
  }
}

data "aws_vpc" "main" {
  default = true # Assuming you have a default VPC
}

data "aws_subnet" "example" {
  # Example: Select a subnet by name
  filter {
    name   = "tag:Name"
    values = ["your-subnet-name"]
  }
}

# Elastic IP (for the static IP)
resource "aws_eip" "static_ip" {
  vpc = true
}

# EC2 instance with static IP association
resource "aws_instance" "web_server" {
  ami           = data.aws_ami.example_ami.id
  instance_type = "t2.micro"
  subnet_id     = data.aws_subnet.example.id

  # Associate the Elastic IP
  network_interface {
    device_index = 0
    private_ips  = [aws_eip.static_ip.private_ip]
    associate_public_ip = true
  }

  # (Optional) User data for bootstrapping your instance
  user_data = <<-EOF
              #!/bin/bash
              # Your instance setup commands here
              EOF

  tags = {
    Name = "web-server-with-static-ip"
  }
}
```

**Explanation**

1. **Provider:** Configures Terraform to use the AWS provider.
2. **Data Sources:**
   - `aws_ami`: Fetches the latest AMI created by your Packer template.
   - `aws_vpc`: Fetches your default VPC.
   - `aws_subnet`: Fetches a subnet (you'll need to adjust the filter).
3. **Elastic IP:** Creates an Elastic IP address (this is your static public IP).
4. **EC2 Instance:**
   - Uses your Packer AMI's ID.
   - Launches into the selected subnet.
   - Associates the Elastic IP to its network interface.
   - Includes optional 'user_data' for instance setup.

**How to Use**

1.  **Replace placeholders:** Fill in "your-aws-region," subnet details, and adjust the AMI filter if needed.
2.  **Packer:** Ensure your Packer HCL template correctly builds and tags/names the AMI.
3.  **Terraform:** Run `terraform init` and `terraform apply`

**Important Notes**

- **Coordination:** Packer and Terraform should be aligned (AMI names, regions, etc.).
- **Alternatives:** For dynamic IPs that are still persistent across stops/starts, consider `aws_instance` with `associate_public_ip = true` without the Elastic IP.

Let me know if you'd like help with any of the following:

- **Customizing this template further for your specific setup**
- **Integrating this Terraform snippet into a larger workflow**
- **Troubleshooting issues when applying this configuration**

To achieve the workflow where a static IP is created for a customer, and then they configure their domain registrar to point to this IP, followed by Terraform configuring the domain to point to the IP, you'll need to split the task into discrete steps. This process involves careful coordination between resource provisioning and external actions (like updating DNS settings at a domain registrar) that Terraform can't directly manage. Here's a suggested approach:

### Step 1: Provision the Static IP

First, create the static IP (AWS Elastic IP) using Terraform and output its value so that the customer can use it to update their DNS settings at their domain registrar.

```hcl
resource "aws_eip" "customer_eip" {
  vpc = true
}

output "customer_eip_address" {
  value = aws_eip.customer_eip.public_ip
}
```

Run `terraform apply` to provision the Elastic IP and provide the customer with the output IP address.

### Step 2: Customer Updates DNS Settings

Inform the customer to update their DNS settings at their domain registrar, pointing their domain to the Elastic IP address provided by Terraform. This step is manual and outside the direct control of Terraform.

### Step 3: Wait for DNS Propagation

Once the customer has updated their DNS settings, you'll need to wait for these changes to propagate across the internet. This can take anywhere from a few minutes to 48 hours. You can use online tools to check the DNS propagation status.

### Step 4: Terraform Configuration for Domain Pointing

After DNS settings are confirmed to be pointing to the provided Elastic IP, you can proceed with the next Terraform run to configure any additional resources that depend on the domain pointing to the IP. This step might involve configuring services that require the domain to be resolvable to the IP, such as setting up a web server, SSL certificates, or other cloud resources.

If you're managing DNS records with AWS Route 53 and want to automate the process within the same Terraform configuration, you can use a `depends_on` argument or create a separate Terraform configuration that you run after DNS propagation. For Route 53, you would define a `aws_route53_record` resource that points your domain to the Elastic IP.

```hcl
resource "aws_route53_record" "example" {
  zone_id = var.route53_zone_id
  name    = "example.com"
  type    = "A"
  ttl     = "300"
  records = [aws_eip.customer_eip.public_ip]
}
```

Note that this assumes you are managing DNS with AWS Route 53. If the DNS is managed externally, Terraform can't update those records directly, and the customer would need to make those changes through their DNS provider's control panel.

### Final Thoughts

This process requires coordination between automated Terraform steps and manual actions by the customer. You can use Terraform outputs to inform the customer of the necessary information (like the EIP address) and then proceed with further Terraform configurations once the manual steps are completed and verified.
