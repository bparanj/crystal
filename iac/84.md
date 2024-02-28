Changing the default SSH port from the standard port 22 to another port is a common security measure to reduce the exposure to automated attacks. Once you change the SSH port on your server, you indeed need to specify the new port number when connecting from the terminal using an SSH command and your PEM file (private key).

Here's how you can change the SSH port:

1. **Edit the SSH configuration file** on your server, typically located at `/etc/ssh/sshd_config`.
   
   - Open the file with a text editor (you'll need sudo privileges): `sudo nano /etc/ssh/sshd_config`
   - Find the line that says `#Port 22`. Remove the `#` to uncomment it, and change `22` to your desired port number, for example, `Port 2222`.
   - Save and close the file.

2. **Restart the SSH service** to apply the changes: `sudo systemctl restart sshd`

3. **Update any firewall rules** to allow connections on the new port. For example, if you're using UFW (Uncomplicated Firewall) on Ubuntu, you would:
   - Allow the new port: `sudo ufw allow 2222/tcp`
   - If you're no longer using the default port, you might want to remove the rule allowing port 22: `sudo ufw delete allow 22/tcp`

### Connecting with the New Port

After changing the SSH port, you must specify the new port number when connecting via SSH. Use the `-p` option followed by the new port number. Assuming you've changed the port to `2222`, here's how you connect:

```bash
ssh -i /path/to/your/private_key.pem -p 2222 username@your_server_ip
```

Replace `/path/to/your/private_key.pem` with the actual path to your PEM file, `2222` with your new SSH port, `username` with your actual username on the server, and `your_server_ip` with the IP address of your server.

### Important Considerations

- **Remember the New Port**: Ensure you remember the new port number, as you'll need it for all future SSH connections.
- **Security Implications**: Changing the default SSH port is a security measure to avoid unsophisticated attacks but should be part of a broader security strategy, including the use of SSH keys, strong passwords, and regular system updates.
- **Connectivity Issues**: Ensure the new port is not blocked by any network firewalls or ISP restrictions that might prevent SSH access.
- **Update Configuration Management Tools**: If you're using configuration management tools or scripts that rely on SSH, remember to update them with the new port number.

Changing the SSH port can help reduce the volume of malicious login attempts, but always consider additional security measures for comprehensive protection.

## Playbook

To create an Ansible playbook that changes the SSH port and is intended to be run by Packer during the image building process, you need to follow a few steps. This playbook will update the SSH configuration to listen on a new port and ensure the firewall allows traffic on that port.

Let's say you want to change the SSH port to `2222`. Here's how the playbook might look:

### Ansible Playbook: `change-ssh-port.yml`

```yaml
---
- name: Update SSH port
  hosts: all
  become: true

  vars:
    new_ssh_port: 2222

  tasks:
    - name: Update SSH configuration to use a new port
      ansible.builtin.lineinfile:
        path: /etc/ssh/sshd_config
        regexp: '^#?Port '
        line: "Port {{ new_ssh_port }}"
        state: present
      notify: restart sshd

    - name: Allow new SSH port in UFW
      ansible.builtin.ufw:
        rule: allow
        port: "{{ new_ssh_port }}"
        proto: tcp

    - name: Reload UFW
      ansible.builtin.systemd:
        name: ufw
        state: reloaded

  handlers:
    - name: restart sshd
      ansible.builtin.systemd:
        name: ssh
        state: restarted
```

### Key Components:

- **Variable `new_ssh_port`**: This makes it easy to change the port by updating the variable.
- **Update SSH Configuration**: The `lineinfile` module searches for lines starting with "Port" and updates them to the desired port. It handles both commented and uncommented lines.
- **Allow New Port in UFW**: If you're using UFW as your firewall, this task updates the rules to allow traffic on the new SSH port.
- **Handler to Restart SSHD**: After changing the SSH configuration, the playbook uses a handler to restart the SSH service, applying the new port setting.

### Integration with Packer

To use this playbook with Packer, ensure you have an Ansible provisioner block in your Packer template. Here's an example of what that might look like in your Packer JSON template:

```json
{
  "provisioners": [
    {
      "type": "ansible",
      "playbook_file": "path/to/change-ssh-port.yml"
    }
  ]
}
```

Replace `"path/to/change-ssh-port.yml"` with the actual path to your playbook file.

### Running Packer

To build your image with Packer and apply the Ansible playbook, run Packer with your template:

```bash
packer build your-template.json
```

Replace `your-template.json` with the name of your Packer template file.

### Important Considerations

- **SSH Connection for Packer**: If you run this playbook as part of your Packer build, ensure that Packer can still connect via SSH after the port change. You might need to adjust your Packer template to connect using the new SSH port for subsequent provisioners.
- **Security**: Always consider the security implications of exposing SSH to the internet, even on a non-standard port. Use additional security measures such as IP whitelisting and SSH key authentication.
- **Firewall Management**: This playbook assumes you're using UFW. If you're using a different firewall tool, adjust the playbook accordingly.
