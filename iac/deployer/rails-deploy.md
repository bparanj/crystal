Ansible playbook template to deploy code to an Ubuntu server, restart the Puma application server, run `bundle install`, and execute Rails database creation and migration commands for a production environment. This example assumes you have SSH access and the necessary permissions to execute commands on the target server.

```yaml
---
- name: Deploy Rails application to Ubuntu server
  hosts: your_server_group
  become: true

  vars:
    deploy_to: /path/to/your/app
    repo_url: git@your.repository.url:your_repo.git
    branch_name: master

  tasks:
    - name: Ensure git is installed
      apt:
        name: git
        state: present
        update_cache: yes

    - name: Clone repository
      git:
        repo: "{{ repo_url }}"
        dest: "{{ deploy_to }}"
        version: "{{ branch_name }}"
        force: yes
      become_user: your_deploy_user

    - name: Run bundle install
      bundler:
        state: present
        chdir: "{{ deploy_to }}"
      environment:
        RAILS_ENV: production

    - name: Create the database if it does not exist
      command: rails db:create RAILS_ENV=production
      args:
        chdir: "{{ deploy_to }}"
      environment:
        RAILS_ENV: production

    - name: Run database migrations
      command: rails db:migrate RAILS_ENV=production
      args:
        chdir: "{{ deploy_to }}"
      environment:
        RAILS_ENV: production

    - name: Ensure puma is installed
      gem:
        name: puma
        state: present
        user_install: no

    - name: Restart Puma
      systemd:
        name: puma@your_app
        state: restarted
        enabled: yes
        daemon_reload: yes
```

Please replace `your_server_group`, `/path/to/your/app`, `git@your.repository.url:your_repo.git`, `master`, and `your_deploy_user` with your actual server group, application directory path, repository URL, branch name, and deploy user, respectively. Also, adjust the `puma@your_app` service name according to your configuration.

This playbook performs the following actions:

1. Ensures git is installed on the target server.
2. Clones the specified repository into the given directory.
3. Runs `bundle install` to install the necessary Ruby gems.
4. Creates the Rails database if it doesn't already exist (be cautious with this in production).
5. Executes database migrations.
6. Ensures the Puma gem is installed.
7. Restarts the Puma application server using systemd.

**Important considerations:**

- This playbook assumes that you have a Puma systemd service set up. The service name `puma@your_app` might need to be adjusted based on your configuration.
- You might need to adjust the `become_user` for tasks where permissions matter, such as cloning the repository or running bundle install.
- Ensure you have all necessary environment variables (like database credentials) configured either in your application's environment, through the systemd service file for Puma, or by passing them through the `environment` parameter in the playbook tasks.

## Iteration #2

To deploy your Rails project directly from your local machine to a server, you can use Ansible's `synchronize` module, which wraps `rsync` to efficiently transfer files. The playbook below assumes your Rails project is in the current working directory from where you run the Ansible command, and it will upload the project to your Ubuntu server.

Please adjust the placeholders (`your_server_group`, `/path/to/your/app/on/server`, `your_deploy_user`, etc.) to match your actual deployment setup. This playbook includes tasks to copy your code, run `bundle install`, and handle database creation and migration, along with restarting the Puma server.

```yaml
---
- name: Deploy Rails application from local machine to server
  hosts: your_server_group
  become: true

  vars:
    local_project_path: "{{ playbook_dir }}"
    remote_deploy_path: /path/to/your/app/on/server
    rails_env: production

  tasks:
    - name: Synchronize project files from local to remote
      ansible.builtin.synchronize:
        src: "{{ local_project_path }}/"
        dest: "{{ remote_deploy_path }}"
        delete: yes # Careful with this in production environments
        recursive: yes
      delegate_to: localhost

    - name: Bundle install
      bundler:
        state: present
        chdir: "{{ remote_deploy_path }}"
        without: development test
      environment:
        RAILS_ENV: "{{ rails_env }}"

    - name: Run Rails db:create and db:migrate
      command: "{{ item }}"
      args:
        chdir: "{{ remote_deploy_path }}"
      loop:
        - bundle exec rails db:create RAILS_ENV={{ rails_env }}
        - bundle exec rails db:migrate RAILS_ENV={{ rails_env }}
      environment:
        RAILS_ENV: "{{ rails_env }}"

    - name: Restart Puma
      systemd:
        name: puma@your_app # Adjust to your specific Puma service name
        state: restarted
        enabled: yes
        daemon_reload: yes
```

**Key points:**

- Ensure `rsync` is installed on your local machine and the target server.
- This playbook uses `delegate_to: localhost` for the `synchronize` task to initiate the file transfer from your local machine.
- The `delete: yes` option in the `synchronize` task will make the remote directory mirror the local one, which means files not present locally will be deleted on the server. Be cautious with this setting, especially in production.
- Update the Puma service name (`puma@your_app`) to match your configuration.
- Ensure all necessary environment variables are properly set for Rails and database connectivity.

Replace placeholder values with your actual configuration details before running the playbook.
