## Package Installation using Packer and Ansible

Create the Packer template:

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
    playbook_file = "${path.root}/playbooks/packages.yml"
    user          = "ubuntu"
    use_proxy     = false
    ansible_env_vars = [
      "ANSIBLE_HOST_KEY_CHECKING=False"
    ]
  }

  provisioner "ansible" {
    playbook_file = "${path.root}/playbooks/webserver.yml"
    user          = "ubuntu"
    // Ensure Ansible can use the dynamic SSH settings provided by Packer
    use_proxy = false
    ansible_env_vars = [
      "ANSIBLE_HOST_KEY_CHECKING=False"
    ]
  }

  post-processor "manifest" {}

}
```

Create the Ansible playbook packages.yml for installing packages in playbooks folder:

```yml
---
- name: Install required packages on Ubuntu 22.04
  hosts: all
  become: true
  tasks:
    - name: Update apt repository and system packages
      ansible.builtin.apt:
        update_cache: yes
        cache_valid_time: 3600 # Cache valid for 1 hour to avoid unnecessary updates

    - name: Install development tools and libraries
      ansible.builtin.apt:
        name:
          - autoconf
          - bison
          - build-essential
          - curl
          - git-core
          - libdb-dev
          - libffi-dev
          - libgdbm-dev
          - libgdbm6
          - libgmp-dev
          - libncurses5-dev
          - libreadline6-dev
          - libsqlite3-dev
          - libssl-dev
          - libyaml-dev
          - locales
          - patch
          - pkg-config
          - rustc
          - uuid-dev
          - zlib1g-dev
          - tzdata
        state: present

    - name: Ensure locale is generated
      ansible.builtin.locale_gen:
        name: en_US.UTF-8
        state: present

    - name: Update locale
      ansible.builtin.command: update-locale LANG=en_US.UTF-8
      when: ansible_facts['env']['LANG'] is not defined or ansible_facts['env']['LANG'] != 'en_US.UTF-8'
```

```
packer fmt .
packer validate .
packer build .
```

Create a .pem file from AWS console, SSH and verify the package installation manually.
