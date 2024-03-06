To create an Ansible playbook that sets up a Message of the Day (MOTD) with your specified message on a Linux server, you can use the `ansible.builtin.copy` or `ansible.builtin.template` module. The `copy` module is straightforward for static messages, but if you ever want to include dynamic information (like the hostname or IP address), you might prefer the `template` module. Here, I'll show you how to use the `copy` module for simplicity.

### Playbook: setup_motd.yml

```yaml
---
- name: Configure MOTD
  hosts: all
  become: true
  vars:
    motd_message: |
      -----------------------------------------------------------------------------------------------------
      This server is managed by ZeroTouch. Do not manually configure or install anything on this server.
      You can view the log files and inspect process status or anything that does not modify this server.
      -----------------------------------------------------------------------------------------------------

  tasks:
    - name: Set MOTD message
      ansible.builtin.copy:
        dest: /etc/motd
        content: "{{ motd_message }}"
        owner: root
        group: root
        mode: '0644'
```

### Explanation:

- **`hosts: all`**: Targets all hosts in your inventory.
- **`become: true`**: Ensures the task is run with elevated privileges (as root), which is necessary to write to `/etc/motd`.
- **`vars`**: Defines the message to be set as MOTD.
- **`ansible.builtin.copy`**: The task uses this module to create or overwrite the `/etc/motd` file with the content specified in `motd_message`. The `owner`, `group`, and `mode` parameters ensure the file has appropriate permissions.

### How to Run the Playbook:

1. Make sure you have Ansible installed on your local machine or wherever you intend to run the playbook from.
2. Save the playbook content to a file named `setup_motd.yml`.
3. Run the playbook against your target hosts. You'll need an inventory file or to specify your hosts when running the playbook. Here's a basic command to run the playbook:

```bash
ansible-playbook -i your_inventory_file setup_motd.yml
```

Replace `your_inventory_file` with the path to your inventory file. If you're targeting a specific host or group and have them defined in your default inventory, you could simplify the command to something like:

```bash
ansible-playbook setup_motd.yml
```

This will configure the MOTD for the servers specified in your inventory or command line, displaying the message to users upon login.
