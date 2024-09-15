## Test SSH Connection

Manual connection test:

```
ssh -i /Users/bparanj/work/nuxt/iac/prototype/experiments/javascript/rails.pem -p 2222 ubuntu@54.244.208.93
```

Using Ansible:

To test an SSH connection to a remote EC2 instance with an Ansible playbook, you can use the `ping` module, which is a simple way to check if your Ansible setup can communicate with the remote hosts defined in your inventory. This does not ly ping hosts, but attempts an SSH connection, and it’s a good way to ensure that your configuration is correct.

Before running this playbook, inventory file must be set up with the IP addresses or DNS names of EC2 instances and any necessary connection parameters like the remote user and private key path.

The host.ini file in the Rails app directory defines the IP and PEM file location:

```ini
[ec2_instances]
ec2_instance_1 ansible_host=54.244.208.93 ansible_user=ubuntu ansible_port=2222  ansible_ssh_private_key_file=/Users/bparanj/work/nuxt/iac/prototype/experiments/javascript/rails.pem

[ec2_instances:vars]
ansible_ssh_common_args='-o StrictHostKeyChecking=no'
```

Create ssh-connection.yml file in the Rails app directory and add the following content:

```yaml
---
- name: Test SSH Connection
  hosts: all
  gather_facts: no

  tasks:
    - name: Test SSH connection
      ansible.builtin.ping:
```

You can now run the playbook:

```bash
ansible-playbook -i host.ini ssh-connection.yml
```

This will attempt to establish an SSH connection to each host defined under `ec2_instances` in the inventory file and return a pong message on success, indicating the SSH connection is working properly.

## Using a Different Port

To specify a custom SSH port (like 2222) in your Ansible playbook or inventory file, you can add the `ansible_port` variable to your host definitions. This informs Ansible to use the specified port when attempting to establish SSH connections. Here's how you can modify the configuration:

### Inventory File Approach

If you're defining your hosts directly in an inventory file (e.g., `inventory.ini`), you can add the `ansible_port` variable like this:

```ini
[ec2_instances]
ec2_instance_1 ansible_host=your.ec2.ip.address ansible_user=ec2-user ansible_ssh_private_key_file=/path/to/your/private_key.pem ansible_port=2222

[ec2_instances:vars]
ansible_ssh_common_args='-o StrictHostKeyChecking=no'
```

### Playbook Approach

Alternatively, if you prefer to keep things organized within your playbook, you could define your hosts and variables there, though it's more common to handle host-specific configurations in the inventory file. If you still prefer to do so in the playbook for simplicity in certain cases, here's how you might structure it:

```yaml
---
- name: Test SSH Connection on Custom Port
  hosts: all
  gather_facts: no
  vars:
    ansible_port: 2222

  tasks:
    - name: Test SSH connection
      ansible.builtin.ping:
```

However, note that setting the `ansible_port` in the playbook vars like this would apply to all hosts targeted by the playbook, which might not be what you want if your inventory includes hosts that use different SSH ports.

### Best Practice

It's generally best to specify connection details (like SSH ports) in your inventory file, as it allows for greater flexibility and scalability, keeping your playbooks focused on the tasks and roles rather than the specifics of your infrastructure setup.

Adjust your firewall or security group settings accordingly to allow incoming connections on the custom SSH port.

## Troubleshooting

TASK [Synchronize project files from local to remote temp directory] ********************\*\*********************\*\*\*********************\*\*********************
fatal: [54.244.208.93 -> localhost]: FAILED! => {"changed": false, "cmd": "/usr/bin/rsync --delay-updates -F --compress --delete-after --archive --rsh='/usr/bin/ssh -S none -o Port=2222 -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null' --out-format='<<CHANGED>>%i %n%L' /Users/bparanj/work/rails-docs/ ubuntu@54.244.208.93:/home/ubuntu/rails-docs-temp/", "msg": "Warning: Permanently added '[54.244.208.93]:2222' (ED25519) to the list of known hosts.\r\nubuntu@54.244.208.93: Permission denied (publickey).\r\nrsync: connection unexpectedly closed (0 bytes received so far) [sender]\nrsync error: unexplained error (code 255) at /AppleInternal/Library/BuildRoots/11aa8fb2-5f4b-11ee-bc7f-926038f30c31/Library/Caches/com.apple.xbs/Sources/rsync/rsync/io.c(453) [sender=2.6.9]\n", "rc": 255}

PLAY RECAP **********************************\*\*\*\***********************************\***********************************\*\*\*\***********************************
54.244.208.93 : ok=1 changed=0 unreachable=0 failed=1 skipped=0 rescued=0 ignored=0

```
$ eval `ssh-agent`
Agent pid 96683
```

```
$ ssh-add /Users/bparanj/work/nuxt/iac/prototype/experiments/javascript/rails.pem
Identity added: /Users/bparanj/work/nuxt/iac/prototype/experiments/javascript/rails.pem
(/Users/bparanj/work/nuxt/iac/prototype/experiments/javascript/rails.pem)
```

```
$ ansible-playbook -i inventory.ini deploy.yml --extra-vars "rails_master_key=501f054eecfdeab14e455aecd0b73e9e"
```
