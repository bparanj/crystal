

postgresql-16 
postgresql-contrib-16

```
sudo sh -c 'echo "deb https://apt.PostgreSQL.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
```

sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

## Signing Keys Problem

```
 wget --quiet -O - https://www.PostgreSQL.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
Warning: apt-key is deprecated. Manage keyring files in trusted.gpg.d instead (see apt-key(8)).
OK
```

## Solution:

The warning indicates that `apt-key` is deprecated, and the recommended approach is now to manage repository signing keys by placing them directly in a directory (`/etc/apt/trusted.gpg.d/`) rather than using `apt-key add`. This change is part of an effort to improve security and manage keys more effectively. Here's how you can adapt to this new method when adding the PostgreSQL repository key, as per your example:

### Step 1: Download the Repository Signing Key

First, download the PostgreSQL signing key directly using `wget` or `curl`. It's a good practice to inspect keys or download them from a trusted source. Since you're downloading from the official PostgreSQL website, it's considered safe:

```bash
wget -qO- https://www.postgresql.org/media/keys/ACCC4CF8.asc > ACCC4CF8.asc
```

### Step 2: Add the Key to the Trusted Keyring Directory

Next, move the downloaded key to the `/etc/apt/trusted.gpg.d/` directory. This action requires superuser privileges. The `.asc` file is essentially a PGP public key in ASCII format. Rename the file with a `.gpg` extension to clarify its purpose and format:

```bash
sudo mv ACCC4CF8.asc /etc/apt/trusted.gpg.d/postgresql.gpg
```

This command moves and renames the key to `postgresql.gpg` in the directory where APT will automatically recognize and trust it when installing packages from the PostgreSQL repository.

### Step 3: Add the PostgreSQL Repository

If you haven't already added the PostgreSQL repository to your system, do so by creating a `.list` file under `/etc/apt/sources.list.d/`. This is generally recommended over adding entries directly to the `sources.list` file to keep your sources organized:

```bash
echo "deb http://apt.postgresql.org/pub/repos/apt/ $(lsb_release -cs)-pgdg main" | sudo tee /etc/apt/sources.list.d/pgdg.list
```

This command adds the official PostgreSQL repository for your Ubuntu distribution to APT's sources.

### Step 4: Update APT and Install PostgreSQL

Finally, update your package lists and install PostgreSQL:

```bash
sudo apt-get update
```

This sequence of commands respects the newer security practices by avoiding deprecated methods, ensuring that your system's package management configuration remains robust and secure.


## Key Rings Problem

```
sudo apt update
W: http://us-west-2.ec2.archive.ubuntu.com/ubuntu/dists/jammy/InRelease: The key(s) in the keyring /etc/apt/trusted.gpg.d/postgresql.gpg are ignored as the file has an unsupported filetype.
W: http://us-west-2.ec2.archive.ubuntu.com/ubuntu/dists/jammy-updates/InRelease: The key(s) in the keyring /etc/apt/trusted.gpg.d/postgresql.gpg are ignored as the file has an unsupported filetype.
W: http://us-west-2.ec2.archive.ubuntu.com/ubuntu/dists/jammy-backports/InRelease: The key(s) in the keyring /etc/apt/trusted.gpg.d/postgresql.gpg are ignored as the file has an unsupported filetype.
W: http://security.ubuntu.com/ubuntu/dists/jammy-security/InRelease: The key(s) in the keyring /etc/apt/trusted.gpg.d/postgresql.gpg are ignored as the file has an unsupported filetype.
W: http://apt.postgresql.org/pub/repos/apt/dists/jammy-pgdg/InRelease: The key(s) in the keyring /etc/apt/trusted.gpg.d/postgresql.gpg are ignored as the file has an unsupported filetype.
W: http://apt.postgresql.org/pub/repos/apt/dists/jammy-pgdg/InRelease: Key is stored in legacy trusted.gpg keyring (/etc/apt/trusted.gpg), see the DEPRECATION section in apt-key(8) for details.
```

## Solution

The warnings you're encountering suggest that the key file (`postgresql.gpg`) you placed in `/etc/apt/trusted.gpg.d/` is not in the correct format that `apt` expects for new-style keyrings. Specifically, the `apt` system expects the keyring files in this directory to be in binary GPG keyring format (`*.gpg`), but the file you have is likely still in ASCII armored format (which is what `.asc` files  are).

To resolve this issue, you need to convert the ASCII armored key (`ACCC4CF8.asc`) to a binary GPG keyring format before moving it to `/etc/apt/trusted.gpg.d/`. Here’s how you can do that:

### 1. Convert the ASCII Armored Key to GPG Keyring Format

First, convert the downloaded ASCII armored key to a binary GPG keyring format. You can use `gpg` to import the key into a keyring file you create in your current directory, and then export it in binary format:

```bash
# Import the ASCII armored key to a temporary keyring in the current directory
gpg --no-default-keyring --keyring ./temp-keyring.gpg --import ACCC4CF8.asc

# Export the key in binary format
gpg --no-default-keyring --keyring ./temp-keyring.gpg --export > postgresql.gpg
```

```
gpg --no-default-keyring --keyring ./temp-keyring.gpg --import ACCC4CF8.asc
gpg: keybox './temp-keyring.gpg' created
gpg: can't open 'ACCC4CF8.asc': No such file or directory
gpg: Total number processed: 0
```



### 2. Move the Binary Keyring to `/etc/apt/trusted.gpg.d/`

Now, move this binary keyring file to the `/etc/apt/trusted.gpg.d/` directory:

```bash
sudo mv postgresql.gpg /etc/apt/trusted.gpg.d/
```

This command replaces the previous ASCII armored file with the new binary keyring format that `apt` expects.

### 3. Clean Up (Optional)

If you created the temporary keyring (`temp-keyring.gpg`) in your current directory, you might want to remove it along with the original ASCII armored file if they are no longer needed:

```bash
rm ACCC4CF8.asc temp-keyring.gpg
```

### 4. Update APT and Install PostgreSQL

Finally, run `apt-get update` again to refresh your package sources. The warnings about the keyring file type should now be resolved:

```bash
sudo apt-get update
sudo apt-get install postgresql
```

This process converts the PostgreSQL repository signing key to the correct format and resolves the warnings about the key being ignored due to an unsupported file type.

## Using Packer

Let's use Packer to install Postgresql 16 and create a custom AMI based on Ubuntu 22.04. We will launch a EC2 instance using this image from the AWS console. We will SSH into the EC2 instance using a PEM file and manually test it. We will also document the packages required for the installation. Once we have a working database, we will install the pg gem, test and document the dependencies. The reason is copy/pasting from the internet without understanding why we are installing the packages can lead to bloated server that has unnecessary packages.

## Prerequisites

- You have an AWS account and your AWS credentials (Access Key ID and Secret Access Key) set up.
- You have Packer installed and configured for use with AWS.
- You have gone through Hello Packer example. (Revise: iac/docs/basics/hello-packer.md and create add it to hivegrid folder)
- You have created IAM user with the necessary permissions to create AWS resources (EC2 in this case).

## Packer Template

Below is a Packer HCL template that provisions an Ubuntu 22.04 AMI with PostgreSQL installed.

```hcl
packer {
  required_version = ">= 1.7.0"
  required_plugins {
    amazon = {
      version = ">= 1.0.0"
      source  = "github.com/hashicorp/amazon"
    }
  }
}

variable "region" {
  type    = string
  default = "us-east-1"
}

variable "source_ami_filter_name" {
  type    = string
  default = "ubuntu/images/*ubuntu-jammy-22.04-amd64-server-*"
}

variable "instance_type" {
  type    = string
  default = "t2.micro"
}

variable "ssh_username" {
  type    = string
  default = "ubuntu"
}

source "amazon-ebs" "ubuntu" {
  region     = var.region
  instance_type = var.instance_type
  source_ami_filter {
    filters = {
      name                = var.source_ami_filter_name
      root-device-type    = "ebs"
      virtualization-type = "hvm"
    }
    owners      = ["099720109477"]  # Ubuntu's owner ID
    most_recent = true
  }
  ssh_username = var.ssh_username
  ami_name     = "ubuntu-22.04-postgresql-{{timestamp}}"
}

build {
  sources = [
    "source.amazon-ebs.ubuntu"
  ]

  provisioner "shell" {
    inline = [
      "sudo apt-get update",
      "sudo apt-get install -y postgresql postgresql-contrib"
    ]
  }
}
```

### Explanation:

- **Required Plugins**: Specifies that the Amazon EBS builder plugin from HashiCorp is required.
- **Variables**: Declares variables for the AWS region, the base AMI name filter for Ubuntu 22.04 (Jammy Jellyfish), the instance type, and the SSH username.
- **Source**: Defines the Amazon EBS source configuration,  the region, instance type, source AMI filter (to automatically select the latest Ubuntu 22.04 AMI), and the SSH username.
- **Builds**: Specifies the build process, which includes the source and a shell provisioner.
  - **Shell Provisioner**: Contains inline shell commands to update the package index and install PostgreSQL and its contrib package.

### Steps:

1. Save the template to a file, e.g., `ubuntu-postgresql.pkr.hcl`.
2. Run `packer init .` in the directory containing your new template file to initialize Packer and install required plugins.
3. Run `packer build ubuntu-postgresql.pkr.hcl` to create the AMI.

## Action Items

- Modifying `postgresql.conf` and `pg_hba.conf` files
- Set up Rails deploy user 
- Secure the installation

The configuration files needs to allow the deploy database user to login using password and must have the privilege to create database. When you run rails db:create, the deploy user will be able to create the database. The database server will only be accessible from the EC2 instance where it is running and cannot be accessed over the Internet for security reasons.
