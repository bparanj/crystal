## Make Ansible Work with Packer

playbooks/playbook.yml:

```yml
---
- name: This playbook is used to install the packages
  hosts: all
  become: true
  tasks:
  - name: Update the apt repository
    apt:
      update_cache: yes
  - name: Install the packages
    apt:
      name: "curl"
      state: present
```

Create ansible.cfg in the project foler:

```
[ssh_connection]
scp_if_ssh = False  # Use this to disable scp explicitly, though it's not directly choosing sftp
pipelining = True   # This can improve performance but has specific requirements
```

Not sure if this is required to fix the SCP error message or not. Pending test by removing to see if it works

Create aws-ubuntu-pkr.hcl:

```hcl
packer {
  required_plugins {
    amazon = {
      source  = "github.com/hashicorp/amazon"
      version = "~> 1"
    }
    ansible = {
      version = "~> 1"
      source  = "github.com/hashicorp/ansible"
    }
  }
}

source "amazon-ebs" "ubuntu" {
  communicator  = "ssh"
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
  tags = {
    "Name"        = "UbuntuImage"
    "Environment" = "Testing"
    "OS_Version"  = "Ubuntu 22.04"
    "Release"     = "Latest"
    "Created-by"  = "Packer"
  }
}

build {
  sources = [
    "source.amazon-ebs.ubuntu"
  ]

  provisioner "ansible" {
    playbook_file = "${path.root}/playbooks/playbook.yml"
    user          = "ubuntu"
    // Ensure Ansible can use the dynamic SSH settings provided by Packer
    use_proxy = false
    ansible_env_vars = [
      "ANSIBLE_HOST_KEY_CHECKING=False"
    ]
  }
}
```

## Installing Webserver

Use the same Packer template, just point the playbook file to webserver.yml:

```hcl
    playbook_file = "${path.root}/playbooks/webserver.yml"
```

Create a playbooks directory, webserver.yml playbook:

```yml
---
- name: Install Nginx on Ubuntu
  hosts: all
  become: true
  tasks:
    - name: Update apt cache
      apt:
        update_cache: yes

    - name: Install Nginx
      apt:
        name: nginx
        state: present

    - name: Ensure Nginx is running
      service:
        name: nginx
        state: started
        enabled: yes
```
