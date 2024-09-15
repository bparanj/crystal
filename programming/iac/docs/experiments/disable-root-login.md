Disabling root login and password-based SSH authentication are common security practices for Linux servers,  Ubuntu 22.04. When you disable these, you  rely on SSH key-based authentication for user accounts. A PEM file (Privacy Enhanced Mail) is often used in this context as it contains a private key for SSH key-based authentication.

### SSH Key-Based Authentication

When you disable root login and password authentication, you can still log in using an SSH key pair (the PEM file you mentioned is part of this mechanism). The process involves:

1. **Generating an SSH Key Pair**: If you haven't already, generate an SSH key pair on your local machine. The private key (`.pem` or `.id_rsa` file) stays on your local machine, while the public key (`.pub` file) gets uploaded to the server.

2. **Uploading the Public Key**: Place the public key in the `~/.ssh/authorized_keys` file of the user account you intend to use on the Ubuntu server.

3. **Configuring SSH**: Ensure your SSH configuration (`/etc/ssh/sshd_config`) on the Ubuntu server is set to allow key-based authentication and disallow password authentication and root login. Relevant settings include:

   ```
   PasswordAuthentication no
   PermitRootLogin no
   ```

4. **Logging In**: Use the private key to log in to the server with a command like:

   ```bash
   ssh -i /path/to/private_key.pem username@server_ip
   ```

   Replace `/path/to/private_key.pem` with the path to your PEM file, `username` with your user account on the server, and `server_ip` with the IP address of your Ubuntu server.

### Important Considerations

- **User Account**: Before disabling root login, ensure you have created another user account with `sudo` privileges. This account will be used for all administrative tasks on the server.

- **SSH Configuration**: Carefully edit the SSH configuration (`/etc/ssh/sshd_config`) and restart the SSH service (`sudo systemctl restart sshd`). Incorrect configuration could lock you out of the server.

- **PEM File Permissions**: Your private key (PEM file) must be kept secure. Set its permissions to be readable only by you:

  ```bash
  chmod 400 /path/to/private_key.pem
  ```

- **Backup Access**: Always have a backup access method in place before making significant changes to the SSH configuration. For cloud instances, this could be through the cloud provider's console or recovery mode options.

By following these steps, you ensure secure access to your Ubuntu 22.04 server using SSH key-based authentication, while disabling less secure methods like password authentication and direct root login.

To configure an Ubuntu 22.04 server to disable root login and password authentication while still allowing SSH access using a PEM file (SSH key-based authentication), you can use an Ansible playbook. This setup enhances server security by disabling less secure authentication methods.

Below is an example playbook that accomplishes this. It assumes you have already copied the public SSH key to the server for a non-root user, which you will use for SSH access.

### Example Ansible Playbook

```yaml
---
- name: Secure SSH Configuration
  hosts: all
  become: true
  tasks:
    - name: Disable root SSH login
      ansible.builtin.lineinfile:
        path: /etc/ssh/sshd_config
        regexp: '^PermitRootLogin'
        line: 'PermitRootLogin no'
        state: present
      notify: restart sshd

    - name: Disable password authentication
      ansible.builtin.lineinfile:
        path: /etc/ssh/sshd_config
        regexp: '^PasswordAuthentication'
        line: 'PasswordAuthentication no'
        state: present
      notify: restart sshd

    - name: Ensure SSH directory exists for non-root user
      ansible.builtin.file:
        path: "/home/{{ ansible_user }}/ssh"
        state: directory
        owner: "{{ ansible_user }}"
        group: "{{ ansible_user }}"
        mode: '0700'

    - name: Add authorized key for non-root user
      ansible.builtin.authorized_key:
        user: "{{ ansible_user }}"
        state: present
        key: "{{ lookup('file', '/path/to/your/public_key.pub') }}"
      when: ansible_user != 'root'

  handlers:
    - name: restart sshd
      ansible.builtin.service:
        name: ssh
        state: restarted
```

### Playbook Breakdown

- **Disable root SSH login**: This task updates `/etc/ssh/sshd_config` to set `PermitRootLogin` to `no`, disabling root login over SSH.
- **Disable password authentication**: Similarly, it sets `PasswordAuthentication` to `no` to require SSH key-based authentication.
- **Ensure SSH directory exists**: Creates the `.ssh` directory for the specified non-root user if it doesn’t already exist, ensuring the correct permissions.
- **Add authorized key**: Adds a specified public SSH key to the non-root user's authorized keys, allowing key-based SSH login. Replace `/path/to/your/public_key.pub` with the  path to your public SSH key file.
- **Handlers - restart sshd**: This handler restarts the SSH service to apply the configuration changes.

### Important Notes

- **SSH Access**: Before running this playbook, ensure that you have SSH access to the server using the non-root user and that your public SSH key is correctly installed. This is critical because, after applying these changes, password-based and root logins will be disabled.
- **Ansible User Variable**: Replace `{{ ansible_user }}` with your specific non-root username if not set as a variable elsewhere in your Ansible configurations.
- **Public Key Path**: Change `/path/to/your/public_key.pub` to the  path of your public SSH key on the machine running Ansible.

### Running the Playbook

To run this playbook, save it to a file (e.g., `secure_ssh.yml`) and execute it with the `ansible-playbook` command, specifying your inventory:

```bash
ansible-playbook -i your_inventory_file secure_ssh.yml
```

Ensure that you test this configuration on a non-critical system first to verify that you maintain SSH access as expected. Adjustments may be necessary depending on your specific server setup and SSH configuration.

The playbook you've provided aims to secure SSH configuration by disabling root login and password authentication, ensuring an SSH directory exists for a non-root user, and adding an authorized key for that user. However, there's a slight mistake in the path for the SSH directory and the location of the public key file when running through Packer. Here's the corrected version:

### Corrected Playbook

```yaml
---
- name: Secure SSH Configuration
  hosts: all
  become: true
  vars:
    ssh_public_key: "{{ lookup('env','HOME') }}/path/to/your/public_key.pub" # Adjust the path as needed

  tasks:
    - name: Disable root SSH login
      ansible.builtin.lineinfile:
        path: /etc/ssh/sshd_config
        regexp: '^(#)?PermitRootLogin'
        line: 'PermitRootLogin no'
        state: present
      notify: restart sshd

    - name: Disable password authentication
      ansible.builtin.lineinfile:
        path: /etc/ssh/sshd_config
        regexp: '^(#)?PasswordAuthentication'
        line: 'PasswordAuthentication no'
        state: present
      notify: restart sshd

    - name: Ensure .ssh directory exists for non-root user
      ansible.builtin.file:
        path: "/home/{{ ansible_user }}/.ssh"
        state: directory
        owner: "{{ ansible_user }}"
        group: "{{ ansible_user }}"
        mode: '0700'

    - name: Add authorized key for non-root user
      ansible.builtin.authorized_key:
        user: "{{ ansible_user }}"
        state: present
        key: "{{ lookup('file', ssh_public_key) }}"
      when: ansible_user != 'root'

  handlers:
    - name: restart sshd
      ansible.builtin.service:
        name: ssh
        state: restarted
```

### Key Corrections and Improvements:

- **SSH Directory Path**: Changed from `/home/{{ ansible_user }}/ssh` to `/home/{{ ansible_user }}/.ssh`. The `.ssh` directory is the correct location for storing user SSH keys.
- **Dynamic Public Key Path**: Added a `vars` section to define `ssh_public_key` using Ansible's `lookup` plugin to fetch the `HOME` environment variable of the user running the playbook. This allows for a more dynamic and correct path setting. Adjust the path (`/path/to/your/public_key.pub`) to where your public key is ly located relative to the `HOME` directory of the user running the playbook.
- **Regular Expression Adjustment**: Updated the `regexp` for `PermitRootLogin` and `PasswordAuthentication` to account for commented-out lines (`^(#)?`). This ensures that the playbook correctly updates these settings whether they are initially commented out or not.

### Running the Playbook with Packer

When running this playbook through Packer, ensure that:

- The path to the public key is accessible from the environment where Packer is executing the playbook.
- The `ansible_user` variable is correctly set to the username you intend to use for SSH connections, and it's not 'root'.
- If `ansible_user` is dynamically defined or relies on Packer's build environment, ensure it's passed correctly to Ansible.

This corrected playbook improves the security of SSH access by enforcing key-based authentication and restricting root access, tailored for execution in a Packer build environment.

To modify the playbook for creating a base image that's common to all customers, it's important to remove user-specific tasks and ensure that the configuration is universally applicable, without tying the setup to any specific user's details. Since adding an authorized key for a non-root user might be considered user-specific, we'll remove that part. The focus will be on securing the SSH configuration in a way that's common for all users, which includes disabling root login and password authentication.

Here's the revised playbook:

```yaml
---
- name: Secure SSH Configuration for Base Image
  hosts: all
  become: true

  tasks:
    - name: Disable root SSH login
      ansible.builtin.lineinfile:
        path: /etc/ssh/sshd_config
        regexp: '^(#)?PermitRootLogin'
        line: 'PermitRootLogin no'
        state: present
      notify: restart sshd

    - name: Disable password authentication
      ansible.builtin.lineinfile:
        path: /etc/ssh/sshd_config
        regexp: '^(#)?PasswordAuthentication'
        line: 'PasswordAuthentication no'
        state: present
      notify: restart sshd

  handlers:
    - name: restart sshd
      ansible.builtin.service:
        name: ssh
        state: restarted
```

### Key Points:

- **Universal SSH Security**: The playbook focuses on securing SSH by disabling root login and password authentication, which are considered best practices for all users.
- **Removed User-specific Tasks**: The task for adding an authorized key for a specific user has been removed. In a base image intended for multiple customers, it's better to leave user-specific configurations, such as SSH keys, to be added during or after instance creation based on the specific customer's requirements.
- **Handlers for Restarting SSH**: After making changes to `sshd_config`, the SSH service is restarted to apply the changes. This is crucial for ensuring that the security settings take effect immediately.

### Applying User-specific Configurations:

For configurations that are unique to each customer, such as adding specific SSH keys, consider the following approaches when deploying instances from the base image:

- **User Data Scripts**: Utilize cloud-init or other user data scripts that run on the first boot to configure instance-specific settings, like adding authorized keys.
- **Configuration Management Tools**: Use Ansible, Chef, Puppet, or similar tools to apply customer-specific configurations after the instance is deployed from the base image.
- **Customization at Runtime**: Provide documentation or scripts to customers for adding their SSH keys and making other personalized configurations post-deployment.

This approach ensures that the base image remains flexible and secure, suitable for a wide range of customers, while still allowing for easy customization to meet individual needs.
