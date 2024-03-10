## Rack Application with Puma

A simple Rack app that uses Puma to serve a web page saying "Hello Puma". This is a proxy and will be replaced by Rails app later. You can test the Caddy reverse proxy to this Rack app with SSL and custom domain.

To create a simple Ruby program that uses Puma to serve a web page saying "Hello Puma", follow these steps. This program will involve creating a basic Rack application that Puma can run.

### Step 1: Install Required Gems

First, you need to install the `puma` gem, and it's a good practice to manage your application's dependencies using a `Gemfile`. Create a `Gemfile` in your project directory with the following content:

```ruby
source 'https://rubygems.org'

gem 'puma'
```

Then, run `bundle install` to install Puma.

### Step 2: Create the Rack Application

Rack provides a minimal interface between webservers supporting Ruby and Ruby frameworks. Create a file named `config.ru` in your project directory. This file will define the Rack application:

```ruby
app = Proc.new do |env|
  ['200', {'Content-Type' => 'text/html'}, ['Hello Puma']]
end

run app
```

This simple application responds to every request with a `200 OK` status and the body "Hello Puma".

### Step 3: Run Your Application with Puma

With the `config.ru` file in place, you can start your application with Puma. Run the following command in your project directory:

```bash
bundle exec puma
```

Puma will start, and you can access your application by navigating to `http://localhost:9292` in your web browser. You should see the "Hello Puma" message.

### Explanation:

- **Gemfile**: This file declares the Puma dependency for your project.
- **config.ru**: This is a Rack configuration file that describes how to run your Ruby application with Rack-compatible servers like Puma.
- **bundle exec puma**: This command starts the Puma server with the settings defined in `config.ru`.

This setup creates a minimal Ruby application that uses Puma as its web server. Puma serves a simple web page with the text "Hello Puma", demonstrating how to get a Ruby application up and running with Puma.

This is for image testing purposes. Caddy will proxy to this process. This will be replace by a Rails app during the deployment of Rails app.

```yaml
---
- name: Deploy Rack application with Puma
  hosts: all
  become: true
  tasks:
    - name: Install bundler
      ansible.builtin.gem:
        name: bundler
        state: present

    - name: Create Gemfile for Puma installation
      ansible.builtin.copy:
        dest: "{{ project_directory }}/Gemfile"
        content: |
          source 'https://rubygems.org'
          gem 'puma'

    - name: Install required gems with Bundler
      ansible.builtin.command:
        chdir: "{{ project_directory }}"
        cmd: bundle install

    - name: Create Rack application file
      ansible.builtin.copy:
        dest: "{{ project_directory }}/config.ru"
        content: |
          app = Proc.new do |env|
            ['200', {'Content-Type' => 'text/html'}, ['Hello Puma']]
          end

          run app

    - name: Start the application with Puma
      ansible.builtin.command:
        chdir: "{{ project_directory }}"
        cmd: bundle exec puma
      async: 0
      poll: 0
```

**Note**: This playbook assumes the variable `project_directory` is defined, representing the path to your project directory on the remote system. For the "Start the application with Puma" task, consider your specific requirements for background execution (`async` and `poll` parameters) as the given configuration (`async: 0` and `poll: 0`) will run the command in the foreground and wait indefinitely, which might not be suitable for all deployment scenarios. Adjust these parameters based on your deployment strategy.

The Rack app, when run with Puma as the web server without specifying a port number, defaults to listening on port `9292`.

The task is configured to start Puma in the foreground and wait indefinitely due to `async: 0` and `poll: 0`, which causes Packer to hang since it waits for the task to complete, which never happens in this configuration.

To resolve this, you should run Puma in the background or configure the task to not wait indefinitely. Here's how you can modify the task to run Puma in the background:

```yaml
- name: Start the application with Puma in the background
  ansible.builtin.command:
    chdir: "{{ project_directory }}"
    cmd: nohup bundle exec puma -d
  async: 10
  poll: 0
```

In this modification:

- `nohup` is used to run the command in the background and ignore the hangup signal.
- `bundle exec puma -d` starts Puma in "daemon" mode, detaching it from the terminal.
- `async: 10` allows the task to run asynchronously for up to 10 seconds, giving it enough time to start Puma.
- `poll: 0` means Ansible will not wait for the task to complete, moving on immediately after starting it asynchronously.

This configuration starts Puma in the background, allowing Packer to continue with the rest of the provisioning tasks without getting stuck.
