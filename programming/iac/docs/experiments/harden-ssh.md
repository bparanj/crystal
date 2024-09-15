Create Ansible playbook for:
 - SSH hardening - prevent password login, change the default default ssh port and prevent root login

To create an Ansible playbook for SSH hardening,  preventing password login, changing the default SSH port, and preventing root login, you can follow this template. This playbook makes changes to the SSH daemon configuration,  found in `/etc/ssh/sshd_config`.

### Ansible Playbook: SSH Hardening

```yaml
---
- name: Harden SSH Configuration
  hosts: all
  become: true
  vars:
    ssh_port: 2222 # New SSH port (change as needed)

  tasks:
    - name: Prevent password authentication
      ansible.builtin.lineinfile:
        path: /etc/ssh/sshd_config
        regexp: '^#?PasswordAuthentication'
        line: 'PasswordAuthentication no'
        state: present

    - name: Change default SSH port
      ansible.builtin.lineinfile:
        path: /etc/ssh/sshd_config
        regexp: '^#?Port'
        line: 'Port {{ ssh_port }}'
        state: present

    - name: Prevent root login via SSH
      ansible.builtin.lineinfile:
        path: /etc/ssh/sshd_config
        regexp: '^#?PermitRootLogin'
        line: 'PermitRootLogin no'
        state: present

    - name: Restart SSH service to apply changes
      ansible.builtin.service:
        name: sshd
        state: restarted
```

### Explanation

- **SSH Port**: This playbook uses a variable `ssh_port` to define the new SSH port. Change `2222` to your preferred port number.
- **Prevent Password Authentication**: This task updates the `sshd_config` file to disable password authentication, requiring SSH keys for login.
- **Change Default SSH Port**: Modifies the SSH port to the value specified in `ssh_port`. This can help reduce the volume of automated attacks.
- **Prevent Root Login**: Disables the ability for the root user to log in directly over SSH, a common security practice.
- **Restart SSH Service**: Applies the changes by restarting the SSH daemon. Note that if you're connected over SSH while running this playbook, changing the port or disabling password authentication could disconnect you.

### Usage

1. Save this playbook to a file (e.g., `ssh_hardening.yml`).
2. Run the playbook using the `ansible-playbook` command:

```bash
ansible-playbook ssh_hardening.yml
```

### Important Considerations

- **SSH Port**: Before changing the SSH port, ensure the new port is allowed through the firewall and is not being used by other services.
- **Remote Access**: If running this playbook remotely via SSH, be cautious with changes that could lock you out, such as changing the SSH port or disabling password authentication without setting up key-based authentication first.
- **Backup**: Always backup your configuration files before making automated changes.

This playbook provides a foundational approach to SSH hardening. Depending on your specific requirements, you may want to implement additional security measures.

## Revise Playbook

The error message you're encountering, "ERROR! The requested handler 'restart sshd' was not found in either the main handlers list nor in the listening handlers list," indicates a mismatch between the name specified in the `notify` directive of your tasks and the name of the  handler that is supposed to restart the SSH service.

In your playbook, tasks are notifying a handler named "restart sshd", but your handler is defined with the name "Restart SSH service to apply changes". The names in the `notify` directive and the  handler must match exactly.

### Solution

To resolve this issue, you need to make sure the name used in the `notify` section of your tasks matches exactly with the name defined in your handlers section.

Change the `notify` sections in your tasks to match the handler's name:

```yaml
notify: Restart SSH service to apply changes
```

So your updated tasks section will look like this:

```yaml
tasks:
  - name: Prevent root login via SSH
    ansible.builtin.lineinfile:
      path: /etc/ssh/sshd_config
      regexp: '^(#)?PermitRootLogin'
      line: 'PermitRootLogin no'
      state: present
    notify: Restart SSH service to apply changes

  - name: Disable password authentication
    ansible.builtin.lineinfile:
      path: /etc/ssh/sshd_config
      regexp: '^(#)?PasswordAuthentication'
      line: 'PasswordAuthentication no'
      state: present
    notify: Restart SSH service to apply changes

  - name: Change default SSH port
    ansible.builtin.lineinfile:
      path: /etc/ssh/sshd_config
      regexp: '^#?Port'
      line: 'Port {{ ssh_port }}'
      state: present
    notify: Restart SSH service to apply changes
```

And your handlers section is correct as it is:

```yaml
handlers:
  - name: Restart SSH service to apply changes
    ansible.builtin.service:
      name: ssh
      state: restarted
```

This correction ensures that when any of the tasks are executed and changes are made, they correctly notify the defined handler to restart the SSH service, applying the new configuration.

In an Ansible playbook, you might see multiple tasks using the `notify` directive to trigger the same handler for several reasons:

1. **Modular Task Management**: Each task in an Ansible playbook is designed to manage a specific piece of configuration or a system setting. For instance, one task might disable root login via SSH, another might change the SSH port, and another might disable password authentication. Each of these tasks modifies a different part of the `sshd_config` file.

2. **Efficiency and Idempotency**: Ansible handlers are idempotent, meaning they will only run once at the end of a play if notified, regardless of how many tasks notify them. This behavior ensures that even if multiple tasks modify settings that require a service restart (like SSHD in your case), the service will only be restarted once, after all changes are made. This approach is more efficient and minimizes the potential impact on the system or service availability.

3. **Clarity and Maintainability**: Defining tasks with specific, focused changes makes playbooks easier to read, understand, and maintain. When a task triggers a significant action (like restarting a critical service), using `notify` makes it clear that the change requires a specific response (in this case, restarting the SSH service to apply the new configuration).

4. **Conditional Notifications**: Sometimes, not all tasks will change a system's state. If a task makes no changes (because the system already meets the desired state), it won't notify the handler. This conditionality ensures that services are only restarted when necessary, based on the  changes made during the playbook run.

5. **Grouping Related Changes**: By having multiple tasks notify the same handler, you can group related configuration changes. This setup is useful when multiple independent changes all require the same subsequent action (like a service restart). It allows for logical grouping and efficient execution of post-configuration steps.

In summary, using multiple `notify` statements for the same handler in different tasks allows for modular, efficient, and clear playbook design, ensuring that necessary actions (like service restarts) are performed precisely and efficiently, reflecting the changes made during the playbook run.

## Verify Port Change

To verify that the SSH default port has been successfully changed by an Ansible playbook, you can use several methods, both directly on the server where SSH is running and remotely. Here are a few approaches:

### 1. Check `sshd_config` Directly on the Server

Log into the server and check the `sshd_config` file for the `Port` directive to see if it reflects the new port number:

```bash
sudo grep '^Port' /etc/ssh/sshd_config
```

This command should display the line from `sshd_config` that specifies the SSH port, showing the updated port if the playbook successfully changed it.

### 2. Check the SSH Service Status

You can also check the status of the SSH service to look for clues about the listening port:

```bash
sudo systemctl status ssh
```

Or for systems using `sshd` as the service name:

```bash
sudo systemctl status sshd
```

The output might not always show the port number directly, depending on your system's configuration and the SSH version.

### 3. Use the `netstat` or `ss` Command

These commands can show you which ports are currently being listened to by the SSH daemon:

Using `netstat` (you may need to install `net-tools` if you're using a minimal Linux distribution):

```bash
sudo netstat -tuln | grep ssh
```

Using `ss`:

```bash
sudo ss -tuln | grep ssh
```

Look for a line that shows the new SSH port number in the `LISTEN` state.

### 4. Attempt to Connect via SSH Locally

Try connecting to SSH locally using the new port to verify that it's listening:

```bash
ssh -p <NewPort> localhost
```

Replace `<NewPort>` with the new SSH port number. If the connection is successful (or at least attempts to authenticate), the port change has been applied.

### 5. Remote Port Scan (If Accessible Remotely)

If the server is accessible over a network or the internet, and security policies allow it, you can use a tool like `nmap` to scan for open ports:

```bash
nmap -p <NewPort> server_ip_address
```

Replace `<NewPort>` with the new port number and `server_ip_address` with the server's IP address. This will tell you if the specified port is open and presumably listening for SSH connections.

**Note**: Remember that changing the SSH port is a basic security measure and might require updating firewall rules or security group settings in cloud environments (like AWS EC2) to allow connections on the new port. Always ensure that the new port does not conflict with other services and is allowed through any firewalls or network security policies.

ssh -i "mybox.pem" -p 2222 ubuntu@ec2-54-244-76-136.us-west-2.compute.amazonaws.com

1. **AWS Management Console**: Open and log in.
2. **EC2 Dashboard**: Navigate to "EC2".
3. **Security Groups**: In the left navigation pane, click "Security Groups".
4. **Select Security Group**: Choose the security group attached to your EC2 instance.
5. **Inbound Rules**: Click "Edit inbound rules".
6. **Add Rule**: 
   - Type: SSH
   - Protocol: TCP
   - Port Range: 2222
   - Source: Custom (0.0.0.0/0 for global access, or specify IP for restricted access).
7. **Save Rules**: Click "Save rules".

If the port range is disabled and defaults to 22 in the AWS Management Console when you select SSH as the type, you can manually specify the port range to allow connections on port 2222 by choosing "Custom TCP" instead of SSH. Here's how:

1. **Add Rule**: Click "Add rule".
2. **Type**: Select "Custom TCP".
3. **Protocol**: Automatically set to TCP.
4. **Port Range**: Enter `2222`.
5. **Source**: Choose "Anywhere" for global access (0.0.0.0/0, ::/0) or specify a specific IP address/range for restricted access.
6. **Save Rules**: Click "Save rules" to apply the new configuration.
