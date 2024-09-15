## Logrotate Configuration with Ansible Playbook

This is day 2 operations. Move to the next folder.

To set up `logrotate` on Ubuntu 22.04 using an Ansible playbook that can be included in a Packer template, you'll create a playbook that installs `logrotate`, ensures it's configured for your specific applications or system logs, and optionally forces an immediate rotation for testing.

Here's a basic example of how such a playbook might look:

### Ansible Playbook for Logrotate

```yaml
---
- name: Configure logrotate for system logs
  hosts: all
  become: true
  tasks:
    - name: Ensure logrotate is installed
      ansible.builtin.apt:
        name: logrotate
        state: present
        update_cache: yes

    - name: Setup custom logrotate configuration
      ansible.builtin.template:
        src: custom_logrotate.conf.j2
        dest: /etc/logrotate.d/custom_logs
        owner: root
        group: root
        mode: "0644"
      notify: force log rotation

  handlers:
    - name: force log rotation
      ansible.builtin.command: logrotate -f /etc/logrotate.d/custom_logs
      changed_when: false
```

### Explanation:

1. **Ensure logrotate is installed**: This task updates the package lists and installs `logrotate` if it's not already installed.

2. **Setup custom logrotate configuration**: This task uses a Jinja2 template file (`custom_logrotate.conf.j2`) to create a custom logrotate configuration. You'll need to create this template based on your specific log rotation needs.

3. **Handlers - force log rotation**: Optionally, you can immediately force log rotation to test your configuration. This handler runs `logrotate -f`, which forces rotation based on your custom configuration. `changed_when: false` is used to prevent Ansible from reporting this task as a change on subsequent playbook runs if the  state hasn't changed.

### Custom Logrotate Configuration Template

You need to create a Jinja2 template (`custom_logrotate.conf.j2`) that Ansible will use to generate the logrotate configuration. Here's an example template for rotating and compressing Apache logs:

```jinja
/var/log/apache2/*.log {
    weekly
    missingok
    rotate 4
    compress
    delaycompress
    notifempty
    create 640 root adm
    sharedscripts
    postrotate
        if /etc/init.d/apache2 status > /dev/null ; then \
            /etc/init.d/apache2 reload > /dev/null; \
        fi;
    endscript
}
```

Replace the paths and settings in the template with those appropriate for your application or system logs.

### Integrating Playbook with Packer

To integrate this playbook into a Packer build, ensure your Packer template (HCL format) includes an Ansible provisioner block pointing to this playbook:

```hcl
source "amazon-ebs" "example" {
  // Configuration for the source AMI
  // ...
}

build {
  sources = ["source.amazon-ebs.example"]

  provisioner "ansible" {
    playbook_file = "path/to/your_ansible_playbook.yml"
  }
}
```

Make sure the path to the playbook is correct, and place your `custom_logrotate.conf.j2` Jinja2 template in the appropriate directory so Ansible can find it.

This setup provides a basic framework. Customize the logrotate settings in the Jinja2 template as needed to match your specific logging policies and requirements.

To customize the logrotate configuration for Caddy, Redis, and PostgreSQL on Ubuntu 22.04 via an Ansible playbook, you'll modify the Jinja2 template to include appropriate log rotation settings for these services. Here's how you can adjust the playbook and create a custom logrotate configuration template for each service.

### Adjusted Ansible Playbook

The main playbook structure remains the same as previously described. Ensure it includes tasks to install logrotate and deploy your custom configuration.

### Custom Logrotate Configuration Template for Caddy, Redis, PostgreSQL

Create a Jinja2 template named `custom_logrotate.conf.j2` with rotation rules for Caddy, Redis, and PostgreSQL. Here's an example configuration:

```jinja
# Logrotate configuration for Caddy, Redis, PostgreSQL

# Caddy web server logs
/var/log/caddy/*.log {
    daily
    missingok
    rotate 7
    compress
    delaycompress
    notifempty
    create 640 caddy caddy
}

# Redis logs
/var/log/redis/*.log {
    weekly
    missingok
    rotate 4
    compress
    delaycompress
    notifempty
    create 640 redis redis
    postrotate
        /usr/bin/redis-cli -p {{ redis_port }} bgrewriteaof
    endscript
}

# PostgreSQL logs
/var/log/postgresql/*.log {
    daily
    missingok
    rotate 7
    compress
    delaycompress
    notifempty
    create 640 postgres postgres
    postrotate
        /usr/bin/pg_ctlcluster {{ postgres_version }} main reload
    endscript
}
```

- For **Caddy**: Adjust the log path if your Caddy logs are stored elsewhere. The `create` directive uses `caddy` as both the user and group; adjust if your setup is different.
- For **Redis**: The `postrotate` script uses `redis-cli` to rewrite the append-only file (`bgrewriteaof`), beneficial for Redis persistence setup. Replace `{{ redis_port }}` with your Redis server's port.
- For **PostgreSQL**: The `postrotate` action reloads PostgreSQL to apply log rotation without restarting the database service. Replace `{{ postgres_version }}` with the version of PostgreSQL you're running.

### Integrating the Template into the Playbook

Ensure the Ansible playbook is correctly pointing to this Jinja2 template for the setup of logrotate configuration. The playbook's task that deploys the logrotate configuration should reference `custom_logrotate.conf.j2`.

### Note:

- **Customization**: The provided log paths and configurations are examples; you'll need to adjust paths, users, groups, and potentially commands based on your specific environment and requirements.
- **Service-Specific Commands**: For Redis and PostgreSQL, the `postrotate` scripts are crucial for ensuring the services continue to log correctly after logs are rotated. Ensure these commands are compatible with your installed versions of Redis and PostgreSQL.

After setting up the playbook and Jinja2 template, run the playbook against your servers to deploy the custom logrotate configuration. Monitor the log directories to ensure logs are being rotated as expected and services continue to operate without interruption.

For managing Rails application log files with logrotate, you can customize the logrotate configuration to include rules specific to your Rails logs. Rails applications  log to one or more files in the `log` directory within the application root, such as `production.log`, `development.log`, etc. You'll want to ensure these logs are rotated regularly to prevent them from consuming too much disk space, while also preserving enough historical log data for troubleshooting.

Here's how you can adjust the `custom_logrotate.conf.j2` template to include a section for Rails log rotation:

### Adding Rails Log Rotation to the Template

Modify your `custom_logrotate.conf.j2` Jinja2 template to include a section for Rails logs. Assuming your Rails application logs are located in `/path/to/your/rails_app/log/*.log`, you can add the following:

```jinja
# Rails application logs
/path/to/your/rails_app/log/*.log {
    weekly
    missingok
    rotate 5
    compress
    delaycompress
    notifempty
    create 0664 {{ rails_user }} {{ rails_group }}
    su {{ rails_user }} {{ rails_group }}
    postrotate
        if pgrep -f 'puma|unicorn|passenger' > /dev/null; then
            # Use this for Puma, adjust for Unicorn/Passenger if needed
            kill -USR1 "$(cat /path/to/your/puma/pid/file.pid)"
        fi
    endscript
}
```

- **Path Adjustment**: Replace `/path/to/your/rails_app/log/*.log` with the  path to your Rails application's log directory.
- **User and Group**: Replace `{{ rails_user }}` and `{{ rails_group }}` with the user and group that your Rails application runs as. This ensures that logrotate has the proper permissions to create and manage the log files.
- **Rotation Policy**: This example rotates logs weekly, keeps 5 old log files, compresses old versions, and ensures the log files are created with the correct permissions if a new one needs to be started.
- **Postrotate Script**: The `postrotate` script is crucial for gracefully reloading the application or web server (e.g., Puma, Unicorn, Passenger) to ensure it starts writing to the newly rotated log file. The example shown sends the `USR1` signal to Puma, which is one way to achieve log rotation without restarting the server. Adjust the signal and process identification method according to your specific application server and setup.

### Note:

- **Signal Handling**: Ensure your application server is configured to handle the signal sent in the `postrotate` script correctly. For Puma, `USR1` is used by default to rotate logs, but this may vary between application servers and configurations.
- **Process Identification**: The `pgrep -f` command is used to find the process ID of your application server (Puma, in the example). You may need to adjust the pattern to match your server process name or use a different method to identify the correct PID for signaling.

After updating the template, re-run your Ansible playbook to apply the new logrotate configuration. It's a good practice to manually run `logrotate` with the `-d` (debug) option to verify your configuration without ly rotating the logs, ensuring everything is set up as expected before it goes into effect automatically.
