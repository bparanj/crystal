To install the latest version of PostgreSQL, version 16, through an Ansible playbook, you might need to add the PostgreSQL official repository to your system before installing it. This ensures you get the latest version directly from PostgreSQL rather than the default version available in your distribution's package repository.

Here's an updated playbook that includes tasks for adding the PostgreSQL Global Development Group (PGDG) repository, which provides the latest PostgreSQL versions, and then installs PostgreSQL 16:

```yaml
---
- name: Install PostgreSQL 16
  hosts: all
  become: true
  tasks:
    - name: Install prerequisites
      ansible.builtin.apt:
        name:
          - ca-certificates
          - wget
        state: present
        update_cache: yes

    - name: Add the PostgreSQL GPG key
      ansible.builtin.apt_key:
        url: https://www.postgresql.org/media/keys/ACCC4CF8.asc
        state: present

    - name: Add PostgreSQL 16 repository
      ansible.builtin.apt_repository:
        repo: deb http://apt.postgresql.org/pub/repos/apt/ {{ ansible_distribution_release }}-pgdg main
        state: present
        update_cache: yes

    - name: Install PostgreSQL 16
      ansible.builtin.apt:
        name: 
          - postgresql-16
          - postgresql-client-16
        state: present
```

This playbook performs the following steps:
1. **Install prerequisites**: Ensures that `ca-certificates` and `wget` are installed which are necessary for fetching and adding the GPG key.
2. **Add the PostgreSQL GPG key**: This key is used to verify the integrity of the packages.
3. **Add PostgreSQL 16 repository**: Adds the official PostgreSQL repository for version 16. Make sure to replace `{{ ansible_distribution_release }}` with your Ubuntu version codename (e.g., `focal`, `bionic`) if your Ansible version does not support the `ansible_distribution_release` variable.
4. **Install PostgreSQL 16**: Installs the PostgreSQL server and client version 16.

After adding a new repository, it's good practice to update the cache (`update_cache: yes`), so your system recognizes the new packages available. This playbook ensures that the latest version of PostgreSQL available from the PGDG repository is installed.

Here's the corrected Ansible playbook with adjustments for installing PostgreSQL 16 and ensuring it configures the correct version's configuration files:

```yaml
- name: Install PostgreSQL 16 on Ubuntu 22.04
  hosts: all
  become: true  # Use sudo
  vars:
    ansible_python_interpreter: /usr/bin/python3

  tasks:
    - name: Install prerequisites
      ansible.builtin.apt:
        name:
          - ca-certificates
          - wget
        state: present
        update_cache: yes

    - name: Add the PostgreSQL GPG key
      ansible.builtin.apt_key:
        url: https://www.postgresql.org/media/keys/ACCC4CF8.asc
        state: present

    - name: Add PostgreSQL 16 repository
      ansible.builtin.apt_repository:
        repo: deb http://apt.postgresql.org/pub/repos/apt/ {{ ansible_distribution_release }}-pgdg main
        state: present
        update_cache: yes

    - name: Install PostgreSQL 16
      ansible.builtin.apt:
        name: 
          - postgresql-16
          - postgresql-client-16
        state: present

    - name: Ensure PostgreSQL is running and enabled on boot
      ansible.builtin.service:
        name: postgresql
        state: started
        enabled: yes

    - name: Configure PostgreSQL to listen on localhost only
      ansible.builtin.lineinfile:
        path: /etc/postgresql/16/main/postgresql.conf  # Updated to version 16
        regexp: '^#?listen_addresses\s*='
        line: "listen_addresses = 'localhost'"
        state: present
      notify: restart postgresql

    - name: Restrict connections to local machine
      ansible.builtin.lineinfile:
        path: /etc/postgresql/16/main/pg_hba.conf  # Updated to version 16
        regexp: '^local\s+all\s+all\s+peer$'
        line: "local   all             all                                     peer"
        state: present
      notify: restart postgresql

    - name: Ensure libpq-dev is installed (Ubuntu/Debian)
      ansible.builtin.apt:
        name: libpq-dev
        state: present

    - name: Install psycopg2-binary using pip3  # Required for postgresql modules
      ansible.builtin.pip:
        name: psycopg2-binary
        state: present

    - name: Create temporary database user with a password
      ansible.builtin.postgresql_user:
        login_user: postgres
        name: dbtester
        password: "password"
        state: present
      become: true
      become_user: postgres

  handlers:
    - name: restart postgresql
      ansible.builtin.service:
        name: postgresql
        state: restarted
        enabled: yes
```

This playbook includes the necessary changes to target PostgreSQL version 16 specifically, ensuring the correct paths are used for configuration files in the `lineinfile` tasks.
