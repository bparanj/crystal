Provide instructions for  firewall rules are configured minimal Ubuntu 24.04 Server to allow outgoing connections from current machine, specifically for HTTPS (port 443 TCP) and OpenVPN (port 1194 UDP/TCP) to the hosts: login.expunge.xyz and api.expunge.xyz

Here are step-by-step instructions to configure firewall rules on an Ubuntu 24.04 server to allow outgoing connections specifically for HTTPS (port 443) and OpenVPN (port 1194) to the hosts `login.expunge.xyz` and `api.expunge.xyz` using **UFW (Uncomplicated Firewall)**.

### 1. **Install UFW (if not already installed)**
   - UFW is the default firewall tool for Ubuntu, but if it isn't installed, you can install it:
     ```bash
     sudo apt update
     sudo apt install ufw
     ```

### 2. **Enable UFW**
   - If UFW is not already enabled, you need to activate it:
     ```bash
     sudo ufw enable
     ```

### 3. **Allow HTTPS (Port 443) Outgoing**
   - Allow outgoing traffic on port 443 (TCP) for HTTPS connections to the specified hosts:
     ```bash
     sudo ufw allow out to login.expunge.xyz port 443 proto tcp
     sudo ufw allow out to api.expunge.xyz port 443 proto tcp
     ```

### 4. **Allow OpenVPN (Port 1194) Outgoing**
   - Allow outgoing traffic on port 1194 for OpenVPN. OpenVPN can operate on both TCP and UDP, so we will allow both protocols:
     ```bash
     sudo ufw allow out to login.expunge.xyz port 1194 proto udp
     sudo ufw allow out to login.expunge.xyz port 1194 proto tcp
     sudo ufw allow out to api.expunge.xyz port 1194 proto udp
     sudo ufw allow out to api.expunge.xyz port 1194 proto tcp
     ```

### 5. **Verify the Firewall Rules**
   - After configuring the firewall, check the status of UFW and verify that the rules are applied correctly:
     ```bash
     sudo ufw status
     ```
   You should see the firewall rules for outgoing connections on ports 443 and 1194 to the specified hosts.

### 6. **Restart UFW (if necessary)**
   - If you make any significant changes, it’s a good idea to reload UFW to apply them:
     ```bash
     sudo ufw reload
     ```

These steps ensure that your Ubuntu server allows outgoing traffic on port 443 for HTTPS and port 1194 for OpenVPN to the specified hosts (`login.expunge.xyz` and `api.expunge.xyz`).

To configure firewall rules on a minimal Ubuntu 24.04 Server to allow specific outgoing connections, we'll use the Uncomplicated Firewall (UFW), which is the default firewall configuration tool for Ubuntu. Here are the steps to set up the rules you've requested:

1. First, ensure UFW is installed and enabled:

```bash
sudo apt update
sudo apt install ufw
sudo ufw enable
```

2. Set the default policies:

```bash
sudo ufw default deny incoming
sudo ufw default allow outgoing
```

This allows all outgoing connections by default, but we'll add specific rules for clarity and potential future restrictions.

3. Allow outgoing HTTPS (port 443 TCP) connections to the specified hosts:

```bash
sudo ufw allow out to login.expunge.xyz port 443 proto tcp
sudo ufw allow out to api.expunge.xyz port 443 proto tcp
```

4. Allow outgoing OpenVPN (port 1194 UDP/TCP) connections to the specified hosts:

```bash
sudo ufw allow out to login.expunge.xyz port 1194 proto udp
sudo ufw allow out to login.expunge.xyz port 1194 proto tcp
sudo ufw allow out to api.expunge.xyz port 1194 proto udp
sudo ufw allow out to api.expunge.xyz port 1194 proto tcp
```

5. Reload the firewall to apply the new rules:

```bash
sudo ufw reload
```

6. Verify the rules have been added correctly:

```bash
sudo ufw status verbose
```

This will display all the active rules, including the ones we just added.

Additional notes:
- These rules assume that DNS resolution is working correctly for the specified domain names. If you're having issues, you might need to allow outgoing DNS traffic (port 53 UDP/TCP) as well.
- The rules allow both UDP and TCP for OpenVPN as it can use either protocol. If you know which specific protocol your OpenVPN setup uses, you can omit the unnecessary rule.
- Remember that these rules only affect outgoing connections. If you need to allow incoming connections (e.g., for SSH access), you'll need to add those rules separately.
- Always test the configuration thoroughly to ensure it doesn't disrupt any necessary services or connections.

If you need to make any changes or if you encounter any issues, you can always disable a rule using `sudo ufw delete [rule]` and then add a corrected version.

