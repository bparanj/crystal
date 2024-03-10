## How to Install PostgreSQL on Ubuntu 22.04 with Ansible

This will install PostgreSQL that is part of the Ubuntu package and is not the latest version on an Ubuntu 22.04 server using Ansible.

Below is an Ansible playbook example that installs PostgreSQL on an Ubuntu 22.04 server. This playbook performs the following steps:

1. **Updates the apt cache**: This is often required to ensure you have the latest listings of available packages.
2. **Installs PostgreSQL**: This step installs the PostgreSQL package.
3. **Ensures PostgreSQL is running**: It ensures that the PostgreSQL service is started and enabled to run at boot.

```yaml
---
- name: Install PostgreSQL on Ubuntu 22.04
  hosts: your_host_group
  become: yes # Use sudo
  tasks:
    - name: Update apt cache
      ansible.builtin.apt:
        update_cache: yes
        cache_valid_time: 3600 # Optional: Cache valid for 1 hour to avoid unnecessary updates

    - name: Install PostgreSQL
      ansible.builtin.apt:
        name: postgresql
        state: present

    - name: Ensure PostgreSQL is running and enabled on boot
      ansible.builtin.service:
        name: postgresql
        state: started
        enabled: yes
```

Before running this playbook, ensure you've done the following:

- Replace `your_host_group` with the name of the group in your Ansible inventory that contains the Ubuntu 22.04 servers where you want PostgreSQL installed. Alternatively, you can specify a single host.
- Have Ansible installed on your control machine.
- Have SSH access configured to the target machine(s) for the Ansible control machine.
- The target machine(s) should be running Ubuntu 22.04.

To run the playbook, save it to a file (e.g., `install_postgresql.yml`) and then execute it with the `ansible-playbook` command, like so:

```sh
ansible-playbook install_postgresql.yml
```

This playbook provides a basic setup. Depending on your requirements, you might want to configure PostgreSQL further, such as setting up databases, users, or adjusting authentication methods and connection settings. These tasks can also be automated with Ansible using additional modules like `postgresql_db`, `postgresql_user`, and custom SQL scripts.
