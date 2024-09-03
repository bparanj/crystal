Here's an Ansible playbook that sets up Caddy as a reverse proxy, directing requests to the `/check` endpoint to `localhost:9292` and the rest of the requests to `localhost:3000`:

```yaml
---
- hosts: all
  become: yes

  tasks:
    - name: Install Caddy
      apt:
        name: caddy
        state: present

    - name: Create Caddyfile
      copy:
        dest: /etc/caddy/Caddyfile
        content: |
          :80 {
              route /check/* {
                  reverse_proxy localhost:9292
              }

              route /* {
                  reverse_proxy localhost:3000
              }
          }

    - name: Restart Caddy
      systemd:
        name: caddy
        state: restarted
```

Here's a breakdown of the playbook:

1. The playbook targets all hosts specified in the inventory.

2. The `become: yes` directive ensures that the tasks are executed with administrative privileges (sudo).

3. The first task installs Caddy using the `apt` module. It ensures that Caddy is present on the system.

4. The second task creates the Caddyfile configuration using the `copy` module. The Caddyfile is created at `/etc/caddy/Caddyfile` with the following content:
   - The server listens on port 80 (`:80`).
   - The `route` directive is used to define the routing rules.
   - The first `route` block matches requests starting with `/check/*` and proxies them to `localhost:9292`.
   - The second `route` block matches all other requests (`/*`) and proxies them to `localhost:3000`.

5. The third task restarts the Caddy service using the `systemd` module to apply the new configuration.

To use this playbook, save it to a file (e.g., `caddy-reverse-proxy.yml`) and run it using the `ansible-playbook` command:

```
ansible-playbook -i inventory.ini caddy-reverse-proxy.yml
```

Make sure to replace `inventory.ini` with the path to your Ansible inventory file that specifies the target hosts.

After running the playbook, Caddy will be installed and configured as a reverse proxy. Requests to the `/check` endpoint will be proxied to `localhost:9292`, while all other requests will be proxied to `localhost:3000`.

This playbook assumes that you are using a Debian-based system (e.g., Ubuntu) and that the services running on `localhost:9292` and `localhost:3000` are already set up and accessible. Adjust the playbook according to your specific requirements and environment.
