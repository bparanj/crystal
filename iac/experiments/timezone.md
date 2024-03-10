When setting up a server that will serve customers across different timezones, it's common to configure the server's timezone to Coordinated Universal Time (UTC). Using UTC helps avoid confusion that can arise from daylight saving time changes and timezone differences. It provides a standard reference point and makes it easier to convert to local times as needed in your application or when parsing logs.

For many applications, especially web applications, the server-side operations (like logging, scheduling, and internal timestamps) are handled in UTC, while the presentation layer converts these times into the local time of the viewer. This separation of concerns allows your application to serve users around the world without having to manage a complex web of timezones on the server side.

If you're configuring a Linux server, you can set the timezone to UTC like this:

1. **Check the current timezone**:

   ```bash
   timedatectl
   ```

2. **List available timezones** (optional):

   ```bash
   timedatectl list-timezones
   ```

3. **Set the timezone to UTC**:
   ```bash
   sudo timedatectl set-timezone UTC
   ```

This command will change the system timezone without the need for a system restart. It's a straightforward way to ensure that your server operates on a universal clock, which can simplify time-related operations, especially when dealing with international customers.

## Ansible Playbook

To set the timezone of a server to UTC using Ansible, you can create a playbook like the following. This playbook ensures that the timezone is set to UTC across all managed nodes.

```yaml
---
- name: Set server timezone to UTC
  hosts: all
  become: true
  tasks:
    - name: Set timezone to UTC
      ansible.builtin.timezone:
        name: UTC
```

**Explanation**:

- `hosts: all`: Specifies that the playbook should run on all hosts in your inventory.
- `become: true`: Indicates that tasks should be executed with privilege escalation (sudo) to ensure you have the permissions needed to change system settings.
- `ansible.builtin.timezone`: Uses the `timezone` module to manage the timezone setting of the host. Setting `name: UTC` configures the timezone to UTC.

Before running this playbook, ensure you have an inventory file (`hosts`) defined, or specify the hosts directly in the command line. Save this playbook to a file, for example, `set-timezone.yml`, and run it with the `ansible-playbook` command:

```bash
ansible-playbook -i /path/to/your/inventory set-timezone.yml
```

Make sure to replace `/path/to/your/inventory` with the actual path to your Ansible inventory file.
