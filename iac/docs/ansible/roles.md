Using roles in Ansible is not strictly necessary, especially if you are managing a simple setup where the database, Rails app, and Redis are all installed on a single EC2 instance. However, adopting roles can still offer several advantages even in such scenarios:

### Advantages of Using Roles:

1. **Organization**: Roles help organize your playbook into clearly defined sections, each responsible for a specific part of the system setup. This makes the playbook easier to read and maintain.

2. **Reusability**: With roles, you can easily reuse the same setup across different projects or environments. For example, if you have another project that also uses Redis, you can reuse the Redis role without any changes.

3. **Modularity**: Roles allow you to manage complex tasks in a modular way. Each role can be developed, tested, and run independently, reducing the complexity of your playbooks.

4. **Encapsulation**: Variables and files used by a role are encapsulated within that role, reducing the chance of conflicts and making the role easier to understand.

5. **Collaboration**: Roles make it easier for teams to work together on the same project. Different team members can work on different roles simultaneously without stepping on each other's toes.

### When to Use Roles:

- **Multiple Environments**: If you plan to deploy your setup across multiple environments (development, staging, production) that share a similar configuration.
  
- **Scalability**: If there is a possibility of scaling your infrastructure in the future (e.g., separating the database and application onto different servers), roles make this transition smoother.

- **Code Maintenance**: If your project is expected to evolve over time, with potentially more services or applications added to the mix.

### Simple Use Case:

For a simple setup with a single EC2 instance, you might start without roles. As your infrastructure grows in complexity, you can refactor your playbooks into roles. Here’s a basic structure without roles:

```yaml
- hosts: all
  tasks:
    - name: Install Redis
      # Redis installation tasks

    - name: Install PostgreSQL
      # PostgreSQL installation tasks

    - name: Deploy Rails application
      # Rails deployment tasks
```

### Transitioning to Roles:

If you decide to use roles, your playbook might look like this:

```yaml
- hosts: all
  roles:
    - redis
    - postgresql
    - rails
```

Each role (`redis`, `postgresql`, `rails`) would contain its own tasks, files, templates, and variables encapsulated within its directory structure.

### Conclusion:

While not necessary for simple setups, roles offer a structured approach that can save time and reduce errors as your infrastructure grows and evolves. Starting with a simple playbook and refactoring into roles as needed can be a practical approach.