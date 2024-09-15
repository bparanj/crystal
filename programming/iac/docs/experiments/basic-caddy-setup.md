
Create install_caddy.yml in playbooks directory:

```yml
---
- name: Install and Configure Caddy Server
  hosts: all
  become: true
  tasks:
    - name: Import Caddy's official signing key
      ansible.builtin.apt_key:
        url: https://dl.cloudsmith.io/public/caddy/stable/gpg.key
        state: present

    - name: Add Caddy's official repository
      ansible.builtin.apt_repository:
        repo: deb [trusted=yes] https://apt.fury.io/caddy/ /
        state: present
        update_cache: yes

    - name: Install Caddy
      ansible.builtin.apt:
        name: caddy
        state: latest

    - name: Create Caddyfile
      ansible.builtin.copy:
        dest: /etc/caddy/Caddyfile
        content: |
          :80 {
              respond "Caddy is running but not yet configured." 200
          }
        owner: root
        group: root
        mode: '0644'
      notify: restart caddy

  handlers:
    - name: restart caddy
      ansible.builtin.systemd:
        name: caddy
        state: restarted
        enabled: yes**
```

Modify the Packer template to include this playbook:

Build the AMI

Verify Caddy installation

If you can see the "Caddy is running but not yet configured." message when accessing your server locally via `curl http://localhost:80` but not when using the public IP address (e.g., `curl http://52.13.222.170:80`), it  points to a network or firewall configuration issue. Here are steps to troubleshoot and resolve this problem:

### 1. Check Security Group Settings

For an AWS EC2 instance, the most common reason for this issue is the Security Group configuration. Ensure that your instance's Security Group allows inbound traffic on port 80 (HTTP) from your IP address or from all sources (0.0.0.0/0) for testing purposes.

- Go to the AWS Management Console.
- Navigate to the EC2 Dashboard.
- Select "Security Groups" from the left-hand menu.
- Find the Security Group associated with your instance.
- Check the "Inbound rules" to ensure there is a rule allowing traffic on port 80 from the appropriate source.

### 2. Verify Network ACLs

Ensure that the Network Access Control List (NACL) for your VPC subnet allows inbound and outbound HTTP traffic on port 80. NACLs can block traffic entering or leaving a subnet, so confirming their configuration is important.

### 3. Check the Instance's Firewall

If you have a firewall configured within the Ubuntu instance (e.g., using `ufw` or another firewall management tool), ensure it allows traffic on port 80:

```bash
sudo ufw allow 80
sudo ufw reload
```

Or if you're not using `ufw`, ensure no other firewall rules are blocking the traffic.

### 4. Ensure Caddy is Listening on All Interfaces

By default, Caddy listens on all available interfaces. However, it's good to confirm that Caddy's configuration doesn't restrict it to localhost. The Caddyfile configuration you provided (`:80 { ... }`) is correctly set to listen on all interfaces for port 80, so this is likely not the issue but always worth verifying.

### 5. Verify Public IP Address

Ensure that the public IP address you're trying to access is indeed the current IP address of your instance. Public IP addresses can change for instances not associated with an Elastic IP (EIP) if they're stopped and restarted.

After checking these aspects, try accessing your instance via the public IP address again. If the problem persists, reviewing logs (`/var/log/cloud-init.log` for initialization issues, `journalctl -u caddy` for Caddy logs) and double-checking all network configurations can provide further insights.

If you can see the "Caddy is running but not yet configured." message when accessing your server locally via `curl http://localhost:80` but not when using the public IP address (e.g., `curl http://52.13.222.170:80`), it  points to a network or firewall configuration issue. Here are steps to troubleshoot and resolve this problem:

### 1. Check Security Group Settings

For an AWS EC2 instance, the most common reason for this issue is the Security Group configuration. Ensure that your instance's Security Group allows inbound traffic on port 80 (HTTP) from your IP address or from all sources (0.0.0.0/0) for testing purposes.

- Go to the AWS Management Console.
- Navigate to the EC2 Dashboard.
- Select "Security Groups" from the left-hand menu.
- Find the Security Group associated with your instance.
- Check the "Inbound rules" to ensure there is a rule allowing traffic on port 80 from the appropriate source.

### 2. Verify Network ACLs

Ensure that the Network Access Control List (NACL) for your VPC subnet allows inbound and outbound HTTP traffic on port 80. NACLs can block traffic entering or leaving a subnet, so confirming their configuration is important.

### 3. Check the Instance's Firewall

If you have a firewall configured within the Ubuntu instance (e.g., using `ufw` or another firewall management tool), ensure it allows traffic on port 80:

```bash
sudo ufw allow 80
sudo ufw reload
```

Or if you're not using `ufw`, ensure no other firewall rules are blocking the traffic.

### 4. Ensure Caddy is Listening on All Interfaces

By default, Caddy listens on all available interfaces. However, it's good to confirm that Caddy's configuration doesn't restrict it to localhost. The Caddyfile configuration you provided (`:80 { ... }`) is correctly set to listen on all interfaces for port 80, so this is likely not the issue but always worth verifying.

### 5. Verify Public IP Address

Ensure that the public IP address you're trying to access is indeed the current IP address of your instance. Public IP addresses can change for instances not associated with an Elastic IP (EIP) if they're stopped and restarted.

After checking these aspects, try accessing your instance via the public IP address again. If the problem persists, reviewing logs (`/var/log/cloud-init.log` for initialization issues, `journalctl -u caddy` for Caddy logs) and double-checking all network configurations can provide further insights.

sudo systemctl status caddy

Problem hitting the Caddy server. Inbound rule must be defined for the security group used by the instance.

Test the Caddy install:

```
curl http://<ip-address>:80
curl http://<ip-address>
Browse to: http://ec2-52-13-222-170.us-west-2.compute.amazonaws.com/
```

If your Security Group's inbound rule only allows traffic on port 22 (SSH) and does not include a rule for port 80 (HTTP), that's likely why you can't access your Caddy server using the public IP address. To resolve this, you need to add an inbound rule to allow HTTP traffic on port 80.

### Adding an Inbound Rule for HTTP Traffic

Follow these steps to add the necessary inbound rule to your Security Group:

1. **Navigate to Security Groups**:
   - Open the AWS Management Console.
   - Go to the EC2 Dashboard.
   - In the navigation pane, under **Network & Security**, click on **Security Groups**.

2. **Select Your Security Group**:
   - Find and select the Security Group associated with your instance.

3. **Edit Inbound Rules**:
   - With the Security Group selected, find the **Inbound rules** tab.
   - Click on the **Edit inbound rules** button.

4. **Add HTTP Rule**:
   - Click **Add rule**.
   - For **Type**, select **HTTP**. This will automatically set the **Port range** to 80.
   - For **Source**, you can select **Anywhere** to allow access from any IP address, or **My IP** to restrict access to your current IP address. The option **Anywhere** will fill in `0.0.0.0/0, ::/0`, indicating both IPv4 and IPv6 addresses are allowed.
   - Add a description if necessary.

5. **Save the Rule**:
   - Click **Save rules** to apply the changes.

After adding this inbound rule, you should be able to access your Caddy server using the instance's public IP address on port 80. This change allows web traffic to reach your server, making the "Caddy is running but not yet configured." message accessible from outside your AWS VPC.

### Important Security Note

While setting the source to **Anywhere** (`0.0.0.0/0, ::/0`) allows easy access for testing purposes, it's important to restrict access to only necessary IP addresses for production environments to enhance security.

This step is automated in [Using Terraform to Define Inbound Rule](./51.md)
