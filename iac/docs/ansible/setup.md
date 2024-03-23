brew install ansible

Ansible Tower:

pip3 install --user ansible=2.16.4

Virtual Env

python3 -m venv .venv --prompt A 
$ source .venv/bin/activate
(A)

SSH access and root privileges on a Ubuntu server.

Validation

$ ansible-playbook --syntax-check webservers-tls.yml
$ ansible-lint webservers-tls.yml
$ yamllint webservers-tls.yml

Running the Playbook

$ ansible-playbook webservers-tls.yml

See the list of available plugins:

$ ansible-doc -t inventory -l                

See plug-in documentation and example:

ansible-doc -t inventory amazon.aws.aws_ec2

Amazon EC2

For Amazon EC2, install the requirements:
$ pip3 install boto3 botocore
Create a file inventory/aws_ec2.yml with, at the very least:
    plugin: aws_ec2

Playbook to print OS details.

Viewing all facts of a server:
ansible ubuntu -m setup

Creating Role Files and Directories with ansible-galaxy

    $ ansible-galaxy role init --init-path playbooks/roles web



YAMLlint
ansible-lint
ansible-later

Playbook to Register Key Pairs

Create the key:

$ ssh-keygen -t ed25519 -a 100 -C '' -f ~/.ssh/ec2-user

Upload the public key:

---
    - name: Register SSH keypair
      hosts: localhost
      gather_facts: false
      tasks:
        - name: Upload public key
          amazon.aws.ec2_key:
            name: ec2key
            key_material: "{{ item }}"
            state: present
            force: true
          no_log: true
          with_file:
            - ~/.ssh/ec2key.pub

Security Groups

- name: Configure SSH security group
  amazon.aws.ec2_group:
    name: my_security_group
    description: SSH and Web Access
    rules:
      - proto: tcp
        from_port: 22
        to_port: 22
        cidr_ip: '0.0.0.0/0'
      - proto: tcp
        from_port: 80
        to_port: 80
        cidr_ip: 0.0.0.0/0
      - proto: tcp
        from_port: 443
        to_port: 443
        cidr_ip: 0.0.0.0/0
    rules_egress:
      - proto: tcp
        from_port: 443
        to_port: 443
        cidr_ip: 0.0.0.0/0
      - proto: tcp
        from_port: 80
        to_port: 80
        cidr_ip: 0.0.0.0/0


Getting the Latest AMI

---
- name: Find latest Ubuntu image on Amazon EC2
  hosts: localhost
  gather_facts: false
  tasks:
    - name: Gather information on Ubuntu AMIs published by Canonical
      amazon.aws.ec2_ami_info:
        owners: 099720109477
        filters:
            name: "ubuntu/images/*ubuntu-jammy-22.04-amd64-server-*"
            root-device-type: "ebs"
            virtualization-type: "hvm"
                    state: "available"
      register: ec2_ami_info

    - name: Sort the list of AMIs by date for the latest image set_fact:
    latest_ami: |
    {{ ec2_ami_info.images | sort(attribute='creation_date') | last }}
        - name: Display the latest AMI ID
        debug:
            var: latest_ami.image_id

Create a New Instance and Add it to a Group

- name: Create an ubuntu instance on Amazon EC2
  hosts: localhost
  gather_facts: false
  tasks:
    - name: Configure and start EC2 instance
      amazon.aws.ec2_instance:
        name: 'web1'
        image_id: "{{ latest_ami.image_id }}"
        instance_type: "{{ instance_type }}"
        key_name: "{{ key_name }}"
        security_group: "{{ security_group }}"
        network:
          assign_public_ip: true
        tags: {type: web, env: production}
        volumes:
          - device_name: /dev/sda1
            ebs:
            volume_size: 16
            delete_on_termination: true
        wait: true
      register: ec2
    - name: Add the instances to the web and production groups
      add_host:
        hostname: "{{ item.public_dns_name }}"
        groupname:
          - web
          - production
      loop: "{{ ec2.instances }}"
    - name: Configure Web Server
      hosts: web:&production
      become: true
      gather_facts: true
      remote_user: ubuntu
      roles:
        - webserver
    - name: Wait for EC2 instance to be ready
        wait_for:
            host: "{{ item.public_dns_name }}"
            port: 22
            search_regex: OpenSSH
            delay: 60
        loop: "{{ ec2.instances }}"
        register: wait

Entire Playbook:

```yaml
---
- name: Provision Ubuntu Web Server on Amazon EC2
  hosts: localhost
  gather_facts: false
  vars:
    instance_type: t2.micro
    key_name: ec2key
    aws_region: "{{ lookup('env', 'AWS_REGION') }}"
    security_group: my_security_group
  tasks:
    - name: Upload public key ec2key.pub
      amazon.aws.ec2_key:
        name: "{{ key_name }}"
        key_material: "{{ lookup('file', '~/.ssh/ec2key.pub') }}"
        state: present
        force: true
      no_log: true

    - name: Configure my_security_group
      amazon.aws.ec2_group:
        name: "{{ security_group }}"
        region: "{{ aws_region }}"
        description: SSH and Web Access
        rules:
          - proto: tcp
            from_port: 22
            to_port: 22
            cidr_ip: '0.0.0.0/0'
          - proto: tcp
            from_port: 80
            to_port: 80
            cidr_ip: 0.0.0.0/0
          - proto: tcp
            from_port: 443
            to_port: 443
            cidr_ip: 0.0.0.0/0
        rules_egress:
          - proto: tcp
            from_port: 443
            to_port: 443
            cidr_ip: 0.0.0.0/0
          - proto: tcp
            from_port: 80
            to_port: 80
            cidr_ip: 0.0.0.0/0

    - name: Gather information on Ubuntu AMIs published by Canonical
      amazon.aws.ec2_ami_info:
        region: "{{ aws_region }}"
        owners: 099720109477
        filters:
          name: "ubuntu/images/hvm-ssd/ubuntu-focal-20.04-*"
          architecture: "x86_64"
          root-device-type: "ebs"
          virtualization-type: "hvm"
          state: "available"
      register: ec2_ami_info

    - name: Sort the list of AMIs by date for the latest image
      set_fact:
        latest_ami: "{{ ec2_ami_info.images | sort(attribute='creation_date') | last }}"

    - name: Configure and start EC2 instance
      amazon.aws.ec2_instance:
        region: "{{ aws_region }}"
        name: 'web1'
        image_id: "{{ latest_ami.image_id }}"
        instance_type: "{{ instance_type }}"
        key_name: "{{ key_name }}"
        security_group: "{{ security_group }}"
        network:
          assign_public_ip: true
        tags:
          type: web
          env: production
        volumes:
          - device_name: /dev/sda1
            ebs:
              volume_size: 16
              delete_on_termination: true
        wait: true
      register: ec2

    - name: Wait for EC2 instance to be ready
      wait_for:
        host: "{{ item.public_dns_name }}"
        port: 22
        search_regex: OpenSSH
        delay: 30
      loop: "{{ ec2.instances }}"
      register: wait

    - name: Add the instances to the web and production groups
      add_host:
        hostname: "{{ item.public_dns_name }}"
        groupname:
          - web
          - production
      loop: "{{ ec2.instances }}"

- name: Configure Web Server
  hosts: web:&production
  become: true
  gather_facts: true
  remote_user: ubuntu
  roles:
    - ssh
    - webserver
```

Creating a VPC

```yaml
---
- name: Create a Virtual Private Cloud (VPC)
  hosts: localhost
  gather_facts: false
  vars:
    aws_region: "{{ lookup('env', 'AWS_REGION') }}"
  tasks:
    - name: Create a vpc
      amazon.aws.ec2_vpc_net:
        region: "{{ aws_region }}"
        name: "Book example"
        cidr_block: 10.0.0.0/16
        tags:
          env: production
      register: result

    - name: Set vpc_id as fact
      set_fact:
        vpc_id: "{{ result.vpc.id }}"

    - name: Add gateway
      amazon.aws.ec2_vpc_igw:
        region: "{{ aws_region }}"
        vpc_id: "{{ vpc_id }}"

- name: Create web subnet
  amazon.aws.ec2_vpc_subnet:
    region: "{{ aws_region }}"
    vpc_id: "{{ vpc_id }}"
    cidr: 10.0.0.0/24
    tags:
      env: production
      tier: web

- name: Create db subnet
  amazon.aws.ec2_vpc_subnet:
    region: "{{ aws_region }}"
    vpc_id: "{{ vpc_id }}"
    cidr: 10.0.1.0/24
    tags:
      env: production
      tier: db

- name: Set routes
  amazon.aws.ec2_vpc_route_table:
    region: "{{ aws_region }}"
    vpc_id: "{{ vpc_id }}"
    tags:
      purpose: permit-outbound
    subnets:
      - 10.0.0.0/24
      - 10.0.1.0/24
    routes:
      - dest: 0.0.0.0/0
        gateway_id: igw
```

Create EC2 Security Groups

```yaml
---
- name: Create EC2 Security Groups
  hosts: localhost
  vars:
    aws_region: "{{ lookup('env', 'AWS_REGION') }}"
    database_port: 5432
    cidrs:
      web: 10.0.0.0/24
      db: 10.0.1.0/24
      ssh: 203.0.113.0/24
  tasks:
    - name: DB security group
      amazon.aws.ec2_group:
        name: db
        region: "{{ aws_region }}"
        description: allow database access for web servers
        vpc_id: "{{ vpc_id }}"
        rules:
          - proto: tcp
            from_port: "{{ database_port }}"
            to_port: "{{ database_port }}"
            cidr_ip: "{{ cidrs.web }}"

    - name: Web security group
      amazon.aws.ec2_group:
        name: web
        region: "{{ aws_region }}"
        description: allow http and https access to web servers
        vpc_id: "{{ vpc_id }}"
        rules:
          - proto: tcp
            from_port: 80
            to_port: 80
            cidr_ip: 0.0.0.0/0
          - proto: tcp
            from_port: 443
            to_port: 443
            cidr_ip: 0.0.0.0/0

    - name: SSH security group
      amazon.aws.ec2_group:
        name: ssh
        region: "{{ aws_region }}"
        description: allow ssh access
        vpc_id: "{{ vpc_id }}"
        rules:
          - proto: tcp
            from_port: 22
            to_port: 22
            cidr_ip: "{{ cidrs.ssh }}"

    - name: Outbound security group
      amazon.aws.ec2_group:
        name: outbound
        description: allow outbound connections to the internet
        region: "{{ aws_region }}"
        vpc_id: "{{ vpc_id }}"
        rules_egress:
          - proto: all
            cidr_ip: 0.0.0.0/0
```



