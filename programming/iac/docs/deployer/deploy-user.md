To become the `deploy` user when you are logged in as the `ubuntu` user on an EC2 instance, you can use the `su` (substitute user) or `sudo` command to switch users. Here's how to do it with both methods:

### Using `sudo`

The `sudo` command is used to run commands as another user,  the root user. However, you can specify any user with the `-u` option. This method is preferred when you have `sudo` privileges but not the password of the target user.

```bash
sudo -u deploy -i
```

The `-i` (simulate initial login) option will give you the environment variables and the shell of the `deploy` user. This is similar to what would happen if the `deploy` user logged in to the system directly.

### Using `su`

If you know the password of the `deploy` user, you can switch to it using `su`:

```bash
su - deploy
```

The `-` option provides an environment similar to what the user would expect had the user logged in directly.

### Note

- You may need to adjust permissions or group memberships to allow switching users without a password. This  involves adding the `ubuntu` user to a group that has `sudo` or `su` permissions for the `deploy` user without requiring a password. This setup requires editing the `/etc/sudoers` file through the `visudo` command for safety.
- For automated scripts or Ansible playbooks, it's common to use `sudo` for its flexibility and logging capabilities. To allow the `ubuntu` user to switch to the `deploy` user without a password, you might add a line like this to the `/etc/sudoers` file (using `visudo` to edit):
  ```sudoers
  ubuntu ALL=(deploy) NOPASSWD: ALL
  ```
  This line allows the `ubuntu` user to execute any command as the `deploy` user without being prompted for a password.

Giving users the ability to switch to other users without a password can introduce security risks if not managed carefully. Always restrict this capability to trusted users and for specific purposes.

## Deploy User SSH using PEM File

The deploy user is created by the deploy_user.yml playbook. The playbook used to deploy the Rails app must use the PEM file to login to the EC2 instance.

Yes, the user created by the provided Ansible playbook will be able to use the PEM file to log in to the EC2 instance, but with a slight modification to the playbook.

Here's the updated playbook that includes the necessary tasks to allow the "deploy" user to log in using the PEM file:

```yaml
---
- name: Create deploy user and add to sudo group
  hosts: all
  become: true

  vars:
    pem_file_path: "/path/to/your/pem/file.pem"

  tasks:
    - name: Ensure deploy user is present
      ansible.builtin.user:
        name: deploy
        state: present
        groups: sudo
        append: yes
        create_home: yes
        shell: /bin/bash

    - name: Ensure deploy user has passwordless sudo
      ansible.builtin.lineinfile:
        path: /etc/sudoers.d/deploy
        line: "deploy ALL=(ALL) NOPASSWD:ALL"
        create: yes
        validate: "visudo -cf %s"

    - name: Set file permissions for the sudoers file for deploy
      ansible.builtin.file:
        path: /etc/sudoers.d/deploy
        mode: "0440"

    - name: Create .ssh directory for deploy user
      ansible.builtin.file:
        path: /home/deploy/.ssh
        state: directory
        owner: deploy
        group: deploy
        mode: "0700"

    - name: Copy PEM file to deploy user's .ssh directory
      ansible.builtin.copy:
        src: "{{ pem_file_path }}"
        dest: /home/deploy/.ssh/id_rsa
        owner: deploy
        group: deploy
        mode: "0400"
```

The updated playbook includes two additional tasks:

1. Create .ssh directory for deploy user:

   - This task creates the `.ssh` directory in the home directory of the "deploy" user.
   - The directory is owned by the "deploy" user and has strict permissions (0700) to ensure security.

2. Copy PEM file to deploy user's .ssh directory:
   - This task copies the PEM file from the specified `pem_file_path` to the `.ssh` directory of the "deploy" user.
   - The PEM file is renamed to `id_rsa` and has strict permissions (0400) to ensure security.
   - The `pem_file_path` variable should be set to the path of your PEM file on the Ansible control node.

With these modifications, the "deploy" user will have the necessary SSH key (PEM file) in their `.ssh` directory, allowing them to log in to the EC2 instance using SSH.

To use the PEM file for SSH login, the "deploy" user can run the following command:

```
ssh -i /home/deploy/.ssh/id_rsa deploy@<ec2-instance-ip>
```

Make sure to replace `<ec2-instance-ip>` with the  IP address or hostname of your EC2 instance.

Also, ensure that the security group associated with the EC2 instance allows inbound SSH traffic (port 22) from the appropriate IP range or security group.

With these changes, the Ansible playbook will create the "deploy" user, grant them sudo permissions, and provide them with the necessary PEM file to log in to the EC2 instance using SSH.
