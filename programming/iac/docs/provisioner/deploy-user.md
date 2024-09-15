Provide Ansible playbook to create deploy user for web application server provisioning task. What should be the permissions?

To create a deploy user for web application server provisioning tasks, you can use an Ansible playbook to add the user, set up SSH key-based authentication, and assign appropriate permissions. The deploy user  needs sufficient permissions to manage files, directories, and services related to the web application but should not have unnecessary access that could pose a security risk.

### Ansible Playbook: Create Deploy User

Below is an Ansible playbook that demonstrates how to create a deploy user, add an SSH key, and set appropriate permissions:

```yaml
---
- name: Create deploy user for web application server
  hosts: all
  become: true
  vars:
    deploy_user: deployuser
    deploy_user_home: "/home/{{ deploy_user }}"
    ssh_public_key: "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQD3k66... user@example.com"

  tasks:
    - name: Create deploy user
      ansible.builtin.user:
        name: "{{ deploy_user }}"
        comment: "Deploy user for web application"
        shell: /bin/bash
        create_home: yes
        home: "{{ deploy_user_home }}"

    - name: Set up authorized keys for the deploy user
      ansible.builtin.authorized_key:
        user: "{{ deploy_user }}"
        state: present
        key: "{{ ssh_public_key }}"

    - name: Ensure deploy user has sudo access for necessary commands
      ansible.builtin.lineinfile:
        path: /etc/sudoers.d/{{ deploy_user }}
        line: "{{ deploy_user }} ALL=(ALL) NOPASSWD: ALL"
        validate: 'visudo -cf %s'
        create: yes
        state: present
```

### Explanation of the Playbook:

- **Create Deploy User**: This task creates a user specified by the `deploy_user` variable, sets a home directory, and specifies the default shell.
- **Set Up Authorized Keys**: Adds an SSH public key to the deploy user's `authorized_keys` file for key-based authentication. Replace `ssh_public_key`'s value with your  public key.
- **Ensure Deploy User Has Sudo Access**: Grants the deploy user permission to execute commands as root without a password. This is necessary for tasks that require elevated privileges, such as installing packages or managing system services.

### Permissions for the Deploy User:

- The deploy user is given sudo access to perform tasks that require elevated privileges. The `NOPASSWD: ALL` setting allows executing all commands without a password prompt, which is convenient for automated deployment scripts but should be used with caution due to security implications.
- For tighter security, you can restrict sudo access to only the commands necessary for deployment and server management tasks. This minimizes potential damage if the deploy user's account is compromised.

### Usage:

1. Replace the placeholder `ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQD3k66... user@example.com` with the  SSH public key you want to use for the deploy user.
2. Save this playbook to a file (e.g., `create_deploy_user.yml`).
3. Run the playbook using the `ansible-playbook` command:

```bash
ansible-playbook create_deploy_user.yml
```

### Security Consideration:

- **SSH Key Management**: Ensure the SSH keys are securely managed and distributed. Only trusted keys should be added to the server.
- **Sudo Permissions**: Granting `NOPASSWD: ALL` permissions for sudo access is powerful and convenient for automation but increases security risks. Consider restricting permissions based on the deploy user's  needs.

## Using PEM File Instead of SSH Key 

To modify the playbook for creating a deploy user for web application server provisioning tasks where a PEM file is used instead of a regular SSH key, you'll need to ensure that the PEM file's public key is added to the deploy user's `authorized_keys`. The process for creating the user remains the same, but since you mentioned PEM files specifically, it's important to clarify that a PEM file can contain various types of cryptographic keys,  SSH keys. For SSH, the public key extracted from the PEM file should be in the authorized keys file.

Given that the PEM file usage context here implies the presence of an SSH key pair for secure access, and assuming the PEM file contains or relates to SSH private keys, here's how you might adjust the playbook. Note: The SSH public key must be extracted from the PEM file if not already done.

### Adjusted Ansible Playbook:

```yaml
---
- name: Create deploy user for web application server
  hosts: all
  become: true
  vars:
    deploy_user: deployuser
    deploy_user_home: "/home/{{ deploy_user }}"
    # Assuming the SSH public key extracted from the PEM file is placed here.
    ssh_public_key_path: "/path/to/deployuser.pub"

  tasks:
    - name: Create deploy user
      ansible.builtin.user:
        name: "{{ deploy_user }}"
        comment: "Deploy user for web application"
        shell: /bin/bash
        create_home: yes
        home: "{{ deploy_user_home }}"

    - name: Set up authorized keys for the deploy user
      ansible.builtin.authorized_key:
        user: "{{ deploy_user }}"
        state: present
        key: "{{ lookup('file', ssh_public_key_path) }}"

    - name: Ensure deploy user has limited sudo access
      ansible.builtin.copy:
        dest: "/etc/sudoers.d/{{ deploy_user }}"
        content: "{{ deploy_user }} ALL=(ALL) NOPASSWD: /bin/systemctl restart nginx, /bin/systemctl restart apache2\n"
        owner: root
        group: root
        mode: '0440'
        validate: 'visudo -cf %s'
```

### Key Adjustments:

- **SSH Public Key Path**: This variable `ssh_public_key_path` should point to the file containing the deploy user's SSH public key, which you've extracted from the PEM file.
- **Limited Sudo Access**: The playbook now specifies limited commands the deploy user can run via sudo without a password. Adjust the command list based on your deployment and server management needs.

### Extracting the Public Key from a PEM File:

If you have a PEM file and need to extract the public key (assuming it's an RSA key for SSH), you can use the following command:

```bash
ssh-keygen -y -f /path/to/private_key.pem > /path/to/deployuser.pub
```

Ensure the public key file's path is correctly referenced in the `ssh_public_key_path` variable of your playbook.

### Usage Notes:

- Update `/path/to/deployuser.pub` in the playbook with the  path to your public key file.
- Before running the playbook, ensure you have correctly extracted the SSH public key from your PEM file and that the file is accessible from your Ansible control node.
- Tailor the sudo commands to fit your operational requirements, ensuring the deploy user has only the permissions necessary to perform their role.

I want to separate the deploy user creation that is common to all customers and setup that is unique to  a specific customer. Split the task such that the common task is done during AMI image creation time and the specific task during provisioning a server for a specific customer.

To separate the deploy user creation (common to all customers) from the setup unique to a specific customer, you can split the tasks into two stages:

1. **AMI Image Creation Time**: Handle common tasks such as creating the deploy user and basic system setup. This is done using Packer with an Ansible provisioner.
2. **Provisioning a Server for a Specific Customer**: Apply customer-specific configurations like setting up environment variables, deploying customer-specific keys, or configuring applications uniquely for each customer. This step is  done using Ansible directly on the provisioned instance from the AMI.

### 1. AMI Image Creation with Common Tasks

For the AMI creation part, you would include tasks in your Packer template that utilize Ansible for common configurations like creating the deploy user.

#### Packer Template with Ansible Provisioner

```hcl
# Main builder configuration
builder "amazon-ebs" {
  same as before
}

# Provisioning with Ansible
provisioner "ansible" {
  playbook_file = "deploy_user.yml"
}
```

**Explanation of Changes and HCL Concepts**

* **Blocks:** HCL uses blocks to define resources. `builder`, `source_ami_filter`, and `provisioner` are block types in this case.
* **Block Labels (Optional):** I've added the label "amazon-ebs" to the `builder` block for readability if you have multiple builders. It's not strictly required.
* **Attributes:** Each configuration setting within a block is an attribute (`region`, `instance_type`, etc.).
* **Nested Blocks:** The `source_ami_filter` is a nested block within the `builder`.
* **Function Calls:** You can use HCL's built-in functions like `timestamp()` to generate dynamic values.

**Important Notes**

* **HCL Version:** Make sure your version of Packer supports HCL2. 
* **File Naming:** Save this HCL configuration with a `.pkr.hcl` extension (e.g., `packer-config.pkr.hcl`).

#### `deploy_user.yml` for Common Tasks

```yaml
---
- name: Common setup for all AMIs
  hosts: all
  become: true
  tasks:
    - name: Create deploy user
      ansible.builtin.user:
        name: deploy
        shell: /bin/bash
        create_home: yes
```

### 2. Provisioning Servers with Customer-Specific Configurations

Once the AMI is created and you're provisioning an instance for a specific customer, use a separate Ansible playbook to apply configurations unique to that customer.

#### Example: `customer_key_setup.yml`

```yaml
---
- name: Setup specific to a customer
  hosts: all
  become: true
  vars:
    customer_name: "ExampleCustomer"
    customer_ssh_key: "{{ lookup('file', 'customer_keys/example_customer.pub') }}"
  tasks:
    - name: Set up customer-specific authorized keys for the deploy user
      ansible.builtin.authorized_key:
        user: deployuser
        state: present
        key: "{{ customer_ssh_key }}"

    - name: Configure environment variables or other settings unique to the customer
      ansible.builtin.lineinfile:
        path: "/home/deployuser/.bashrc"
        line: "export CUSTOMER_NAME='{{ customer_name }}'"
```

### Usage

1. **Create AMI**: Use Packer to create the AMI, incorporating common configurations.
2. **Provision Instances**: When provisioning an instance for a specific customer, run the `customer_specific_setup.yml` playbook against the new instance, possibly passing in customer-specific variables or files.

This approach cleanly separates the common setup performed at the AMI creation stage from the customer-specific configurations applied at the instance provisioning stage. It ensures a base level of configuration is baked into the AMI for efficiency, while still allowing customization for individual customers upon instance launch.

## PEM File Instead of SSH Keys

To modify the Ansible playbook to use a PEM file for the SSH key instead of a public key from a file lookup, you need to adjust the way the key is handled. Since PEM files are  used for private keys and the `authorized_key` module is for adding public keys to the `.ssh/authorized_keys` file, I'll assume you want to use the PEM file for SSH connections or tasks within Ansible that require SSH authentication.

However, if the goal is to place a PEM file on the server for use in other applications or services that require it (since directly using a PEM file for the `authorized_key` module is not a standard practice), you might want to securely copy the PEM file to the server and ensure the correct permissions are set. Here's how you can modify the playbook to include a task that copies a PEM file to the server for a customer-specific configuration:

```yaml
---
- name: Setup specific to a customer
  hosts: all
  become: true
  vars:
    customer_name: "ExampleCustomer"
    customer_pem_file: "customer_keys/example_customer.pem"  # Specify the path to the PEM file

  tasks:
    - name: Copy customer-specific PEM file to the server
      ansible.builtin.copy:
        src: "{{ customer_pem_file }}"
        dest: "/home/deployuser/{{ customer_name }}.pem"  # Destination path on the server
        owner: deployuser
        group: deployuser
        mode: '0600'  # Ensures the file is readable only by the owner

    - name: Set up customer-specific authorized keys for the deploy user
      ansible.builtin.authorized_key:
        user: deployuser
        state: present
        key: "{{ lookup('file', customer_pem_file) }}"

    - name: Configure environment variables or other settings unique to the customer
      ansible.builtin.lineinfile:
        path: "/home/deployuser/.bashrc"
        line: "export CUSTOMER_NAME='{{ customer_name }}'"
```

In this modification:
- The `vars` section now includes `customer_pem_file` to specify the path to the PEM file.
- A new task named "Copy customer-specific PEM file to the server" uses the `ansible.builtin.copy` module to securely transfer the PEM file to the target server. The destination includes the customer name for uniqueness, and permissions are set to `0600` to ensure the file is secure.
- The `authorized_key` task remains unchanged as a placeholder, since directly using a PEM file with this module is not standard. If you're ly looking to use the PEM file for SSH authentication in Ansible, you'd  configure this in your Ansible inventory or SSH settings rather than in a playbook task.

The direct use of PEM files for authorized SSH keys is not typical since PEM files usually contain private keys. Ensure you're following security best practices for your specific use case, especially when handling private keys.

If the PEM file is used by the customer for passwordless login to an EC2 instance and not specifically for Ansible operations, then the goal is to ensure the EC2 instance has the corresponding public key installed in the `~/.ssh/authorized_keys` file for the user (in this case, `deployuser`). Typically, the PEM file you're referring to is a private key, and what needs to be added to the `authorized_keys` file is the public key derived from it. 

However, since the PEM file itself won't be directly used in the `authorized_key` module (because this module requires the public key), and assuming there's a misunderstanding in directly using a PEM file for `authorized_key`, let's adjust the initial approach to align with common practices for passwordless SSH setup:

1. **Ensure you have the public key**: The public key should be extracted from the PEM file (if not already provided). This is  done outside of Ansible and is a one-time operation per key.

2. **Use the public key in `authorized_key` task**: You would then specify the public key in the Ansible playbook to ensure it's added to the `authorized_keys` file for passwordless authentication.

If you already have the public key or can extract it from the PEM, the original playbook you provided does the correct operation by adding an `authorized_key` for the `deployuser`. If the public key is not readily available but you have access to the PEM file, you would first extract the public key using a command like `ssh-keygen -y -f /path/to/private_key.pem > public_key.pub` outside of Ansible.

Given your clarification, here's a slight modification to the playbook to focus on the usage of a public key (assuming it's already extracted and available):

```yaml
---
- name: Setup specific to a customer
  hosts: all
  become: true
  vars:
    customer_name: "ExampleCustomer"
    customer_public_key: "{{ lookup('file', 'customer_keys/example_customer.pub') }}"  # Assuming the public key is extracted

  tasks:
    - name: Set up customer-specific authorized keys for the deploy user
      ansible.builtin.authorized_key:
        user: deployuser
        state: present
        key: "{{ customer_public_key }}"

    - name: Configure environment variables or other settings unique to the customer
      ansible.builtin.lineinfile:
        path: "/home/deployuser/.bashrc"
        line: "export CUSTOMER_NAME='{{ customer_name }}'"
```

This playbook assumes:
- `customer_keys/example_customer.pub` is the path to the public key extracted from the PEM file.
- The `authorized_key` module is used to add the public key to the `deployuser`'s `authorized_keys` for passwordless SSH access.

The key part here is making sure you have the public key ready (`example_customer.pub`) as the `authorized_key` module requires the SSH public key content, not the PEM file directly used for SSH logins.
