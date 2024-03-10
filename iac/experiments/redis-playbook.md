## Ansible Playbook for Installing and Configuring Redis on Ubuntu 22.04

Provide Ansible playbook for installing and configuring Redis on Ubuntu 22.04

Here is an Ansible playbook to install and configure Redis on an Ubuntu 22.04 server. This playbook will perform the following actions:

1. **Install Redis**: This will ensure Redis is installed on your Ubuntu server.
2. **Configure Redis**: Modifies the Redis configuration file for custom settings.
3. **Restart and enable Redis**: Ensures Redis is running and enabled to start at boot.

You'll need to adjust the configuration settings according to your requirements. For this example, let's assume you want to bind Redis to `127.0.0.1` (localhost) and set the `maxmemory` policy.

```yaml
---
- name: Install and configure Redis on Ubuntu 22.04
  hosts: your_host_group
  become: yes # Use sudo
  tasks:
    - name: Install Redis server
      ansible.builtin.apt:
        name: redis-server
        state: present
        update_cache: yes

    - name: Update Redis configuration file
      ansible.builtin.lineinfile:
        path: /etc/redis/redis.conf
        regexp: "^{{ item.option }}"
        line: "{{ item.option }} {{ item.value }}"
        state: present
      loop:
        - { option: "bind", value: "127.0.0.1" }
        - { option: "maxmemory-policy", value: "allkeys-lru" }
      notify: restart redis

    - name: Ensure Redis is running and enabled
      ansible.builtin.service:
        name: redis-server
        state: started
        enabled: yes

  handlers:
    - name: restart redis
      ansible.builtin.service:
        name: redis-server
        state: restarted
```

Before running the playbook:

- Replace `your_host_group` with the name of the group in your Ansible inventory that represents the Ubuntu 22.04 servers where you want Redis installed. You can also specify a single host.
- Adjust the configuration settings in the `loop` section under the "Update Redis configuration file" task as needed. The example provided sets Redis to listen on localhost and uses the `allkeys-lru` eviction policy when max memory is reached.
- Ensure you have Ansible installed on your control machine and that you have SSH access configured for the target machine(s).

To run this playbook, save it to a file (e.g., `install_redis.yml`) and execute it with the `ansible-playbook` command:

```sh
ansible-playbook install_redis.yml
```

This playbook provides a basic setup for Redis. Depending on your specific requirements, you may want to further customize the Redis configuration by adding more options to the loop under the "Update Redis configuration file" task.

## Splitting Playbook

Splitting your Ansible playbook into multiple files and organizing them into different folders can significantly enhance the maintainability, readability, and scalability of your infrastructure code. Whether you need to split this specific playbook depends on several factors, including the complexity of your environment, the reusability of your tasks, and your team's working style. Here's a general guide on how and when to consider splitting your playbook:

### Advantages of Splitting Playbooks:

1. **Modularity:** Smaller, focused files are easier to understand, debug, and reuse in different contexts.
2. **Reusability:** Common tasks or roles can be reused across different playbooks, reducing duplication.
3. **Collaboration:** It's easier for multiple team members to work on different aspects of the infrastructure without causing merge conflicts.
4. **Scalability:** As your infrastructure grows, having a well-organized structure makes it easier to manage complex deployments.

### When to Split a Playbook:

- **Multiple Roles or Tasks:** If your playbook covers different roles (like web server, database) or distinct tasks (installation, configuration, deployment) that can be logically separated.
- **Different Environments:** If you manage multiple environments (development, staging, production) that share common tasks but also have unique requirements.
- **Large Playbooks:** If your playbook becomes too large or complex, making it difficult to quickly understand or modify.

### How to Split a Playbook:

Given your current playbook focused on installing and configuring Redis, here's a simple way to organize it if you decide to expand or modularize:

1. **Roles Directory Structure:**

   ```
   ansible-project/
   ├── roles/
   │   └── redis/
   │       ├── tasks/
   │       │   └── main.yml          # Main tasks for installing and configuring Redis
   │       ├── handlers/
   │       │   └── main.yml          # Handlers, e.g., for restarting Redis
   │       └── defaults/
   │           └── main.yml          # Default variables, if any
   ├── inventory/
   │   └── hosts.yml                 # Inventory file with your hosts
   └── playbooks/
       └── setup-redis.yml           # Main playbook that applies the Redis role
   ```

2. **Main Playbook (`playbooks/setup-redis.yml`):**

   ```yaml
   - name: Setup Redis on Ubuntu 22.04
     hosts: your_host_group
     become: yes
     roles:
       - redis
   ```

3. **Redis Role Tasks (`roles/redis/tasks/main.yml`):** Move the tasks from your original playbook here.

4. **Handlers (`roles/redis/handlers/main.yml`):** Move the restart handler here.

This structure makes your Ansible project more organized and manageable, especially as you add more roles or support more complex setups. It also makes it easier to share and maintain roles across different projects or teams.

## Hostname for One Server

If Redis is being installed on only one server, the value for the `hosts` section in your playbook should directly reference the host or group that includes this specific server. You can define this in your Ansible inventory file. Here are a few approaches on how you can specify this:

### 1. Using the Hostname Directly

If you have a single server and its hostname or IP address is known, you can directly use it in the playbook:

```yaml
- name: Install and configure Redis on Ubuntu 22.04
  hosts: your_server_ip_or_hostname
  become: yes # Use sudo
  tasks:
    # Tasks here
```

Replace `your_server_ip_or_hostname` with the actual IP address or hostname of your server.

### 2. Using an Inventory Group

If you manage your hosts using an Ansible inventory file, you can organize your servers into groups. Even if there's currently only one server for Redis, using a group can be beneficial for scalability and clarity. For example, in your inventory file, you might have:

```ini
[redis_servers]
redis_server ansible_host=your_redis_server_ip
```

Then, in your playbook, you would reference the group:

```yaml
- name: Install and configure Redis on Ubuntu 22.04
  hosts: redis_servers
  become: yes # Use sudo
  tasks:
    # Tasks here
```

This method allows you to easily expand your infrastructure in the future by simply adding more servers to the `redis_servers` group in your inventory file.

### 3. Using `localhost`

If the playbook is being run on the same server where Redis needs to be installed, you could use `localhost` as the target:

```yaml
- name: Install and configure Redis on Ubuntu 22.04
  hosts: localhost
  connection: local
  become: yes # Use sudo
  tasks:
    # Tasks here
```

This approach is less common for this scenario but can be useful for certain local setups or testing environments.

### Conclusion

For your specific case, if Redis is being installed on a single server, you should either directly use the server's IP address or hostname, or better, define a group in your Ansible inventory file and reference that group in your playbook. This allows for clearer organization and easier scalability of your infrastructure management efforts.

To organize the Ansible playbook into a more modular structure using roles, you would split the provided playbook into different files and place them into specific folders within a role. Here's how you can divide the tasks and handlers into a role named `redis`:

### Directory Structure

```
ansible-role-redis/
├── tasks/
│   └── main.yml
├── handlers/
│   └── main.yml
```

### tasks/main.yml

This file contains all the tasks required to install and configure Redis on Ubuntu 22.04.

```yaml
- name: Install Redis server
  ansible.builtin.apt:
    name: redis-server
    state: present
    update_cache: yes

- name: Update Redis configuration file
  ansible.builtin.lineinfile:
    path: /etc/redis/redis.conf
    regexp: "^{{ item.option }}"
    line: "{{ item.option }} {{ item.value }}"
    state: present
  loop:
    - { option: "bind", value: "127.0.0.1" }
    - { option: "maxmemory-policy", value: "allkeys-lru" }
  notify: restart redis

- name: Ensure Redis is running and enabled
  ansible.builtin.service:
    name: redis-server
    state: started
    enabled: yes
```

### handlers/main.yml

This file contains all the handlers that are triggered by the tasks, such as restarting the Redis service.

```yaml
- name: restart redis
  ansible.builtin.service:
    name: redis-server
    state: restarted
```

### Using the Role in a Playbook

After splitting the playbook into the role structure, you would then use the role in your main playbook. Here's how the main playbook might look, assuming the role is named `redis` and you've placed it within a roles directory at the root of your Ansible project:

```yaml
- name: Install and configure Redis on Ubuntu 22.04
  hosts: localhost
  become: true # Use sudo
  roles:
    - redis
```

This structure simplifies the playbook and makes the `redis` role reusable in other playbooks or projects. By organizing tasks and handlers into roles, you can manage complex playbooks more efficiently, making them easier to read, maintain, and extend.

The `redis/defaults/main.yml` file within an Ansible role is intended to store default variables for that role. These variables are the lowest priority in the hierarchy of variable precedence in Ansible, meaning they can be easily overridden by other variables defined elsewhere, such as in the playbook or passed at the command line.

For the Redis role, `defaults/main.yml` might include variables that are commonly changed or need to be configurable to suit different environments. Since the original tasks you provided configure Redis with some specific settings, let's consider what variables could be useful to define in the `defaults/main.yml` file.

Here's an example of what might be inside `redis/defaults/main.yml`:

```yaml
---
# Default Redis configuration options
redis_bind_interface: "127.0.0.1"
redis_maxmemory_policy: "allkeys-lru"

# Default package name and service
redis_package_name: "redis-server"
redis_service_name: "redis-server"

# Other default settings could include
redis_port: 6379
redis_configuration_file: "/etc/redis/redis.conf"
```

These variables are then used in the tasks and templates of the role, making the role more flexible and easier to adapt to different configurations or environments without altering the tasks directly. For example, the task for updating the Redis configuration file could use these variables like so:

```yaml
- name: Update Redis configuration file
  ansible.builtin.lineinfile:
    path: "{{ redis_configuration_file }}"
    regexp: "^{{ item.option }}"
    line: "{{ item.option }} {{ item.value }}"
    state: present
  loop:
    - { option: "bind", value: "{{ redis_bind_interface }}" }
    - { option: "maxmemory-policy", value: "{{ redis_maxmemory_policy }}" }
  notify: restart redis
```

By defining these variables in `defaults/main.yml`, you make it easier for users of the role to customize the Redis installation to their needs by overriding these default values in their playbooks or inventory files.

To reduce duplication in your Packer template, especially when using multiple Ansible provisioners with similar configurations, you have a couple of options. One common approach is to consolidate your Ansible playbooks into a single playbook that includes the others as roles or includes/tasks. Another approach is to use a Packer feature or scripting to streamline the repeated parts of the configuration.

### Consolidating Playbooks into a Single Ansible Playbook

You can create a master playbook that includes all the tasks or roles from your separate playbooks. This approach uses Ansible's capabilities to include other playbooks or roles within a single playbook.

#### Master Playbook Example

Create a new playbook (e.g., `master_playbook.yml`) that includes all the other playbooks as tasks using `import_playbook` or as roles.

```yaml
---
- hosts: all
  user: ubuntu
  become: yes
  tasks:
    - name: Include packages playbook
      import_playbook: packages.yml

    - name: Include fail2ban playbook
      import_playbook: fail2ban.yml

    - name: Include redis playbook
      import_playbook: redis.yml

    - name: Include install_caddy playbook
      import_playbook: install_caddy.yml

    - name: Include goss playbook
      import_playbook: goss.yml
```

Then, in your Packer template, you only need to specify one provisioner that runs the master playbook:

```hcl
provisioner "ansible" {
  playbook_file = "${path.root}/playbooks/master_playbook.yml"
  user          = "ubuntu"
  use_proxy     = false
  ansible_env_vars = [
    "ANSIBLE_HOST_KEY_CHECKING=False"
  ]
}
```

### Using a Script to Run Multiple Playbooks

If consolidating into a single playbook is not desirable or feasible, another approach could involve using a shell script to run multiple playbooks in sequence. This approach requires a bit more setup but can be very flexible.

1. **Create a Shell Script** (`run_playbooks.sh`) that executes the ansible-playbook command for each playbook:

```bash
#!/bin/bash
ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -i hosts.ini -u ubuntu --private-key your_private_key.pem playbooks/packages.yml
ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -i hosts.ini -u ubuntu --private-key your_private_key.pem playbooks/fail2ban.yml
# Add the rest of your playbooks here
```

2. **Modify Packer to Use the Shell Script**:

```hcl
provisioner "shell" {
  script = "run_playbooks.sh"
}
```

Ensure the script is executable and available in the context where Packer runs it. This method consolidates your Ansible runs into a single step in Packer, reducing the repetitive blocks in your template.

Both methods aim to streamline your Packer template by reducing redundancy and making the provisioning process more manageable and maintainable.

The error you're encountering typically occurs when trying to use `import_playbook` within the `tasks` section of an Ansible playbook, which is not allowed. The `import_playbook` directive cannot be used as part of a task list; it's intended to be used at the playbook level, not nested inside `tasks`.

### Correcting the Master Playbook

To fix this issue, you should structure your master playbook to include other playbooks directly, without wrapping them inside `tasks`. Here's how you can adjust your `master_playbook.yml` to avoid this error:

```yaml
---
- import_playbook: packages.yml
- import_playbook: fail2ban.yml
- import_playbook: redis.yml
- import_playbook: install_caddy.yml
- import_playbook: goss.yml
```

This structure tells Ansible to run each listed playbook in sequence, which is the correct way to use `import_playbook`.

### Alternative Approach: Using Roles

If your playbooks are closely related and you're looking to organize shared tasks, you might consider restructuring your playbooks into roles and then including those roles within a single playbook. For example, each of your current playbooks (`packages.yml`, `fail2ban.yml`, etc.) could be converted into a role, and you could have a master playbook that includes these roles:

```yaml
---
- hosts: all
  become: yes
  roles:
    - packages
    - fail2ban
    - redis
    - install_caddy
    - goss
```

In this case, each role would be a directory under the `roles/` directory, containing its own `tasks/main.yml` file, and possibly `handlers`, `defaults`, `vars`, and other role-specific directories as needed.

### Note on Ansible Best Practices

When combining multiple configurations or setups into a single run, it's essential to ensure that they are logically compatible and that the order of execution is correct. Using roles helps encapsulate each configuration aspect, making your playbook more modular and maintainable.

Before restructuring your playbooks into roles, it's a good idea to review how each playbook operates to ensure that combining them won't cause conflicts or unintended behavior.

Converting the previous JSON Packer configuration into HCL format, you can set up passwordless sudo for the `ubuntu` user using a shell provisioner before running your Ansible playbooks. Below is how you can integrate this into your Packer HCL template:

### Step 1: Define Your Source Block

First, define your source block for the builder you are using. This example will use an Amazon EC2 instance, but you should adjust it according to your specific builder requirements:

```hcl
source "amazon-ebs" "example" {
  ami_name      = "packer-example-${timestamp()}"
  instance_type = "t2.micro"
  region        = "us-east-1"
  source_ami_filter {
    filters = {
      name                = "ubuntu/images/*ubuntu-focal-20.04-amd64-server-*"
      root-device-type    = "ebs"
      virtualization-type = "hvm"
    }
    owners      = ["099720109477"]
    most_recent = true
  }
  ssh_username = "ubuntu"
}
```

### Step 2: Add a Shell Provisioner to Modify the sudoers File

Add a shell provisioner to your Packer template to echo the passwordless sudo configuration for the `ubuntu` user into `/etc/sudoers.d/ubuntu`:

```hcl
build {
  sources = [
    "source.amazon-ebs.example"
  ]

  provisioner "shell" {
    inline = [
      "echo 'ubuntu ALL=(ALL) NOPASSWD:ALL' | sudo tee /etc/sudoers.d/ubuntu",
      "sudo chmod 0440 /etc/sudoers.d/ubuntu"
    ]
  }
}
```

### Step 3: Add Your Ansible Provisioner

Following the shell provisioner, add your Ansible provisioner block. Ensure it is placed after the shell provisioner in the `build` block so it executes afterward:

```hcl
  provisioner "ansible" {
    playbook_file = "path/to/your/ansible/playbook.yml"
  }
```

### Complete Packer HCL Template

Combining all the steps, your complete Packer HCL template would look like this:

```hcl
source "amazon-ebs" "example" {
  // Your source configuration
}

build {
  sources = [
    "source.amazon-ebs.example"
  ]

  provisioner "shell" {
    inline = [
      "echo 'ubuntu ALL=(ALL) NOPASSWD:ALL' | sudo tee /etc/sudoers.d/ubuntu",
      "sudo chmod 0440 /etc/sudoers.d/ubuntu"
    ]
  }

  provisioner "ansible" {
    playbook_file = "path/to/your/ansible/playbook.yml"
  }
}
```

This HCL template sets up an EC2 instance (or your specific builder), configures passwordless sudo for the `ubuntu` user, and then runs an Ansible playbook against it. Adjust the `source` block as needed for your specific use case, and replace `"path/to/your/ansible/playbook.yml"` with the actual path to your playbook.
