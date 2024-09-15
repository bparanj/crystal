Here's a Ansible playbook for installing and configuring Fail2ban on Ubuntu 22.04:

**Filename: fail2ban-playbook.yml**

```yaml
---
- name: Install and configure Fail2ban
  hosts: all  # Replace 'all' with your specific host group
  become: true  # Required for package installation and service management

  tasks:
    - name: Install Fail2ban
      apt:
        name: fail2ban
        state: present

    - name: Copy default Fail2ban configuration (for backup)
      copy:
        src: /etc/fail2ban/jail.conf
        dest: /etc/fail2ban/jail.conf.backup
        remote_src: yes  

    - name: Create Fail2ban local configuration
      template:
        src: jail.local.j2  # You'll need to create this template
        dest: /etc/fail2ban/jail.local
        owner: root
        group: root
        mode: 0644

    - name: Ensure Fail2ban service is enabled and running
      service:
        name: fail2ban
        state: started
        enabled: true
```

**Important Parts**

* **Hosts:** Update the `hosts` line to target the servers where you want Fail2ban.
* **`jail.local.j2`** (Template): You need to create a Jinja2 template file named `jail.local.j2`. This will contain your custom Fail2ban jail configurations. See a basic example below.

**Example `jail.local.j2` template**

```jinja2
[DEFAULT]
ignoreip = 127.0.0.1/8 ::1  # Add your trusted IPs
bantime = 86400  # Ban for 1 day 
findtime = 600   # Find suspicious attempts within 10 minutes
maxretry = 3     # Allow 3 retries before banning

[sshd]
enabled = true
```

**How to Use**

1.  **Create the `jail.local.j2` file:** Populate it with your desired Fail2ban jail configurations. Place it in a `templates` folder next to your playbook.
2.  **Run the playbook:** `ansible-playbook fail2ban-playbook.yml`

**Key Points**

* **Customization:** The key to this playbook is the `jail.local.j2` template. Edit it extensively to define the jails and protection rules you want.
* **Roles:** For larger setups, consider using a dedicated Ansible role (e.g., from Ansible Galaxy) for more organized management of Fail2ban configuration. 

**Let me know if you'd like help crafting a more elaborate `jail.local.j2` template with specific filters and actions** 

Here's an Ansible playbook that installs and configures Fail2Ban on an Ubuntu 22.04 server. This playbook includes tasks to:

1. **Install Fail2Ban**: Ensures that Fail2Ban is installed.
2. **Configure Fail2Ban**: Copies a custom configuration file from the control node to the target node. You'll need to create this configuration file based on your specific needs.
3. **Ensure Fail2Ban is running and enabled on boot**: Manages the state of the Fail2Ban service.

```yaml
---
- name: Install and configure Fail2Ban on Ubuntu 22.04
  hosts: your_host_group
  become: yes  # Required to gain root privileges
  tasks:
    - name: Install Fail2Ban
      ansible.builtin.apt:
        name: fail2ban
        state: present

    - name: Copy Fail2Ban configuration file
      ansible.builtin.copy:
        src: /path/to/your/jail.local
        dest: /etc/fail2ban/jail.local
        owner: root
        group: root
        mode: '0644'
      notify: restart fail2ban

    - name: Ensure Fail2Ban is running and enabled on boot
      ansible.builtin.service:
        name: fail2ban
        state: started
        enabled: yes

  handlers:
    - name: restart fail2ban
      ansible.builtin.service:
        name: fail2ban
        state: restarted
```

Before running this playbook:

- Replace `your_host_group` with the group name of your target servers defined in your Ansible inventory. If you're targeting a single server, specify its hostname or IP address.
- Ensure you have a Fail2Ban configuration file ready to be deployed (`jail.local`). The path `/path/to/your/jail.local` should be replaced with the  path to your customized `jail.local` file on the control node. The `jail.local` file is used to override the default configuration settings.
- Ensure Ansible is installed on your control machine and you have SSH access to the target machine(s).

To run the playbook, save it to a file (e.g., `install_fail2ban.yml`), and then use the `ansible-playbook` command:

```sh
ansible-playbook install_fail2ban.yml
```

This playbook is a basic example. You might want to further customize the Fail2Ban configuration to meet your specific needs. You can do this by modifying the `jail.local` file or by adding more tasks to the playbook to deploy additional configuration files as necessary.

Creating a basic configuration file for Fail2Ban involves setting up a few key elements. Fail2Ban works by monitoring log files for patterns that indicate malicious activity, such as repeated failed login attempts, and then applying rules to block the offending IP addresses, usually through firewall rules.

Fail2Ban configurations can be overridden or extended by creating or modifying the `jail.local` file in the `/etc/fail2ban` directory. This file does not exist by default, but when created, it allows you to customize settings without modifying the default `jail.conf` file, ensuring your custom settings are preserved across package updates.

Here's a basic `jail.local` configuration that you can use as a starting point. This example includes a jail for SSH (which is very common), but you can extend it with more services as needed.

```ini
[DEFAULT]
# Ban hosts for one hour:
bantime = 1h

# Find 5 failures within a 10-minute window:
findtime = 10m

# The number of failures before a host gets banned.
maxretry = 5

# Email configuration for notifications.
destemail = your_email@example.com
sender = fail2ban@example.com
mta = sendmail
action = %(action_mwl)s

# Override the default ignoreip value if you have IPs that should never be banned.
# ignoreip = 127.0.0.1/8 ::1

[sshd]
enabled = true
port = ssh
filter = sshd
logpath = /var/log/auth.log
maxretry = 3
```

### Key Elements of the Configuration

- **[DEFAULT]**: Settings in this section apply to all jails unless overridden in the jail's specific section.
- **bantime**: The duration for which an IP is banned. This can be specified in seconds or using a time duration (e.g., `1h` for one hour, `1d` for one day).
- **findtime** and **maxretry**: These settings define the failure threshold for banning. If Fail2Ban finds `maxretry` failed attempts within a `findtime` period, the source IP will be banned.
- **destemail** and **action**: Configuration for email notifications. The `action = %(action_mwl)s` line configures Fail2Ban to send an email with whois information and relevant log lines on ban. Make sure to replace `your_email@example.com` with your  email address.
- **[sshd]**: A jail for monitoring SSH login attempts. This section can be customized or extended with additional jails for other services.

### Extending Your Configuration

To monitor other services, you can add more sections similar to `[sshd]`. For each service, you would specify the service-specific settings such as `enabled`, `filter`, `port`, `logpath`, and any custom values for `findtime`, `bantime`, and `maxretry`.

Before implementing this configuration, ensure you have Fail2Ban installed and that you create or modify the `jail.local` file with appropriate permissions. Also, test your configuration to ensure it behaves as expected, paying special attention to the impact of banning policies on legitimate users and services.

Yes, adding the line `ignoreip = 127.0.0.1/8 ::1` to your Fail2Ban configuration file is a good starting point. This setting instructs Fail2Ban to ignore any ban actions for the specified IP addresses. `127.0.0.1/8` represents the loopback address range (localhost) for IPv4, and `::1` is the loopback address for IPv6. By  this line, you prevent Fail2Ban from banning legitimate access from the local system, which is especially important for services that might have legitimate reasons to connect frequently and could otherwise be mistakenly banned.

Here's a basic example of a Fail2Ban configuration file (`jail.local`) that you can use as a starting point. This file overrides some default settings from `jail.conf` and specifies a few common jails:

```ini
[DEFAULT]
# "ignoreip" can be an IP address, a CIDR mask, or a DNS host. Here, localhost is excluded.
ignoreip = 127.0.0.1/8 ::1

# "bantime" is the duration of time a host is banned.
bantime = 10m

# "findtime" is the duration of time that a host is monitored for repeated failures.
findtime = 10m

# "maxretry" is the number of failures that triggers a ban action against the host.
maxretry = 5

# Email for sending ban notifications.
destemail = your_email@example.com

# Action to take when banning an IP. See action.d/ directory for other options.
action = %(action_mwl)s

[sshd]
enabled = true
port = ssh
filter = sshd
logpath = /var/log/auth.log
maxretry = 3

[sshd-ddos]
enabled = true
port = ssh
filter = sshd-ddos
logpath = /var/log/auth.log
maxretry = 6

```

This configuration:

- Ignores localhost for banning actions.
- Sets a default ban time of 10 minutes.
- Observes failed attempts within a 10-minute window.
- Triggers a ban after 5 retries by default, but adjusts this for specific services (e.g., 3 retries for SSH).
- Uses the `action_mwl` action, which bans the IP and sends an email with the whois report and relevant log lines.

Remember to replace `your_email@example.com` with your  email address if you wish to receive notifications. Also, ensure that you have mail utilities configured on your server for email notifications to work.

Before deploying this configuration, review and adjust the settings to match your security policies and operational requirements. Fail2Ban is highly customizable, allowing you to fine-tune its behavior to best fit your environment.

Ubuntu 22.04 (Jammy Jellyfish) does not come with `sendmail` installed by default. Ubuntu  includes minimal packages necessary for a basic setup to keep the installation lean. For mail services, users are encouraged to install the mail server software that best fits their needs, whether it be `sendmail`, `Postfix`, `Exim`, or any other MTA (Mail Transfer Agent).

If you need `sendmail` or a similar MTA for sending emails from your server, you can easily install it. For example, to install `Postfix`, which is  used as an alternative to `sendmail` and often preferred for its simpler configuration, you can use the following command:

```sh
sudo apt update
sudo apt install postfix
```

During the installation, you will be prompted to choose the type of mail configuration; you can select "Internet Site" if your server should send emails directly to the Internet or choose another option that better fits your setup.

If you specifically need `sendmail`, you can install it with:

```sh
sudo apt update
sudo apt install sendmail
```

After installing, you may need to configure it to suit your requirements.

Verifying your Fail2Ban installation and setup involves several steps to ensure it's installed, running correctly, and effectively banning IPs that meet your defined criteria for banning. Here’s how you can go about it:

### 1. Check Fail2Ban Installation

First, check if Fail2Ban is installed by querying its version. This command helps confirm the installation and shows the installed version:

```sh
fail2ban-client version
```

### 2. Verify Fail2Ban Service Status

Next, verify that the Fail2Ban service is active and running on your system:

```sh
sudo systemctl status fail2ban
```

This command gives you the status of Fail2Ban, showing whether it's active (running) or not. An active status indicates that Fail2Ban is running as expected.

### 3. Check Fail2Ban Configuration

Fail2Ban works based on jail configurations that define which services to monitor and the criteria for banning IPs. You can check your active jails using:

```sh
sudo fail2ban-client status
```

This command lists all jails that are currently enabled. To dive deeper into the configuration of a specific jail, use:

```sh
sudo fail2ban-client status <jail-name>
```

Replace `<jail-name>` with the name of the jail you want to inspect. This will show you details like the currently banned IPs for that jail.

### 4. Test Fail2Ban Filtering

To ensure Fail2Ban is correctly identifying and banning offending IPs, you can simulate an attack or a failed login attempt (depending on what your jails are monitoring) and then check if Fail2Ban bans the IP as expected. For example, if you have a jail set up for SSH, you could attempt to log in with incorrect credentials multiple times from a specific IP.

Afterwards, use the command to check the status of the sshd jail (if that’s what you’re testing):

```sh
sudo fail2ban-client status sshd
```

This should show the offending IP as banned.

### 5. Review Fail2Ban Logs

Fail2Ban logs actions (such as banning and unbanning IPs) to its log file, which is  located at `/var/log/fail2ban.log`. You can inspect this file to see the history of Fail2Ban’s actions:

```sh
sudo less /var/log/fail2ban.log
```

This allows you to scroll through the log file. Look for entries related to the jails you're interested in to verify that Fail2Ban is actively monitoring and taking action.

### 6. Check Firewall Rules

Fail2Ban bans IPs by updating firewall rules to reject traffic from those IPs. You can check the current firewall rules to see the bans in effect:

For `iptables`, use:

```sh
sudo iptables -L
```

For `nftables`, use:

```sh
sudo nft list ruleset
```

### Conclusion

By following these steps, you can thoroughly verify your Fail2Ban installation and setup. It’s important to periodically check Fail2Ban’s status and logs to ensure it continues to protect your system effectively against unwanted access attempts.

When using Packer to provision machines with Ansible,  setting up Fail2Ban as part of the provisioning process, the location of the Fail2Ban configuration file (e.g., `jail.local`) on your **control machine** (the machine running Packer) can be anywhere that is accessible to the Ansible playbook being executed by Packer. However, during the playbook run, you'll need to ensure that this file gets copied to the correct location on the **target machine** (the machine being provisioned by Packer).

The standard location for the Fail2Ban configuration file `jail.local` on the target machine is `/etc/fail2ban/jail.local`. This is where Fail2Ban expects to find override settings for its default configuration.

Here's a high-level overview of how this process might look:

1. **On your control machine**: Place your `jail.local` file in a known location within your project's directory structure where Packer and Ansible have access to it. For example, if you have a directory structure like this:

    ```
    my-packer-project/
    ├── ansible/
    │   ├── playbook.yml
    │   └── roles/
    │       └── fail2ban/
    │           ├── files/
    │           │   └── jail.local  # Your custom Fail2Ban config
    │           └── tasks/
    │               └── main.yml
    └── packer.json
    ```

    You might place `jail.local` under `ansible/roles/fail2ban/files/`.

2. **In your Ansible playbook**: Add a task to copy the `jail.local` file from its location in your project directory to the correct location on the target machine. If using roles, this might be defined in a task like:

    ```yaml
    - name: Copy Fail2Ban configuration file
      ansible.builtin.copy:
        src: jail.local
        dest: /etc/fail2ban/jail.local
        owner: root
        group: root
        mode: '0644'
    ```

    This assumes that your playbook or role has appropriate tasks for installing and configuring Fail2Ban, and that the `copy` task is part of a role or playbook that runs after Fail2Ban is installed.

3. **In your Packer configuration**: Ensure that Packer is set to use Ansible as a provisioner, and point it to your playbook. For example, in `packer.json`, you might have something like:

    ```json
    {
      "provisioners": [
        {
          "type": "ansible",
          "playbook_file": "ansible/playbook.yml"
        }
      ]
    }
    ```

4. **Running Packer**: When you run Packer, it will use Ansible to execute your playbook on the target machine as part of the provisioning process. The `copy` task in your playbook will transfer the `jail.local` file from your control machine to the correct location on the target machine.

The key is that the `jail.local` file needs to be accessible to the Ansible playbook when it runs, and the playbook should take care of placing it in the correct location on the target machine.

Yes, it's generally a good practice to take a backup of existing configuration files like `jail.conf` before making changes, even if your project uses Git to store files. Here's why:

### 1. **Safety Net**: 
A backup serves as a safety net, allowing you to quickly revert to the original configuration if something goes wrong with your changes. This can be crucial in production environments where uptime and stability are paramount.

### 2. **Versioning and History**:
While Git provides version control and the ability to revert to previous versions, having a direct backup on the server can be beneficial for immediate access or recovery, especially if the changes lead to issues that prevent normal Git operations.

### 3. **Best Practices**:
It's a best practice in system administration to backup configuration files before making changes. This practice ensures that you always have a way to restore the system's previous state without relying solely on external systems (like Git).

### 4. **Environment Specific Configurations**:
Sometimes, configuration files on a server contain environment-specific settings that might not be tracked in Git, especially if secrets or sensitive information is involved. Having a local backup ensures you don't lose these customizations.

### Making a Backup:

Before making changes to `jail.conf`, you can create a backup like so:

```bash
sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.conf.backup
```

### Regarding Git:

Using Git to manage configuration files is a smart approach, as it provides version control, change tracking, and collaboration tools. However, Git should complement, not replace, standard backup procedures. Configuration files in Git likely represent a "template" or "baseline" state, which might be customized further in specific environments.

### Conclusion:

Even with Git, take a moment to back up critical configuration files before making changes. This approach adds an extra layer of safety and conforms to best practices in IT operations. After making and testing your changes, you can commit the final version to Git, ensuring that your repository stays up-to-date with the operational state of your configurations.

Yes, the task you've outlined will work for creating a backup of the `jail.conf` file, but with an important consideration regarding its first-time execution. If the playbook is run for the first time and Fail2Ban is not yet installed (thus the `jail.conf` file does not exist), this task will fail because the source file does not exist. To handle this scenario gracefully, you can add a condition to check if the file exists before attempting to copy it. Here's how you can modify the task:

```yaml
- name: Check if default Fail2Ban configuration exists
  ansible.builtin.stat:
    path: /etc/fail2ban/jail.conf
  register: jail_conf_stat

- name: Copy default Fail2ban configuration (for backup)
  ansible.builtin.copy:
    src: /etc/fail2ban/jail.conf
    dest: /etc/fail2ban/jail.conf.backup
    remote_src: yes
  when: jail_conf_stat.stat.exists
```

Here's what these tasks do:

1. **Check if `jail.conf` exists**: The `ansible.builtin.stat` module is used to check if the default Fail2Ban configuration file (`jail.conf`) exists. This task registers the result of the check in a variable called `jail_conf_stat`.

2. **Conditionally copy the file**: The `ansible.builtin.copy` task is then conditioned to run only if `jail.conf` exists, as indicated by `jail_conf_stat.stat.exists`. This prevents the task from failing if Fail2Ban is not installed and `jail.conf` does not exist yet.

This approach ensures that your playbook is idempotent and can handle scenarios where Fail2Ban might not be installed on the target system during the first playbook run. It also prevents potential errors from stopping your playbook execution and provides a more robust solution for managing configurations and backups with Ansible.

In Ansible playbooks, the `handlers` section is used to define tasks that should only be run when notified by other tasks. Handlers are  used for operations that need to occur after a change to the system, such as restarting a service after its configuration file has been modified. This ensures that the service picks up any changes made to its configuration.

In the provided playbook example, the `restart fail2ban` handler is defined to restart the Fail2Ban service. This handler is notified by the "Copy Fail2Ban configuration file" task using the `notify` directive. Here's why this is important and useful:

1. **Configuration Changes**: When you change the configuration of a service like Fail2Ban, the service needs to be restarted for those changes to take effect. The playbook modifies Fail2Ban's configuration by copying a new `jail.local` file, so restarting the service ensures it uses the updated configuration.

2. **Efficiency**: The handler is only triggered if the task that notifies it makes a change. If the "Copy Fail2Ban configuration file" task does not change the file (because the existing file is already the same as the source), then the handler won't be triggered, and the service won't be unnecessarily restarted. This makes your playbook more efficient by avoiding redundant service restarts.

3. **Organization and Readability**: By separating the restart operation into a handler, the playbook keeps the logic for managing the service's state separate from the logic for configuring the service. This separation improves the readability and maintainability of your playbook.

4. **Idempotency**: Handlers contribute to the idempotency of an Ansible playbook. Even if the playbook is run multiple times, the service will only be restarted if a change is made, preventing unnecessary restarts and ensuring the playbook can safely be re-run.

In summary, the `restart fail2ban` handler in your playbook ensures that Fail2Ban is restarted and applies any new configuration changes whenever the `jail.local` file is updated. This pattern is a best practice for managing services with Ansible.

Given the recommended directory structure where your `main.yml` is located under the `tasks` folder and your `jail.local` file is under the `files` folder within an Ansible role, you don't need to specify the absolute path to `jail.local` when referring to it in your task. Ansible has a feature known as 'search paths' for roles, which includes looking in specific directories for files, templates, and other resources based on convention.

Here's the simplified structure for clarity:

```
roles/
└── your_role_name/
    ├── files/
    │   └── jail.local
    ├── tasks/
    │   └── main.yml
    └── ...
```

When using the `ansible.builtin.copy` module within a role, Ansible automatically searches for files to copy in the `files` directory of the role. Therefore, you can reference `jail.local` directly by its filename without needing the full path:

```yaml
- name: Copy Fail2Ban configuration file
  ansible.builtin.copy:
    src: jail.local
    dest: /etc/fail2ban/jail.local
    owner: root
    group: root
    mode: '0644'
  notify: restart fail2ban
```

In this context, `src: jail.local` is sufficient for Ansible to find your file in the `files` directory of the role being executed. This approach simplifies file management within roles and avoids hard-coding paths, making your roles more portable and easier to understand.

To organize your Ansible playbook more effectively, especially when it starts to grow in complexity, you can split it into multiple files. This can include separating tasks into individual files, defining variables in their own files, and using roles for better reusability and structure. Given your `main.yml` playbook that installs and configures Fail2Ban, here's how you might split it:

### Step 1: Create a Role for Fail2Ban

1. **Create Role Directory Structure**: First, create a directory structure for your role. Let's call the role `fail2ban`. Your directory structure under the `roles` directory would look like this:

    ```
    roles/
    └── fail2ban/
        ├── tasks/
        │   ├── main.yml
        │   ├── install.yml
        │   ├── configure.yml
        │   └── service.yml
        ├── handlers/
        │   └── main.yml
        └── files/
            └── jail.local
    ```

2. **Split Tasks**: Break down the tasks from your original `main.yml` into separate files within the `tasks` directory of the role. For example:

    - `install.yml` for installing Fail2Ban.
    - `configure.yml` for checking and copying configuration files.
    - `service.yml` for ensuring Fail2Ban is running and enabled.

3. **Define Handlers**: Move the handler for restarting Fail2Ban into the `handlers/main.yml` file within the role.

### Step 2: Populate the Files

- **tasks/install.yml**:

    ```yaml
    - name: Install Fail2Ban
      ansible.builtin.apt:
        name: fail2ban
        state: present
    ```

- **tasks/configure.yml**:

    ```yaml
    - name: Check if default Fail2Ban configuration exists
      ansible.builtin.stat:
        path: /etc/fail2ban/jail.conf
      register: jail_conf_stat

    - name: Copy default Fail2ban configuration (for backup)
      ansible.builtin.copy:
        src: /etc/fail2ban/jail.conf
        dest: /etc/fail2ban/jail.conf.backup
        remote_src: yes
      when: jail_conf_stat.stat.exists

    - name: Copy Fail2Ban configuration file
      ansible.builtin.copy:
        src: "{{ role_path }}/files/jail.local"
        dest: /etc/fail2ban/jail.local
        owner: root
        group: root
        mode: "0644"
      notify: restart fail2ban
    ```

- **tasks/service.yml**:

    ```yaml
    - name: Ensure Fail2ban is running and enabled on boot
      ansible.builtin.service:
        name: fail2ban
        state: started
        enabled: true
    ```

- **handlers/main.yml**:

    ```yaml
    - name: restart fail2ban
      ansible.builtin.service:
        name: fail2ban
        state: restarted
    ```

- **tasks/main.yml** (This file will include other task files):

    ```yaml
    ---
    - include_tasks: install.yml
    - include_tasks: configure.yml
    - include_tasks: service.yml
    ```

### Step 3: Use the Role in Your Playbook

Finally, in your playbook, instead of directly listing tasks, you would now call the `fail2ban` role:

```yaml
---
- name: Install and configure Fail2ban
  hosts: all # Replace 'all' with your specific host group
  become: true # Required for package installation and service management

  roles:
    - fail2ban
```

### Conclusion

This structure makes your playbook more modular, easier to maintain, and reusable across different projects. Each part of the Fail2Ban setup is clearly separated, making it easier to update or extend the configuration in the future.

Yes, that's correct. To use the role-based structure effectively, you should create a `fail2ban.yml` playbook inside the `playbooks` folder. This playbook will define the execution context for the `fail2ban` role you've prepared, specifying which hosts to target and any other playbook-level settings. Here's a step-by-step guide to setting this up:

### Step 1: Create the Playbook

1. **Navigate to Your Playbooks Directory**: Go to your `playbooks` directory where you intend to organize your playbook files.

2. **Create the `fail2ban.yml` File**: Inside the `playbooks` directory, create a file named `fail2ban.yml`. This is where you'll define the playbook that utilizes the `fail2ban` role.

### Step 2: Define the Playbook Content

Edit the `fail2ban.yml` file and add the following content, which outlines the use of the `fail2ban` role. This playbook specifies that it should run on all hosts (you might want to adjust the `hosts` value to target a specific group or host), and it requires elevated privileges (`become: true`) for tasks like installing packages and managing service states.

```yaml
---
- name: Install and configure Fail2Ban on Ubuntu 22.04
  hosts: all  # Adjust this to target a specific group or host
  become: true  # Required for tasks needing root privileges

  roles:
    - fail2ban
```

### Step 3: Organize Your Directory Structure

Ensure your Ansible project directory is well organized. For example, you might have a structure like this:

```
ansible-project/
├── playbooks/
│   └── fail2ban.yml
└── roles/
    └── fail2ban/
        ├── tasks/
        │   ├── main.yml
        │   ├── install.yml
        │   ├── configure.yml
        │   └── service.yml
        ├── handlers/
        │   └── main.yml
        └── files/
            └── jail.local
```

### Step 4: Running Your Playbook

To run your playbook, navigate to the root of your Ansible project directory (where your `playbooks` folder is located) and execute the playbook using the `ansible-playbook` command. Make sure you have access to your inventory (hosts) and that your control machine is configured to communicate with the target hosts over SSH.

```sh
ansible-playbook playbooks/fail2ban.yml -i your_inventory_file
```

Replace `your_inventory_file` with the path to your inventory file, or if you're using the default inventory path, you might not need to specify it.

### Conclusion

By organizing your Ansible project this way, you make your infrastructure as code more maintainable, scalable, and understandable. The playbook in the `playbooks` directory serves as an entry point to applying the configurations defined in your roles, allowing for clear separation of logic and reusability across different environments or projects.

## Steps

1. Create the directory structure.

```
ansible-project/
├── playbooks/
│   └── fail2ban.yml
└── roles/
    └── fail2ban/
        ├── tasks/
        │   ├── main.yml
        │   ├── install.yml
        │   ├── configure.yml
        │   └── service.yml
        ├── handlers/
        │   └── main.yml
        └── files/
            └── jail.local
```

2. Copy the files to their locations.

3. Modify the Packer template to include fail2ban playbook.

4. Create AMI image 

5. Verify fail2ban on EC2 instance manually
