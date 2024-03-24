## Creating EC2 Instance

```bash
mkdir roles 
cd roles
```

```bash
ansible-galaxy init rails_server
```

```bash
tree rails_server
```

```yaml
---
- name: create the host security group
  ec2_group:
    name: "{{ ec2_sg_name }}"
    description: security group for new host
    region: "{{ ec2_region }}"
    rules:
      - proto: tcp
        from_port: 22
        to_port: 22
        cidr_ip: 0.0.0.0/0
      - proto: tcp
        from_port: 8000
        to_port: 8000
        cidr_ip: 0.0.0.0/0
      - proto: tcp
        from_port: 443
        to_port: 443
        cidr_ip: 0.0.0.0/0
    rules_egress:
      - proto: all
        cidr_ip: 0.0.0.0/0
  register: basic_firewall

- name: launch the new ec2 instance
  ec2:
    group: "{{ ec2_sg_name }}"
    instance_type: "{{ ec2_instance_type }}"
    image: "{{ ec2_image }}"
    wait: true
    region: "{{ ec2_region }}"
    keypair: "{{ ec2_keypair }}"
    count: 1
  register: ec2

- name: wait for SSH to come up
  wait_for:
    host: '{{ item.public_ip }}'
    port: 22
    state: started
  with_items: '{{ ec2.instances }}'

- name: add tag to instance
  ec2_tag:
    resource: '{{ item.id }}'
    region: '{{ ec2_region }}'
    state: present
  with_items: '{{ ec2.instances }}'
  args:
    tags:
      Name: rails-server
```

vars/main.yml:

```
---
ec2_sg_name: "AnsibleSecurityGroup"
ec2_region: "us-east-1"
ec2_instance_type: "t2.micro"
ec2_image: "ami-0099823645f06b6a1"
ec2_keypair: "ansible-ec2-key"
```

Create server_deploy.yml:

```yml
---
- hosts: localhost
  connection: local
  gather_facts: false
user: root
roles:
  - splunk_server
```

Run the playbook:

```bash
ansible-playbook -i hosts server_deploy.yml
```

Verify the server is runnin in the AWS console.

Connect to the EC2 instance:

```bash
ssh -i rails-server.pem ec2-user@<public_ip_address>
```

Terminate the instance:

```bash
ansible localhost -m ec2 -a "instance_ids=i-123456 region=us-east-1 state=absent"
```
