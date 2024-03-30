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
