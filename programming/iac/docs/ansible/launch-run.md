To create a single Ansible playbook that launches an EC2 instance and then runs further tasks against that newly launched instance, you can use a combination of the `amazon.aws.ec2_instance` module to launch the instance, the `add_host` module to dynamically add the new instance to an in-memory inventory, and then perform operations on that instance using subsequent tasks. Here’s an outline of such a playbook:

```yaml
---
- name: Launch and Configure EC2 Instance
  hosts: localhost
  gather_facts: false
  vars:
    instance_type: t2.micro
    image_id: ami-123456 # Replace with the  AMI ID for Ubuntu 22.04
    region: us-east-1
    keypair: my-keypair # Replace with your key pair name
    security_group: my-security-group # Replace with your security group name
    subnet_id: subnet-123456 # Replace with your subnet ID

  tasks:
    - name: Launch a new EC2 instance
      amazon.aws.ec2_instance:
        key_name: "{{ keypair }}"
        image_id: "{{ image_id }}"
        instance_type: "{{ instance_type }}"
        security_group: "{{ security_group }}"
        network:
          subnet_id: "{{ subnet_id }}"
        tags:
          Name: "MyInstance"
        region: "{{ region }}"
        wait: true
        assign_public_ip: true
      register: ec2_instance

    - name: Add new instance to host group
      add_host:
        name: "{{ ec2_instance.instance.public_ip_address }}"
        groups: launched
        ansible_ssh_private_key_file: /path/to/private/key.pem # Replace with the path to your private key
        ansible_user: ubuntu # or 'ec2-user', 'admin', depending on the AMI

- name: Configure Newly Launched Instance
  hosts: launched
  gather_facts: false
  become: true
  tasks:
    - name: Example task - Install nginx
      ansible.builtin.apt:
        name: nginx
        state: present
```

### Key Points:

- **Launch a new EC2 instance**: This task launches the instance using parameters you specify. Adjust `image_id`, `instance_type`, `keypair`, `security_group`, and `subnet_id` according to your requirements.
- **Add new instance to host group**: After the instance is launched, the `add_host` module adds the new instance to an in-memory group named `launched`. The `ansible_ssh_private_key_file` and `ansible_user` need to match the credentials for the AMI you're using.
- **Configure Newly Launched Instance**: In the second play, it targets the `launched` group. It includes an example task to install nginx on the new instance. Replace this task with whatever configuration steps you need.

Ensure that:
- The AWS credentials are correctly set up for Ansible to use.
- The specified AMI ID (`image_id`), key pair name (`keypair`), security group name (`security_group`), and subnet ID (`subnet_id`) are correct for your AWS environment.
- The path to the SSH private key file (`ansible_ssh_private_key_file`) is correct and points to the key associated with the `keypair`.

This playbook combines launching an EC2 instance and configuring it within a single Ansible playbook run, demonstrating a basic but powerful infrastructure as code (IaC) practice.
