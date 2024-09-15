Creating an Ansible playbook to test connection to an AWS instance involves a few steps. First, ensure you have Ansible installed on your control machine, and you have the necessary AWS access set up,  your instance's IP address and your SSH key. Here's a simple playbook to test the connection:

1. **Create Your Ansible Inventory File:**
   Before writing the playbook, add your AWS instance details to an inventory file. This file lists the servers you want Ansible to manage. Create a file named `hosts.ini` (or any name you prefer) and add your AWS instance details under a group `[aws_instances]`:

   ```ini
   [aws_instances]
   aws_instance_1 ansible_host=<your_aws_instance_ip> ansible_user=ec2-user ansible_ssh_private_key_file=<path_to_your_private_key>
   ```

   Replace `<your_aws_instance_ip>` with your AWS instance's IP address and `<path_to_your_private_key>` with the path to your SSH private key file.

2. **Write the Ansible Playbook:**
   Create a file named `connection_test.yml` and add the following content:

   ```yaml
   ---
   - name: Test Connection to AWS Instance
     hosts: aws_instances
     gather_facts: no

     tasks:
       - name: Ping AWS Instance
         ansible.builtin.ping:
   ```

   This playbook does the following:
   - It targets hosts under the `[aws_instances]` group from your inventory.
   - `gather_facts: no` is used to speed up the execution since we're only interested in testing the connection.
   - It uses the `ansible.builtin.ping` module to test the connection. This module will attempt to ping the AWS instance.

3. **Run the Playbook:**
   Execute the playbook using the `ansible-playbook` command, specifying your inventory file with the `-i` flag:

   ```sh
   ansible-playbook -i hosts.ini connection_test.yml
   ```

   If the connection is successful, you'll see a `SUCCESS` message in the output for the ping task.

This playbook is a simple way to confirm that Ansible can connect to your AWS instance. It's a basic example to start with. As you progress, you can expand your playbooks to manage configurations, deploy applications, and automate tasks on your AWS instances.
