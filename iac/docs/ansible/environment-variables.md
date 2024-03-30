To have Ansible read environment variables from a file and then ensure those variables are set on an EC2 instance during playbook execution, you can follow a two-step approach:

1. **Load Environment Variables in Ansible**: Use Ansible tasks to read variables from a file within your Ansible environment. This can be done using the `include_vars` module or a custom task that reads the file and registers the variables.
   
2. **Set Environment Variables on the EC2 Instance**: Use the `lineinfile` module or a similar method to append the environment variables to a profile script (`/etc/profile`, `~/.bashrc`, `~/.profile`, etc.) on the EC2 instance, ensuring they are loaded in future sessions.

Here's a breakdown of each step with example tasks:

### 1. Loading Environment Variables in Ansible

Suppose you have a file named `env_vars.yml` that contains key-value pairs of your environment variables.

**env_vars.yml**:
```yaml
ENV_VAR1: value1
ENV_VAR2: value2
```

You can load these variables into your playbook with the `include_vars` module:

```yaml
- name: Load environment variables from a file
  include_vars:
    file: env_vars.yml
    name: env_vars
```

### 2. Setting Environment Variables on the EC2 Instance

Now, to set these environment variables on your EC2 instance, you can use a task that iterates over the loaded variables and appends them to `.bashrc` or another suitable profile script on the instance.

```yaml
- name: Set environment variables on the EC2 instance
  ansible.builtin.lineinfile:
    dest: /home/ec2-user/.bashrc
    line: 'export {{ item.key }}="{{ item.value }}"'
    state: present
    create: yes
  loop: "{{ lookup('dict', env_vars) }}"
  become: yes
  become_user: ec2-user
```

This task iterates through each environment variable loaded from `env_vars.yml` and appends it to the `.bashrc` file of the `ec2-user` user on the target EC2 instance. It uses the `lineinfile` module to ensure that each environment variable is added only once (`state: present` ensures idempotency).

### Complete Playbook Example

Combining both steps, here's how your complete playbook might look:

```yaml
---
- name: Configure EC2 instance environment variables
  hosts: your_ec2_hosts
  vars_files:
    - env_vars.yml
  tasks:
    - name: Load environment variables from a file
      include_vars:
        file: env_vars.yml
        name: env_vars

    - name: Set environment variables on the EC2 instance
      ansible.builtin.lineinfile:
        dest: /home/ec2-user/.bashrc
        line: 'export {{ item.key }}="{{ item.value }}"'
        state: present
        create: yes
      loop: "{{ lookup('dict', env_vars) }}"
      become: yes
      become_user: ec2-user
```

Remember to adjust the `hosts` value to target your specific EC2 instances and the `dest` path in the `lineinfile` task according to the default shell and home directory of your EC2 instance's user.

This playbook approach allows you to dynamically set environment variables on an EC2 instance based on the contents of a file read by Ansible, ensuring that your EC2 instance is configured with the necessary environment for your application or services.

To make Ansible read environment variables from a file and set them up properly on an EC2 instance when running a playbook, you can use the `ansible.builtin.set_fact` module along with the `lookup` function to read the variables from the file. Here's an example of how you can achieve this:

1. Create a file named `env_vars.yml` (or any other name you prefer) to store your environment variables. The file should be in the YAML format, with each variable defined as a key-value pair. For example:

```yaml
---
DB_HOST: db.example.com
DB_PORT: 5432
API_KEY: abcdefghijklmnop
```

2. In your Ansible playbook, use the `ansible.builtin.set_fact` module along with the `lookup` function to read the environment variables from the file and set them as Ansible variables. Here's an example playbook:

```yaml
---
- name: Set up environment variables on EC2 instance
  hosts: ec2_instance
  tasks:
    - name: Read environment variables from file
      ansible.builtin.set_fact:
        env_vars: "{{ lookup('file', 'env_vars.yml') | from_yaml }}"

    - name: Set environment variables on EC2 instance
      ansible.builtin.lineinfile:
        path: /etc/environment
        line: "{{ item.key }}={{ item.value }}"
      loop: "{{ env_vars | dict2items }}"
      become: yes

    - name: Print environment variables
      ansible.builtin.debug:
        msg: "{{ env_vars }}"
```

In this playbook:
   - The `ansible.builtin.set_fact` module is used to read the environment variables from the `env_vars.yml` file using the `lookup` function with the `file` lookup plugin.
   - The `from_yaml` filter is applied to parse the contents of the file as YAML and convert it into an Ansible dictionary.
   - The `ansible.builtin.lineinfile` module is used to set the environment variables on the EC2 instance by modifying the `/etc/environment` file.
   - The `loop` directive is used to iterate over the dictionary of environment variables (`env_vars`) and set each variable as a line in the `/etc/environment` file.
   - The `become: yes` directive is used to run the task with elevated privileges (sudo) since modifying the `/etc/environment` file requires root permissions.
   - Finally, the `ansible.builtin.debug` module is used to print the environment variables to verify that they were read correctly.

3. Run the Ansible playbook with the appropriate inventory and credentials to set up the environment variables on the EC2 instance.

By following these steps, Ansible will read the environment variables from the specified file (`env_vars.yml`) and set them up on the EC2 instance when the playbook is run. The environment variables will be available to the applications and processes running on the instance.

Secure the file containing the environment variables, especially if it contains sensitive information like API keys or database credentials. You can use Ansible Vault or other security mechanisms to encrypt the file and protect its contents.

