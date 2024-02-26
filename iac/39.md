## Packer Template - First EC2 Image

```
brew tap hashicorp/tap
brew install hashicorp/tap/packer
```

```
packer version        
Packer v1.10.1
```

```
mkdir experiments
cd experiments
```

```hcl
packer {
  required_plugins {
    amazon = {
      source  = "github.com/hashicorp/amazon"
      version = "~> 1"
    }
  }
}

source "amazon-ebs" "ubuntu" {
  ami_name      = "packer-ubuntu-aws-{{timestamp}}"
  instance_type = "t2.micro"
  region        = "us-west-2"
  source_ami_filter {
    filters = {
      name                = "ubuntu/images/*ubuntu-jammy-22.04-amd64-server-*"
      root-device-type    = "ebs"
      virtualization-type = "hvm"
    }
    most_recent = true
    owners      = ["099720109477"]
  }
  ssh_username = "ubuntu"
}
build {
  sources = [
    "source.amazon-ebs.ubuntu"
  ]
}
```

Download Packer plugin:

```
packer init aws-ubuntu.pkr.hcl
```


```
packer fmt aws-ubuntu.pkr.hcl 
packer validate aws-ubuntu.pkr.hcl
```

```
export AWS_ACCESS_KEY_ID=<your access key>
export AWS_SECRET_ACCESS_KEY=<your secret key>
export AWS_DEFAULT_REGION=us-west-2
```

```
packer build aws-ubuntu.pkr.hcl
```

The Packer template written in HashiCorp Configuration Language (HCL). Packer is a tool used to automate the creation of any type of machine image. It embraces modern configuration management by allowing you to provide machine images as a part of your infrastructure.

Here's a breakdown of the code:

- The `packer` block at the top specifies the required plugins for this Packer configuration. In this case, it requires the `amazon` plugin from `github.com/hashicorp/amazon` with a version compatible with version 1.

- The `source "amazon-ebs" "ubuntu"` block defines a source configuration for an Amazon EBS-backed AMI. The `ami_name` is dynamically generated using a timestamp. The `instance_type` is set to `t2.micro`, and the `region` is set to `us-west-2`.

- The `source_ami_filter` block within the source configuration is used to select the base AMI for the instance. It filters for Ubuntu 22.04 (Jammy) AMIs with a root device type of `ebs` and a virtualization type of `hvm`. It selects the most recent AMI that matches these filters, owned by the account with the ID `099720109477`.

- The `ssh_username` is set to `ubuntu`, which is the default username for Ubuntu AMIs.

- The `build` block specifies what source the build should use. In this case, it's using the `amazon-ebs` source named `ubuntu` that was defined earlier.

In the context of the Packer template you provided, the `owners` field within the `source_ami_filter` block specifies the AWS account IDs that own the AMI that we're searching for. 

In this case, the `owners` field is set to `["099720109477"]`. This means that Packer will filter the AMIs and select the most recent one owned by the account with the ID `099720109477`.

This account ID is commonly used in Packer templates because it's the ID for the official Canonical account. Canonical is the company that produces and maintains Ubuntu, so this ID is used to filter for official Ubuntu AMIs.

Here's the relevant part of the code:

```hcl
source_ami_filter {
  filters = {
    name                = "ubuntu/images/*ubuntu-jammy-22.04-amd64-server-*"
    root-device-type    = "ebs"
    virtualization-type = "hvm"
  }
  most_recent = true
  owners      = ["099720109477"]  // Canonical's account ID
}
```

This configuration ensures that you're always building your custom AMI from the most recent official Ubuntu AMI.

# Lab: Write a Packer Template
This lab will walk you through updating a Packer HCL Template. It uses the amazon-ebs source to create a custom image in the us-west-2 region of AWS.

Duration: 30 minutes

- Task 1: Create a Source Block
- Task 2: Validate the Packer Template
- Task 3: Create a Builder Block
- Task 4: Build a new Image using Packer

## Creating a Packer Template

```bash
mkdir packer_templates
cd packer_templates
```

### Task 1: Create a Source Block
Source blocks define what kind of virtualization to use for the image, how to launch the image and how to connect to the image.  Sources can be used across multiple builds.  We will use the `amazon-ebs` source configuration to launch a `t2.micro` AMI in the `us-west-2` region.

### Step 1.1.1

Create a `aws-ubuntu.pkr.hcl` file with the following Packer `source` block and `required_plugins`.

```hcl
packer {
  required_plugins {
    amazon = {
      source  = "github.com/hashicorp/amazon"
      version = "~> 1"
    }
  }
}

source "amazon-ebs" "ubuntu" {
  ami_name      = "packer-ubuntu-aws-{{timestamp}}"
  instance_type = "t2.micro"
  region        = "us-west-2"
  source_ami_filter {
    filters = {
      name                = "ubuntu/images/*ubuntu-jammy-22.04-amd64-server-*"
      root-device-type    = "ebs"
      virtualization-type = "hvm"
    }
    most_recent = true
    owners      = ["099720109477"]
  }
  ssh_username = "ubuntu"
}
```

### Step 1.1.2
The `packer init` command is used to download Packer plugin binaries. This is the first command that should be executed when working with a new or existing template. This command is always safe to run multiple times.

```shell
packer init aws-ubuntu.pkr.hcl
```

### Task 2: Validate the Packer Template
Packer templates can be auto formatted and validated via the Packer command line.

### Step 2.1.1

Format and validate your configuration using the `packer fmt` and `packer validate` commands.

```shell
packer fmt aws-ubuntu.pkr.hcl 
packer validate aws-ubuntu.pkr.hcl
```

### Task 3: Create a Builder Block
Builders are responsible for creating machines and generating images from them for various platforms.  They are use in tandem with the source block within a template.

### Step 3.1.1
Add a builder block to `aws-ubuntu.pkr.hcl` referencing the source specified above.  The source can be referenced usin the HCL interpolation syntax.

```hcl
build {
  sources = [
    "source.amazon-ebs.ubuntu"
  ]
}
```

### Task 4: Build a new Image using Packer
The `packer build` command is used to initiate the image build process for a given Packer template. For this lab, please note that you will need credentials for your AWS account in order to properly execute a `packer build`. You can set your credentials using [environment variables](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html#linux), using [aws configure](https://docs.aws.amazon.com/cli/latest/reference/configure/) if you have the AWSCLI installed, or [embed the credentials](https://www.packer.io/docs/builders/amazon/ebsvolume#access-configuration) in the template.

> Example using environment variables on a Linux or macOS:

```shell
export AWS_ACCESS_KEY_ID=<your access key>
export AWS_SECRET_ACCESS_KEY=<your secret key>
export AWS_DEFAULT_REGION=us-west-2
```

> Example via Powershell:

```pwsh
PS C:\> $Env:AWS_ACCESS_KEY_ID="<your access key>"
PS C:\> $Env:AWS_SECRET_ACCESS_KEY="<your secret key>"
PS C:\> $Env:AWS_DEFAULT_REGION="us-west-2"
```

### Step 4.1.1
Run a `packer build` for the `aws-ubuntu.pkr.hcl` template.

```shell
packer build aws-ubuntu.pkr.hcl
```

Packer will print output similar to what is shown below.

```bash
amazon-ebs.ubuntu: output will be in this color.

==> amazon-ebs.ubuntu: Prevalidating any provided VPC information
==> amazon-ebs.ubuntu: Prevalidating AMI Name: packer-ubuntu-aws-1620827902
    amazon-ebs.ubuntu: Found Image ID: ami-0dd273d94ed0540c0
==> amazon-ebs.ubuntu: Creating temporary keypair: packer_609bdefe-f179-a11c-3bfd-6f4deda66c99
==> amazon-ebs.ubuntu: Creating temporary security group for this instance: packer_609bdf00-c182-00a1-e516-32aea832ff9e
==> amazon-ebs.ubuntu: Authorizing access to port 22 from [0.0.0.0/0] in the temporary security groups...
==> amazon-ebs.ubuntu: Launching a source AWS instance...
==> amazon-ebs.ubuntu: Adding tags to source instance
    amazon-ebs.ubuntu: Adding tag: "Name": "Packer Builder"
    amazon-ebs.ubuntu: Instance ID: i-0c9a0b1b896b8c95a
==> amazon-ebs.ubuntu: Waiting for instance (i-0c9a0b1b896b8c95a) to become ready...
==> amazon-ebs.ubuntu: Using ssh communicator to connect: 34.219.135.12
==> amazon-ebs.ubuntu: Waiting for SSH to become available...
==> amazon-ebs.ubuntu: Connected to SSH!
==> amazon-ebs.ubuntu: Stopping the source instance...
    amazon-ebs.ubuntu: Stopping instance
==> amazon-ebs.ubuntu: Waiting for the instance to stop...
==> amazon-ebs.ubuntu: Creating AMI packer-ubuntu-aws-1620827902 from instance i-0c9a0b1b896b8c95a
    amazon-ebs.ubuntu: AMI: ami-0561bdc79bbb8f5a0
==> amazon-ebs.ubuntu: Waiting for AMI to become ready...
==> amazon-ebs.ubuntu: Terminating the source AWS instance...
==> amazon-ebs.ubuntu: Cleaning up any extra volumes...
==> amazon-ebs.ubuntu: No volumes to clean up, skipping
==> amazon-ebs.ubuntu: Deleting temporary security group...
==> amazon-ebs.ubuntu: Deleting temporary keypair...
Build 'amazon-ebs.ubuntu' finished after 3 minutes 16 seconds.

==> Wait completed after 3 minutes 16 seconds

==> Builds finished. The artifacts of successful builds are:
--> amazon-ebs.ubuntu: AMIs were created:
us-west-2: ami-0561bdc79bbb8f5a0
```

**Note:** This lab assumes you have the default VPC available in your account. If you do not, you will need to add the [`vpc_id`](https://www.packer.io/docs/builders/amazon/ebs#vpc_id) and [`subnet_id`](https://www.packer.io/docs/builders/amazon/ebs#subnet_id). The subnet will need to have public access and a valid route to an Internet Gateway.

##### Resources
* Packer [Docs](https://www.packer.io/docs/index.html)
* Packer [CLI](https://www.packer.io/docs/commands/index.html)

