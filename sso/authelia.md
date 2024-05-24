
Change the version to the latest: v4.38.8

Here's an Ansible playbook that installs Authelia, a single sign-on and two-factor authentication server:

```yaml
---
- name: Install Authelia
  hosts: all
  become: true

  vars:
    authelia_version: 4.36.6
    authelia_config_dir: /etc/authelia
    authelia_data_dir: /var/lib/authelia

  tasks:
    - name: Add Authelia APT repository
      apt_repository:
        repo: deb [arch=amd64] https://apt.authelia.com/ stable main
        state: present

    - name: Add Authelia APT repository key
      apt_key:
        url: https://apt.authelia.com/gpg.key
        state: present

    - name: Install Authelia
      apt:
        name: authelia={{ authelia_version }}
        state: present
        update_cache: yes

    - name: Create Authelia configuration directory
      file:
        path: "{{ authelia_config_dir }}"
        state: directory
        owner: root
        group: root
        mode: 0755

    - name: Create Authelia data directory
      file:
        path: "{{ authelia_data_dir }}"
        state: directory
        owner: authelia
        group: authelia
        mode: 0750

    - name: Copy Authelia configuration file
      template:
        src: authelia.yml.j2
        dest: "{{ authelia_config_dir }}/configuration.yml"
        owner: root
        group: root
        mode: 0640

    - name: Enable and start Authelia service
      service:
        name: authelia
        state: started
        enabled: yes
```

This playbook does the following:

1. It starts by specifying the hosts on which to run the playbook and sets `become` to `true` to run tasks with elevated privileges.

2. The `vars` section defines variables for the Authelia version, configuration directory, and data directory.

3. The first task adds the Authelia APT repository to the system.

4. The second task adds the Authelia APT repository key to ensure package authenticity.

5. The third task installs Authelia using the specified version from the APT repository.

6. The fourth task creates the Authelia configuration directory (`/etc/authelia`) with the appropriate permissions.

7. The fifth task creates the Authelia data directory (`/var/lib/authelia`) with the appropriate permissions and ownership.

8. The sixth task copies the Authelia configuration file from a Jinja2 template (`authelia.yml.j2`) to the configuration directory. You'll need to create this template file separately with your desired Authelia configuration.

9. The final task enables and starts the Authelia service.

To use this playbook, save it to a file (e.g., `install-authelia.yml`) and create the `authelia.yml.j2` template file with your Authelia configuration. Then, run the playbook using the `ansible-playbook` command:

```
ansible-playbook install-authelia.yml
```

Make sure you have Ansible installed and configured to connect to the target hosts before running the playbook.

This playbook assumes you are running it on a Debian-based system (such as Ubuntu) that uses APT for package management. If you are using a different operating system, you may need to modify the package installation tasks accordingly.

Authelia is an open-source authentication and authorization server providing 2-factor authentication and single sign-on (SSO) capabilities. Below is an Ansible playbook to install Authelia on an Ubuntu server. This playbook will also include the necessary dependencies and configuration steps.

### Ansible Playbook for Installing Authelia

**playbook.yml**:
```yaml
---
- name: Install Authelia
  hosts: all
  become: true

  vars:
    authelia_version: "4.31.1"
    authelia_user: "authelia"
    authelia_group: "authelia"
    authelia_install_dir: "/opt/authelia"
    authelia_config_dir: "/etc/authelia"
    authelia_config_file: "/etc/authelia/configuration.yml"
    authelia_data_dir: "/var/lib/authelia"
    authelia_log_dir: "/var/log/authelia"

  tasks:
    - name: Update apt cache
      apt:
        update_cache: yes

    - name: Install dependencies
      apt:
        name:
          - wget
          - tar
          - curl
          - ca-certificates
        state: present

    - name: Create authelia group
      group:
        name: "{{ authelia_group }}"
        state: present

    - name: Create authelia user
      user:
        name: "{{ authelia_user }}"
        group: "{{ authelia_group }}"
        create_home: false
        shell: /bin/false

    - name: Create necessary directories
      file:
        path: "{{ item }}"
        state: directory
        owner: "{{ authelia_user }}"
        group: "{{ authelia_group }}"
        mode: '0755'
      with_items:
        - "{{ authelia_install_dir }}"
        - "{{ authelia_config_dir }}"
        - "{{ authelia_data_dir }}"
        - "{{ authelia_log_dir }}"

    - name: Download Authelia
      get_url:
        url: "https://github.com/authelia/authelia/releases/download/v{{ authelia_version }}/authelia-linux-amd64.tar.gz"
        dest: "/tmp/authelia-linux-amd64.tar.gz"

    - name: Extract Authelia
      unarchive:
        src: "/tmp/authelia-linux-amd64.tar.gz"
        dest: "{{ authelia_install_dir }}"
        remote_src: yes
        creates: "{{ authelia_install_dir }}/authelia"

    - name: Create symbolic link
      file:
        src: "{{ authelia_install_dir }}/authelia"
        dest: "/usr/local/bin/authelia"
        state: link

    - name: Create Authelia configuration file
      copy:
        dest: "{{ authelia_config_file }}"
        content: |
          theme: light
          default_redirection_url: https://example.com
          jwt_secret: a_very_secret_key
          storage:
            local:
              path: "{{ authelia_data_dir }}/db.sqlite3"
          authentication_backend:
            file:
              path: "{{ authelia_config_dir }}/users.yml"
          access_control:
            default_policy: deny
            rules:
              - domain: "*.example.com"
                policy: bypass
          session:
            name: authelia_session
            secret: another_very_secret_key
            expiration: 3600
            inactivity: 300
            domain: example.com
          regulation:
            max_retries: 3
            find_time: 120
            ban_time: 300
          server:
            host: 0.0.0.0
            port: 9091
          logging:
            level: debug
            format: text
            file_path: "{{ authelia_log_dir }}/authelia.log"

    - name: Create users configuration file
      copy:
        dest: "{{ authelia_config_dir }}/users.yml"
        content: |
          users:
            john:
              password: password_hash_here
              displayname: John Doe
              email: john.doe@example.com

    - name: Set permissions for configuration files
      file:
        path: "{{ item }}"
        owner: "{{ authelia_user }}"
        group: "{{ authelia_group }}"
        mode: '0640'
      with_items:
        - "{{ authelia_config_file }}"
        - "{{ authelia_config_dir }}/users.yml"

    - name: Create systemd service file for Authelia
      copy:
        dest: /etc/systemd/system/authelia.service
        content: |
          [Unit]
          Description=Authelia authentication server
          After=network.target

          [Service]
          User={{ authelia_user }}
          Group={{ authelia_group }}
          ExecStart=/usr/local/bin/authelia --config {{ authelia_config_file }}
          Restart=always
          RestartSec=5s
          LimitNOFILE=4096

          [Install]
          WantedBy=multi-user.target

    - name: Reload systemd to apply changes
      systemd:
        daemon_reload: yes

    - name: Enable and start Authelia service
      systemd:
        name: authelia
        enabled: yes
        state: started
```

### Explanation
- **Update apt cache and install dependencies**: Ensures that the necessary packages are installed.
- **Create user and group**: Creates a dedicated user and group for running Authelia.
- **Download and extract Authelia**: Downloads the Authelia binary and extracts it to the designated directory.
- **Create configuration files**: Sets up the main configuration file and the user configuration file for Authelia.
- **Create systemd service**: Defines a systemd service for managing the Authelia process.
- **Start and enable the service**: Ensures that the Authelia service starts on boot and is currently running.

### Usage
1. **Clone the repository** or create a directory for your Ansible playbook and copy the provided playbook into a file named `playbook.yml`.
2. **Run the playbook** using Ansible:
   ```bash
   ansible-playbook -i <inventory_file> playbook.yml
   ```
   Replace `<inventory_file>` with your inventory file that contains the target server information.

### References
- [Authelia Documentation](https://www.authelia.com/docs/getting-started/)
- [Ansible Documentation](https://docs.ansible.com/ansible/latest/user_guide/intro_getting_started.html)
- [Systemd Service Documentation](https://www.freedesktop.org/software/systemd/man/systemd.service.html)

Great! To use Authelia with Caddy as the reverse proxy, you'll need to configure Caddy to integrate with Authelia for authentication. Here's an updated Ansible playbook that installs both Authelia and Caddy and sets up the necessary configuration:

```yaml
---
- name: Install Authelia and Caddy
  hosts: all
  become: true

  vars:
    authelia_version: 4.36.6
    authelia_config_dir: /etc/authelia
    authelia_data_dir: /var/lib/authelia
    caddy_version: 2.6.4
    caddy_config_dir: /etc/caddy
    caddy_data_dir: /var/lib/caddy

  tasks:
    - name: Add Authelia APT repository
      apt_repository:
        repo: deb [arch=amd64] https://apt.authelia.com/ stable main
        state: present

    - name: Add Authelia APT repository key
      apt_key:
        url: https://apt.authelia.com/gpg.key
        state: present

    - name: Install Authelia
      apt:
        name: authelia={{ authelia_version }}
        state: present
        update_cache: yes

    - name: Create Authelia configuration directory
      file:
        path: "{{ authelia_config_dir }}"
        state: directory
        owner: root
        group: root
        mode: 0755

    - name: Create Authelia data directory
      file:
        path: "{{ authelia_data_dir }}"
        state: directory
        owner: authelia
        group: authelia
        mode: 0750

    - name: Copy Authelia configuration file
      template:
        src: authelia.yml.j2
        dest: "{{ authelia_config_dir }}/configuration.yml"
        owner: root
        group: root
        mode: 0640

    - name: Download and install Caddy
      get_url:
        url: https://github.com/caddyserver/caddy/releases/download/v{{ caddy_version }}/caddy_{{ caddy_version }}_linux_amd64.deb
        dest: /tmp/caddy.deb
      register: caddy_download

    - name: Install Caddy
      apt:
        deb: /tmp/caddy.deb

    - name: Create Caddy configuration directory
      file:
        path: "{{ caddy_config_dir }}"
        state: directory
        owner: root
        group: root
        mode: 0755

    - name: Create Caddy data directory
      file:
        path: "{{ caddy_data_dir }}"
        state: directory
        owner: caddy
        group: caddy
        mode: 0750

    - name: Copy Caddy configuration file
      template:
        src: Caddyfile.j2
        dest: "{{ caddy_config_dir }}/Caddyfile"
        owner: root
        group: root
        mode: 0644

    - name: Enable and start Authelia service
      service:
        name: authelia
        state: started
        enabled: yes

    - name: Enable and start Caddy service
      service:
        name: caddy
        state: started
        enabled: yes
```

In this updated playbook:

1. We've added variables for Caddy, including the version, configuration directory, and data directory.

2. The tasks for installing Authelia remain the same as in the previous playbook.

3. We've added tasks to download and install Caddy using the official Caddy release package.

4. We create the Caddy configuration directory (`/etc/caddy`) and data directory (`/var/lib/caddy`) with the appropriate permissions.

5. We copy the Caddy configuration file from a Jinja2 template (`Caddyfile.j2`) to the configuration directory. You'll need to create this template file with your desired Caddy configuration, including the integration with Authelia for authentication.

6. Finally, we enable and start both the Authelia and Caddy services.

To use this playbook, save it to a file (e.g., `install-authelia-caddy.yml`) and create the `authelia.yml.j2` and `Caddyfile.j2` template files with your respective configurations.

For the `Caddyfile.j2` template, you'll need to configure Caddy to use Authelia for authentication. Here's an example configuration:

```
:80 {
  reverse_proxy localhost:9091
}

:443 {
  tls /etc/caddy/certs/example.com.crt /etc/caddy/certs/example.com.key
  reverse_proxy localhost:9091
}

authelia.example.com {
  reverse_proxy localhost:9091
}

protected.example.com {
  reverse_proxy localhost:8080
  authelia_auth authelia.example.com {
    authelia_url https://authelia.example.com
  }
}
```

In this example, Caddy is configured to:

- Listen on ports 80 and 443 and reverse proxy to Authelia (running on `localhost:9091`).
- Serve Authelia on `authelia.example.com`.
- Protect the `protected.example.com` domain with Authelia authentication by using the `authelia_auth` directive and specifying the Authelia URL.

Make sure to adjust the configuration according to your specific requirements, such as domain names, ports, and SSL/TLS certificate paths.

Once you have the playbook and template files ready, run the playbook using the `ansible-playbook` command:

```
ansible-playbook install-authelia-caddy.yml
```

This will install and configure Authelia and Caddy on the target hosts, allowing you to use Authelia for authentication with Caddy as the reverse proxy.

4.38.8

To set up Authelia with Caddy as the reverse proxy, you can use an Ansible playbook to install and configure both Authelia and Caddy. This playbook will install the necessary software, configure Caddy to use Authelia for authentication, and set up Authelia to handle authentication requests.

### Ansible Playbook

**playbook.yml**:
```yaml
---
- name: Install Authelia and Caddy
  hosts: all
  become: true

  vars:
    authelia_version: "4.31.1"
    authelia_user: "authelia"
    authelia_group: "authelia"
    authelia_install_dir: "/opt/authelia"
    authelia_config_dir: "/etc/authelia"
    authelia_config_file: "/etc/authelia/configuration.yml"
    authelia_data_dir: "/var/lib/authelia"
    authelia_log_dir: "/var/log/authelia"
    caddy_config_file: "/etc/caddy/Caddyfile"

  tasks:
    - name: Update apt cache
      apt:
        update_cache: yes

    - name: Install dependencies
      apt:
        name:
          - wget
          - tar
          - curl
          - ca-certificates
          - debian-keyring
          - debian-archive-keyring
          - apt-transport-https
        state: present

    - name: Add Caddy repository
      apt_repository:
        repo: "deb [trusted=yes] https://apt.fury.io/caddy/ /"
        state: present

    - name: Install Caddy
      apt:
        name: caddy
        state: present

    - name: Create authelia group
      group:
        name: "{{ authelia_group }}"
        state: present

    - name: Create authelia user
      user:
        name: "{{ authelia_user }}"
        group: "{{ authelia_group }}"
        create_home: false
        shell: /bin/false

    - name: Create necessary directories
      file:
        path: "{{ item }}"
        state: directory
        owner: "{{ authelia_user }}"
        group: "{{ authelia_group }}"
        mode: '0755'
      with_items:
        - "{{ authelia_install_dir }}"
        - "{{ authelia_config_dir }}"
        - "{{ authelia_data_dir }}"
        - "{{ authelia_log_dir }}"

    - name: Download Authelia
      get_url:
        url: "https://github.com/authelia/authelia/releases/download/v{{ authelia_version }}/authelia-linux-amd64.tar.gz"
        dest: "/tmp/authelia-linux-amd64.tar.gz"

    - name: Extract Authelia
      unarchive:
        src: "/tmp/authelia-linux-amd64.tar.gz"
        dest: "{{ authelia_install_dir }}"
        remote_src: yes
        creates: "{{ authelia_install_dir }}/authelia"

    - name: Create symbolic link
      file:
        src: "{{ authelia_install_dir }}/authelia"
        dest: "/usr/local/bin/authelia"
        state: link

    - name: Create Authelia configuration file
      copy:
        dest: "{{ authelia_config_file }}"
        content: |
          theme: light
          default_redirection_url: https://example.com
          jwt_secret: a_very_secret_key
          storage:
            local:
              path: "{{ authelia_data_dir }}/db.sqlite3"
          authentication_backend:
            file:
              path: "{{ authelia_config_dir }}/users.yml"
          access_control:
            default_policy: deny
            rules:
              - domain: "*.example.com"
                policy: bypass
          session:
            name: authelia_session
            secret: another_very_secret_key
            expiration: 3600
            inactivity: 300
            domain: example.com
          regulation:
            max_retries: 3
            find_time: 120
            ban_time: 300
          server:
            host: 0.0.0.0
            port: 9091
          logging:
            level: debug
            format: text
            file_path: "{{ authelia_log_dir }}/authelia.log"

    - name: Create users configuration file
      copy:
        dest: "{{ authelia_config_dir }}/users.yml"
        content: |
          users:
            john:
              password: password_hash_here
              displayname: John Doe
              email: john.doe@example.com

    - name: Set permissions for configuration files
      file:
        path: "{{ item }}"
        owner: "{{ authelia_user }}"
        group: "{{ authelia_group }}"
        mode: '0640'
      with_items:
        - "{{ authelia_config_file }}"
        - "{{ authelia_config_dir }}/users.yml"

    - name: Create systemd service file for Authelia
      copy:
        dest: /etc/systemd/system/authelia.service
        content: |
          [Unit]
          Description=Authelia authentication server
          After=network.target

          [Service]
          User={{ authelia_user }}
          Group={{ authelia_group }}
          ExecStart=/usr/local/bin/authelia --config {{ authelia_config_file }}
          Restart=always
          RestartSec=5s
          LimitNOFILE=4096

          [Install]
          WantedBy=multi-user.target

    - name: Reload systemd to apply changes
      systemd:
        daemon_reload: yes

    - name: Enable and start Authelia service
      systemd:
        name: authelia
        enabled: yes
        state: started

    - name: Configure Caddy for Authelia
      copy:
        dest: "{{ caddy_config_file }}"
        content: |
          {
            email you@example.com
          }

          example.com {
            reverse_proxy /authelia/* 127.0.0.1:9091
            reverse_proxy /* 127.0.0.1:8080 {
              header_up X-Forwarded-User {http.auth.user.email}
              header_up X-Forwarded-Groups {http.auth.user.groups}
            }
            authenticate / {
              forward_auth authelia:9091 {
                uri /api/verify?rd=https://example.com/
                copy_headers X-Forwarded-*
                trust_forward_headers
              }
              inject headers {
                Cookie "authelia_session"
              }
            }
          }

    - name: Restart Caddy to apply changes
      systemd:
        name: caddy
        state: restarted
```

### Explanation

1. **Update apt cache and install dependencies**: Ensures that necessary packages are installed.
2. **Add Caddy repository and install Caddy**: Adds the official Caddy repository and installs Caddy.
3. **Create user and group for Authelia**: Creates a dedicated user and group for running Authelia.
4. **Download and extract Authelia**: Downloads the Authelia binary and extracts it to the designated directory.
5. **Create configuration files**: Sets up the main configuration file and the user configuration file for Authelia.
6. **Create systemd service for Authelia**: Defines a systemd service for managing the Authelia process.
7. **Configure Caddy**: Sets up Caddy to use Authelia for authentication by modifying the Caddyfile.
8. **Restart Caddy**: Restarts Caddy to apply the new configuration.

### Usage

1. **Clone the repository** or create a directory for your Ansible playbook and copy the provided playbook into a file named `playbook.yml`.
2. **Run the playbook** using Ansible:
   ```bash
   ansible-playbook -i <inventory_file> playbook.yml
   ```
   Replace `<inventory_file>` with your inventory file that contains the target server information.

### References

- [Authelia Documentation](https://www.authelia.com/docs/getting-started/)
- [Caddy Documentation](https://caddyserver.com/docs/)
- [Ansible Documentation](https://docs.ansible.com/ansible/latest/user_guide/intro_getting_started.html)
- [Systemd Service Documentation](https://www.freedesktop.org/software/systemd/man/systemd.service.html)

By following these steps, you will have Authelia and Caddy installed and configured on your server, with Caddy acting as a reverse proxy that uses Authelia for authentication.

Here is an updated Ansible playbook to install Authelia version 4.38.8 with Caddy as the reverse proxy on an Ubuntu server.

### Ansible Playbook

**playbook.yml**:
```yaml
---
- name: Install Authelia and Caddy
  hosts: all
  become: true

  vars:
    authelia_version: "4.38.8"
    authelia_user: "authelia"
    authelia_group: "authelia"
    authelia_install_dir: "/opt/authelia"
    authelia_config_dir: "/etc/authelia"
    authelia_config_file: "/etc/authelia/configuration.yml"
    authelia_data_dir: "/var/lib/authelia"
    authelia_log_dir: "/var/log/authelia"
    caddy_config_file: "/etc/caddy/Caddyfile"

  tasks:
    - name: Update apt cache
      apt:
        update_cache: yes

    - name: Install dependencies
      apt:
        name:
          - wget
          - tar
          - curl
          - ca-certificates
          - debian-keyring
          - debian-archive-keyring
          - apt-transport-https
        state: present

    - name: Add Caddy repository
      apt_repository:
        repo: "deb [trusted=yes] https://apt.fury.io/caddy/ /"
        state: present

    - name: Install Caddy
      apt:
        name: caddy
        state: present

    - name: Create authelia group
      group:
        name: "{{ authelia_group }}"
        state: present

    - name: Create authelia user
      user:
        name: "{{ authelia_user }}"
        group: "{{ authelia_group }}"
        create_home: false
        shell: /bin/false

    - name: Create necessary directories
      file:
        path: "{{ item }}"
        state: directory
        owner: "{{ authelia_user }}"
        group: "{{ authelia_group }}"
        mode: '0755'
      with_items:
        - "{{ authelia_install_dir }}"
        - "{{ authelia_config_dir }}"
        - "{{ authelia_data_dir }}"
        - "{{ authelia_log_dir }}"

    - name: Download Authelia
      get_url:
        url: "https://github.com/authelia/authelia/releases/download/v{{ authelia_version }}/authelia-linux-amd64.tar.gz"
        dest: "/tmp/authelia-linux-amd64.tar.gz"

    - name: Extract Authelia
      unarchive:
        src: "/tmp/authelia-linux-amd64.tar.gz"
        dest: "{{ authelia_install_dir }}"
        remote_src: yes
        creates: "{{ authelia_install_dir }}/authelia"

    - name: Create symbolic link
      file:
        src: "{{ authelia_install_dir }}/authelia"
        dest: "/usr/local/bin/authelia"
        state: link

    - name: Create Authelia configuration file
      copy:
        dest: "{{ authelia_config_file }}"
        content: |
          theme: light
          default_redirection_url: https://example.com
          jwt_secret: a_very_secret_key
          storage:
            local:
              path: "{{ authelia_data_dir }}/db.sqlite3"
          authentication_backend:
            file:
              path: "{{ authelia_config_dir }}/users.yml"
          access_control:
            default_policy: deny
            rules:
              - domain: "*.example.com"
                policy: bypass
          session:
            name: authelia_session
            secret: another_very_secret_key
            expiration: 3600
            inactivity: 300
            domain: example.com
          regulation:
            max_retries: 3
            find_time: 120
            ban_time: 300
          server:
            host: 0.0.0.0
            port: 9091
          logging:
            level: debug
            format: text
            file_path: "{{ authelia_log_dir }}/authelia.log"

    - name: Create users configuration file
      copy:
        dest: "{{ authelia_config_dir }}/users.yml"
        content: |
          users:
            john:
              password: password_hash_here
              displayname: John Doe
              email: john.doe@example.com

    - name: Set permissions for configuration files
      file:
        path: "{{ item }}"
        owner: "{{ authelia_user }}"
        group: "{{ authelia_group }}"
        mode: '0640'
      with_items:
        - "{{ authelia_config_file }}"
        - "{{ authelia_config_dir }}/users.yml"

    - name: Create systemd service file for Authelia
      copy:
        dest: /etc/systemd/system/authelia.service
        content: |
          [Unit]
          Description=Authelia authentication server
          After=network.target

          [Service]
          User={{ authelia_user }}
          Group={{ authelia_group }}
          ExecStart=/usr/local/bin/authelia --config {{ authelia_config_file }}
          Restart=always
          RestartSec=5s
          LimitNOFILE=4096

          [Install]
          WantedBy=multi-user.target

    - name: Reload systemd to apply changes
      systemd:
        daemon_reload: yes

    - name: Enable and start Authelia service
      systemd:
        name: authelia
        enabled: yes
        state: started

    - name: Configure Caddy for Authelia
      copy:
        dest: "{{ caddy_config_file }}"
        content: |
          {
            email you@example.com
          }

          example.com {
            reverse_proxy /authelia/* 127.0.0.1:9091
            reverse_proxy /* 127.0.0.1:8080 {
              header_up X-Forwarded-User {http.auth.user.email}
              header_up X-Forwarded-Groups {http.auth.user.groups}
            }
            authenticate / {
              forward_auth authelia:9091 {
                uri /api/verify?rd=https://example.com/
                copy_headers X-Forwarded-*
                trust_forward_headers
              }
              inject headers {
                Cookie "authelia_session"
              }
            }
          }

    - name: Restart Caddy to apply changes
      systemd:
        name: caddy
        state: restarted
```

### Explanation

1. **Update apt cache and install dependencies**: Ensures that necessary packages are installed.
2. **Add Caddy repository and install Caddy**: Adds the official Caddy repository and installs Caddy.
3. **Create user and group for Authelia**: Creates a dedicated user and group for running Authelia.
4. **Download and extract Authelia**: Downloads the Authelia binary and extracts it to the designated directory.
5. **Create configuration files**: Sets up the main configuration file and the user configuration file for Authelia.
6. **Create systemd service for Authelia**: Defines a systemd service for managing the Authelia process.
7. **Configure Caddy**: Sets up Caddy to use Authelia for authentication by modifying the Caddyfile.
8. **Restart Caddy**: Restarts Caddy to apply the new configuration.

### Usage

1. **Clone the repository** or create a directory for your Ansible playbook and copy the provided playbook into a file named `playbook.yml`.
2. **Run the playbook** using Ansible:
   ```bash
   ansible-playbook -i <inventory_file> playbook.yml
   ```
   Replace `<inventory_file>` with your inventory file that contains the target server information.

### References

- [Authelia Documentation](https://www.authelia.com/docs/getting-started/)
- [Caddy Documentation](https://caddyserver.com/docs/)
- [Ansible Documentation](https://docs.ansible.com/ansible/latest/user_guide/intro_getting_started.html)
- [Systemd Service Documentation](https://www.freedesktop.org/software/systemd/man/systemd.service.html)

By following these steps, you will have Authelia version 4.38.8 and Caddy installed and configured on your server, with Caddy acting as a reverse proxy that uses Authelia for authentication.
