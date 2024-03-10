## Caddy SSL Setup

For the scenario where you need to modify the Caddy configuration after the domain is mapped and DNS has propagated, consider the following approach:

1. **Post-Provisioning Configuration Script**:

   - After the EC2 instance is provisioned and the domain DNS settings are confirmed to be propagated, you can run a post-provisioning script that updates the Caddy configuration with the domain-specific settings.
   - This script can be executed manually, or it could be automated as part of a CI/CD pipeline, depending on your workflow.

2. **Example Script to Update Caddy Configuration**:

   - Suppose you need to configure `yourdomain.com` to reverse proxy to a Rack app running on `localhost:9292`. You could create an Ansible playbook, a bash script, or use another automation tool to perform the following steps:
     1. SSH into the EC2 instance.
     2. Update the Caddyfile with the domain-specific configuration.
     3. Reload or restart Caddy to apply the changes.

3. **Ansible Playbook Example**:
   Here's an example of an Ansible task that updates the Caddyfile and restarts Caddy. This playbook assumes you have SSH access and the necessary permissions on the target server.

   ```yaml
   - hosts: your_ec2_instance
     become: yes
     tasks:
       - name: Update Caddyfile
         copy:
           dest: /etc/caddy/Caddyfile
           content: |
             yourdomain.com {
                 reverse_proxy localhost:9292
             }
           owner: root
           group: root
           mode: "0644"

       - name: Reload Caddy to apply changes
         command: systemctl reload caddy
   ```

   - Before running the playbook, replace `your_ec2_instance` with your actual EC2 instance's inventory or IP address, and `yourdomain.com` with your actual domain name.

4. **Execution**:

   - After preparing the Ansible playbook (or your chosen script), execute it once the domain mapping is confirmed to work. This will update the Caddy configuration to serve your domain and proxy requests to the Rack app.

5. **Automation and Integration**:
   - Integrate this step into your customer signup or domain setup workflow. Depending on how automated you want the process to be, you could trigger this script automatically after a webhook notification of domain setup completion, or run it manually as needed.

By following this approach, you can dynamically update the Caddy configuration to serve different domains as they are mapped to your service, without needing to pre-configure Caddy for specific domains in the base image.

```
ansible-playbook -i inventory_file playbooks/caddy_ssl.yml
```
