To modify the Ansible playbook for commands that require sudo access for the "ubuntu" user on the EC2 instance, you can use the `become` directive in your playbook. The `become` directive allows you to execute tasks with elevated privileges (sudo) on the remote server.

Here's how you can modify the playbook:

```yaml
- hosts: ec2_instances
  become: yes
  become_user: root
  tasks:
    - name: Execute a command with sudo access
      command: apt update
```

In this modified playbook:
- The `become: yes` line tells Ansible to use privilege escalation (sudo) for executing the tasks.
- The `become_user: root` line specifies that the tasks should be executed as the "root" user, which has sudo privileges.
- The `command: apt update` is an example command that requires sudo access to update the package lists on the EC2 instance.

By adding `become: yes` and `become_user: root`, Ansible will execute the tasks with sudo privileges using the "ubuntu" user on the EC2 instance.

Make sure that the "ubuntu" user has sudo access on the EC2 instance. If the "ubuntu" user is not part of the sudo group or doesn't have the necessary permissions, you may need to configure sudo access for the user on the server.

Your inventory file (`inventory.ini`) remains the same:

```
[ec2_instances]
your_ec2_instance_hostname_or_ip ansible_user=ubuntu ansible_ssh_private_key_file=/path/to/your/pemfile.pem
```

Run the Ansible playbook using the following command:

```
ansible-playbook -i inventory.ini playbook.yml
```

Ansible will use the "ubuntu" user to connect to the EC2 instance, and then use sudo privileges to execute the tasks as the "root" user.

Use `become` and `become_user` judiciously and only for tasks that require elevated privileges. It's a good practice to minimize the use of sudo and only grant the necessary permissions to users for security reasons.
