1) Create on the remote server `deploy` user:

```bash
# on the server, as a root user

$ adduser deploy
$ adduser deploy sudo
```

2) Make sure that you can login to the server with deploy user without a password entry:

> It assumes that you have ssh keypair already (`~/.ssh/id_rsa` and `~/.ssh/id_rsa.pub`) on your desktop.

```bash
# on the desktop

$ ssh-add
$ ssh-copy-id deploy@deploy_server_ip

# Now try to login to the server as deploy user:
$ ssh deploy@deploy_server_ip
```

> If it didn't work, and you get message like `Permission denied (publickey)`, it seems like password authentication disabled by default on your server (which is a good thing actually). Login to the server as a `root` again, then login to `deploy` user (`$ su - deploy`) and add your .pub key to the deploy's `~/.ssh/authorized_keys` file: `mkdir -p ~/.ssh && chmod 700 ~/.ssh`, `echo your_public_key_string_value >> ~/.ssh/authorized_keys && chmod 644 ~/.ssh/authorized_keys`. If all went fine, you should login without password (`$ ssh deploy@deploy_server_ip`).


3) Now it's time for Ansible magic!

> you need ansible to be intalled on your desktop machine: `sudo apt install ansible` or `brew install ansible`.

```
$ ansible-playbook config/provision.yml -i 'deploy_server_ip,' -u deploy --ask-become-pass
```

---

**Bonus: disable password login authentication**

> What for:

> Some VPS providers don't have an option to allow provide a custom public SSH key for the root user's authentication while creating a new VPS server. In this case, you'll get automatically generated password (for root user) after VPS will be created, which then can be used to login to the server. But, using password authentication isn't a good practice and can leave security vulnerabilities, such as brute force attack. It's better to disable password auth and use only SSH key authentication. 

1) Copy your public SSH key to the server's root user using `ssh-copy-id` tool:

```bash
$ ssh-copy-id root@deploy_server_ip
```

Example:

```
$ ssh-copy-id root@5.180.150.210
/usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed: "/home/bob/.ssh/id_rsa.pub"
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
root@5.180.150.210's password:

Number of key(s) added: 1

Now try logging into the machine, with:   "ssh 'root@5.180.150.210'"
and check to make sure that only the key(s) you wanted were added.
```

If all went fine, you'll be able to login to the server without a password prompt. Do it and:

2) On the server (as a root user), open `/etc/ssh/sshd_config` file (you can use `nano` editor),

> This is an important step, before process it MAKE SURE THAT you can sucessfully login to the server using SSH key, (not password). Otherwise you can lose access to your server. 

and navigate to `PasswordAuthentication` line. Make sure that it's not comment-out (not starts with #), and set value to `no`:

```
PasswordAuthentication no
```

Then save the file.

3) Reastart sshd to apply new settings: `$ service ssh restart`. All done!


## Connection Test

This is a connection test playbook to confirm the connection to AWS instance

- name: Connection test
  hosts: all
  tasks:
    - name: ping connection
      ping:

## Playbook for Rails

---
- name: build application Infrastructure
  hosts: all
  become: true

  vars:
    ruby_version: 3.0.0
    app_user: ubuntu
    app_name: file_uploader_latest
    default_path: /home/ubuntu/file_uploader_latest
    app_path: /home/ubuntu/file_uploader_latest/current
    master_key: !vault |
      $ANSIBLE_VAULT;1.1;AES256
      32353566626139643563386165656463636339396133383839316464316132313863313163323961
      3733333830343337353738616432333139633831643932630a363931343566316139343462353763
      65386665383231656561653661393662396430386666343432653037366561633265373633386537
      3234386661393163340a316264363237363265393561633962346263316339326138373137333432
      63373834323131303633353231343437613261666638303632383835303264346438623363333439
      3637376537326133393139326439663131386661626161336434
    key_base: 6b9aab512927ff24a996da1ed66e7bc06d2a1da21479bc60f14a0942677b73d81430009507d2be4230869cf1b4bb79988cde02397442b326def5491a8c2529b8
    node_version: 14.17.0
    server_name: 18.117.98.112
  tasks:
    - name: Install RVM dependencies and other packages
      apt:
        name:
          - curl
          - gnupg2
          - dirmngr
          - bzip2
          - g++
          - gcc
          - autoconf
          - automake
          - bison
          - libc6-dev
          - libffi-dev
          - libgdbm-dev
          - libncurses5-dev
          - libsqlite3-dev
          - libtool
          - libyaml-dev
          - make
          - pkg-config
          - sqlite3
          - zlib1g-dev
          - libgmp-dev
          - libreadline-dev
          - libssl-dev
          - git
          - nginx
        state: present
        update_cache: yes #to handle the issue with package obsolete

    - name: Install RVM key
      become_user: "{{app_user}}"
      shell: "gpg --keyserver keyserver.ubuntu.com --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3 7D2BAF1CF37B13E2069D6956105BD0E739499BDB"
      register: rvm_key_output
      changed_when: "'public key created' in rvm_key_output.stdout"

    - name: Install RVM
      become_user: "{{app_user}}"
      shell: "curl --insecure -sSL https://get.rvm.io | bash -s stable"

    - name: confirm the RVM version installed
      become_user: "{{app_user}}"
      shell: "source /home/{{app_user}}/.rvm/scripts/rvm && rvm -v"
      register: rvm_status
      args:
        executable: /bin/bash
    - debug:
        msg: "RVM version installed: {{rvm_status.stdout}}"

    - name: Install Ruby
      become_user: "{{app_user}}"
      shell: "source /home/{{app_user}}/.rvm/scripts/rvm && rvm install {{ruby_version}} "
      args:
        executable: /bin/bash

    - name: default ruby
      become_user: "{{app_user}}"
      shell: "source /home/{{app_user}}/.rvm/scripts/rvm && rvm --default use {{ruby_version}} "
      args:
        executable: /bin/bash

    - name: Clone Git repository
      git:
        repo: https://github.com/anoobbava/{{app_name}}.git
        dest: "{{app_path}}"
        version: master
        clone: yes
        depth: 1
        force: yes
      become_user: "{{ app_user }}"

    - name: Install Gems using Bundler
      become_user: "{{ app_user }}"
      shell: "source /home/{{app_user}}/.rvm/scripts/rvm && gem install bundler"
      args:
        executable: /bin/bash
        chdir: "{{app_path}}"

    - name: Copy the master.key to config path from Ansible Vault
      copy:
        dest: "{{app_path}}/config/master.key"
        content: "{{master_key}}"

    - name: bundle install Gems
      become_user: "{{ app_user }}"
      shell: "source /home/{{app_user}}/.rvm/scripts/rvm && RAILS_ENV=production bundle install"
      args:
        executable: /bin/bash
        chdir: "{{app_path}}"

    - name: create and migrate database and seed the data
      become_user: "{{ app_user }}"
      shell: |
        source /home/{{app_user}}/.rvm/scripts/rvm && bin/rails db:setup RAILS_ENV=production
      args:
        executable: /bin/bash
        chdir: "{{app_path}}"

    - name: Install NVM # install the latest version of NVM
      become_user: "{{app_user}}"
      shell: "curl -sSL https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash"

    - name: Install Node
      become_user: "{{app_user}}"
      shell: "source /home/{{app_user}}/.nvm/nvm.sh && nvm install {{node_version}}"
      args:
        executable: /bin/bash

    - name: Node version
      become_user: "{{app_user}}"
      shell: "source /home/{{app_user}}/.nvm/nvm.sh && node -v"
      register: nvm_status
      args:
        executable: /bin/bash
    - debug:
        msg: "Node Version: {{nvm_status.stdout}}"

    - name: Install yarn
      shell: "source /home/{{app_user}}/.nvm/nvm.sh && npm install --global yarn"
      args:
        executable: /bin/bash
        chdir: "{{app_path}}"

    - name: debug yarn version
      shell: " source /home/{{app_user}}/.nvm/nvm.sh && yarn --version"
      register: output
      args:
        executable: /bin/bash
    - debug:
        msg: "Yarn version: {{output.stdout}}"

    - name: precompile assets
      shell: " source /home/ubuntu/.nvm/nvm.sh && source /home/{{app_user}}/.rvm/scripts/rvm && bundle exec rake assets:precompile RAILS_ENV=production"
      args:
        executable: /bin/bash
        chdir: "{{app_path}}"

    - name: create shared folder for unicorn
      file:
        path: "{{item}}"
        state: directory
        owner: "{{app_user}}"
        group: "{{app_user}}"
      loop:
        - "{{default_path}}/shared"
        - "{{default_path}}/shared/pids"
        - "{{default_path}}/shared/sockets"
        - "{{default_path}}/shared/logs"

    - name: Start Unicorn as detached mode
      shell: " source /home/{{app_user}}/.rvm/scripts/rvm && unicorn -c {{app_path}}/config/unicorn.rb -E production -D"
      args:
        executable: /bin/bash

    - name: Delete the Default nginx site configurations
      file: path=/etc/nginx/sites-enabled/default
        state=absent

    - name: Configure nginx for production
      template:
        src: nginx.conf.j2
        dest: /etc/nginx/sites-available/{{ app_name }}
      notify: Restart Nginx

    - name: Enable Nginx site
      file:
        src: /etc/nginx/sites-available/{{ app_name }}
        dest: /etc/nginx/sites-enabled/{{ app_name }}
        state: link
      notify: Restart Nginx

  handlers:
    - name: Restart Nginx
      service:
        name: nginx
        state: restarted

[Ansible Playbooks for Rails](https://github.com/nickjj/ansible-rails)
