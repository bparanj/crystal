## Puma Service for Rack App

To create a systemd service file for Puma and start it using Ansible, you can use the `ansible.builtin.template` module to generate the service file dynamically and then use the `ansible.builtin.systemd` module to enable and start the service. Here's how you could structure your playbook:

### Step 1: Create a Template for the Service File

First, create a template file for your systemd service. Let's call it `puma.service.j2` and save it in your Ansible project's `templates` directory. The `.j2` extension indicates it's a Jinja2 template, which Ansible uses for templating.

```ini
[Unit]
Description=Puma HTTP Server
After=network.target

[Service]
Type=simple
User={{ app_user }}
WorkingDirectory={{ project_directory }}
ExecStart={{ bundle_path }} exec puma
Restart=always

[Install]
WantedBy=multi-user.target
```

In this template, `{{ app_user }}`, `{{ project_directory }}`, and `{{ bundle_path }}` are variables that will be replaced with actual values when the template is processed by Ansible.

### Step 2: Create the Ansible Playbook

Next, create an Ansible playbook to deploy the template and manage the Puma service. Here's an example playbook:

```yaml
---
- name: Configure and start Puma systemd service
  hosts: your_target_hosts
  become: yes
  vars:
    app_user: "your_app_user" # Replace with the actual user name
    project_directory: "/path/to/your/app" # Replace with the actual directory path
    bundle_path: "/path/to/bundle" # Replace with the actual bundle executable path

  tasks:
    - name: Deploy Puma systemd service file
      ansible.builtin.template:
        src: puma.service.j2
        dest: /etc/systemd/system/puma.service
        owner: root
        group: root
        mode: "0644"

    - name: Reload systemd to recognize the new service
      ansible.builtin.systemd:
        daemon_reload: yes

    - name: Enable and start Puma service
      ansible.builtin.systemd:
        name: puma
        enabled: yes
        state: started
```

This playbook performs the following actions:

1. **Deploy Puma systemd service file**: It uses the `template` module to create the service file from the `puma.service.j2` template, placing the result in `/etc/systemd/system/puma.service`.

2. **Reload systemd**: This step is necessary for systemd to recognize the newly added service file.

3. **Enable and start Puma service**: Finally, it ensures the Puma service is enabled to start on boot and starts it immediately.

### Notes:

- Make sure to replace `your_target_hosts`, `your_app_user`, `/path/to/your/app`, and `/path/to/bundle` with the appropriate values for your environment.
- The path to `bundle` can vary depending on how Ruby is installed (e.g., if using rbenv, rvm, or system Ruby). You might need to specify the full path to the `bundle` executable.
- This playbook requires `become: yes` to grant Ansible permissions to perform actions that require root privileges, like creating service files under `/etc/systemd/system` and managing systemd services.

After creating the playbook and the Jinja2 template, run the playbook with `ansible-playbook your_playbook_name.yml`, replacing `your_playbook_name.yml` with the name of your playbook file.
