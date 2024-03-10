## Restricting PostgreSQL Connections to the Local EC2 Instance

Restricting connections to the PostgreSQL database server so that it's accessible only from the EC2 instance it resides on involves both network security configurations and PostgreSQL's own configuration settings. This restriction ensures that the database listens only for connections from the local machine, enhancing security. This setup can be approached in two phases: during the base image creation with Packer and during infrastructure provisioning with Terraform.

### During Base Image Creation with Packer

**1. PostgreSQL Configuration:**

- Modify the PostgreSQL configuration file (`postgresql.conf`) to listen on `localhost` (127.0.0.1) or the local loopback interface. This is often the default setting, but it's good to explicitly confirm or set this during the image creation phase.
  ```plaintext
  listen_addresses = 'localhost'
  ```
- This step ensures that, by default, the PostgreSQL server accepts connections only from the local system.

**2. pg_hba.conf Configuration:**

- Ensure the `pg_hba.conf` file is configured to allow connections from the local machine. Typically, this involves an entry like:
  ```plaintext
  # TYPE  DATABASE        USER            ADDRESS                 METHOD
  local   all             all                                     peer
  ```
- This configuration ensures that only local connections are permitted, using the method appropriate for your authentication requirements.

### During Infrastructure Provisioning with Terraform

**1. Security Group Configuration:**

- While Terraform is used for provisioning the infrastructure, it should ensure that the EC2 instance's security group does not allow inbound traffic on the PostgreSQL port (default is 5432) from outside sources. Since the database should only accept connections from the same instance, this might be more about not opening the port to the outside rather than explicitly restricting it, as the Packer configuration already limits PostgreSQL to listen on `localhost`.

**2. No External Access Required:**

- If the application and database are on the same instance, there's no need to configure the security group to allow external database connections, thus no specific Terraform configuration is required for this aspect beyond ensuring no rules are added that open the PostgreSQL port to the internet or other AWS resources.

### Best Practices and Considerations

- **Packer Phase**: Focus on configuring the PostgreSQL server itself for security. This includes setting it to listen only on `localhost` and configuring local access policies.

- **Terraform Phase**: Concentrate on network security and ensuring that the EC2 instance is within a security group that does not expose the PostgreSQL port to the outside world. Terraform is also ideal for configuring other aspects of your AWS environment that interact with your EC2 instance, ensuring they adhere to the principle of least privilege.

- **Separation of Concerns**: By handling PostgreSQL configuration during the Packer phase and network-level configurations during the Terraform phase, you maintain a clear separation of concerns. Packer deals with software and application setup, while Terraform handles the infrastructure and networking aspects.

This approach allows for flexibility and modularity in your infrastructure setup, enabling easy updates to either the application environment or the network configuration without requiring comprehensive changes across your infrastructure setup.

## Ansible Playbook

To modify the Ansible playbook to automate the steps of restricting PostgreSQL connections to the local EC2 instance only, you would need to add tasks to modify PostgreSQL's `postgresql.conf` and `pg_hba.conf` files according to the security practices outlined previously. This playbook assumes the target host(s) are Ubuntu 22.04 instances where PostgreSQL is not yet configured for local connections only.

```yaml
---
- name: Install and Secure PostgreSQL on Ubuntu 22.04
  hosts: your_host_group
  become: yes # Use sudo
  tasks:
    - name: Update apt cache
      ansible.builtin.apt:
        update_cache: yes
        cache_valid_time: 3600 # Cache valid for 1 hour

    - name: Install PostgreSQL
      ansible.builtin.apt:
        name: postgresql
        state: present

    - name: Ensure PostgreSQL is running and enabled on boot
      ansible.builtin.service:
        name: postgresql
        state: started
        enabled: yes

    - name: Configure PostgreSQL to listen on localhost only
      ansible.builtin.lineinfile:
        path: /etc/postgresql/12/main/postgresql.conf
        regexp: '^#?listen_addresses\s*='
        line: "listen_addresses = 'localhost'"
        state: present
      notify: restart postgresql

    - name: Restrict connections to local machine
      ansible.builtin.blockinfile:
        path: /etc/postgresql/12/main/pg_hba.conf
        block: |
          # TYPE  DATABASE        USER            ADDRESS                 METHOD
          local   all             all                                     peer
        marker: "# {mark} ANSIBLE MANAGED BLOCK"
        insertafter: EOF
      notify: restart postgresql

  handlers:
    - name: restart postgresql
      ansible.builtin.service:
        name: postgresql
        state: restarted
        enabled: yes
```

### Modifications Explained

1. **Configure PostgreSQL to Listen on Localhost**: A task is added to modify `postgresql.conf` to ensure PostgreSQL listens on `localhost` only. This step involves finding the line that specifies the `listen_addresses` and setting it to `'localhost'`.

2. **Restrict Connections to Local Machine**: Another task uses the `blockinfile` module to append a configuration block to `pg_hba.conf` that allows local connections only. This step ensures that all local connections are authenticated using the method deemed appropriate for your setup, in this case, `peer`.

3. **Handlers for Restarting PostgreSQL**: After modifying these critical configuration files, it's necessary to restart PostgreSQL for changes to take effect. A handler named `restart postgresql` is defined to manage this.

### Notes

- The specific version of PostgreSQL (`/etc/postgresql/12/main/`) might differ based on the version installed on your Ubuntu 22.04 instance. Adjust the path to match the version of PostgreSQL installed by the playbook.
- These modifications enforce local connections only, enhancing the security of your PostgreSQL server as desired.
- Ensure you have tested this playbook in a safe environment before running it in production, as incorrect configurations could lead to service disruptions.

## Using the Correct Version

To correct the playbook for PostgreSQL version 14.11 on Ubuntu 22.04, you need to adjust the paths in the tasks to match the PostgreSQL version you're using. Since the provided tasks are configured for PostgreSQL version 12, we'll update these to reflect the correct version, which is 14. The main changes involve the path where the `postgresql.conf` and `pg_hba.conf` files are located.

Here's the corrected playbook:

```yaml
- name: Configure PostgreSQL to listen on localhost only and restrict connections
  hosts: all
  become: yes
  handlers:
    - name: restart postgresql
      ansible.builtin.systemd:
        name: postgresql
        state: restarted

  tasks:
    - name: Configure PostgreSQL to listen on localhost only
      ansible.builtin.lineinfile:
        path: /etc/postgresql/14/main/postgresql.conf
        regexp: '^#?listen_addresses\s*='
        line: "listen_addresses = 'localhost'"
        state: present
      notify: restart postgresql

    - name: Restrict connections to local machine
      ansible.builtin.blockinfile:
        path: /etc/postgresql/14/main/pg_hba.conf
        block: |
          # TYPE  DATABASE        USER            ADDRESS                 METHOD
          local   all             all                                     peer
        marker: "# {mark} ANSIBLE MANAGED BLOCK"
        insertafter: EOF
      notify: restart postgresql
```

### Key Changes:

- The paths in both tasks have been updated from `.../postgresql/12/main/...` to `.../postgresql/14/main/...` to match the PostgreSQL 14.11 installation directory structure on Ubuntu 22.04.
- The `handlers` section is defined to restart PostgreSQL after changes. Make sure that the handler is correctly defined and called after making changes to the configuration files.

### Testing the Playbook:

To test the playbook:

1. **Apply the Playbook**: Run the playbook against your target EC2 instance where PostgreSQL is installed.

   ```bash
   ansible-playbook playbook.yml -i inventory_file
   ```

2. **Verify `postgresql.conf` Changes**: SSH into the EC2 instance and check that the `listen_addresses` parameter in `/etc/postgresql/14/main/postgresql.conf` is set to `localhost`.

   ```bash
   grep "listen_addresses" /etc/postgresql/14/main/postgresql.conf
   ```

   This ensures PostgreSQL listens on the localhost interface only.

3. **Verify `pg_hba.conf` Changes**: Ensure that the `pg_hba.conf` file contains the ANSIBLE MANAGED BLOCK for local connections, indicating that local connections are allowed and remote connections are restricted.

   ```bash
   cat /etc/postgresql/14/main/pg_hba.conf
   ```

4. **Test Database Connectivity**:

   - **Locally**: Attempt to connect to the PostgreSQL database locally from the EC2 instance to verify that local connections are permitted.
   - **Remotely**: Try to connect to the PostgreSQL database from a different machine to confirm that remote connections are restricted.

5. **Monitor Logs**: Check PostgreSQL logs for any errors or warnings after applying the playbook and testing connectivity. The log files are typically located in `/var/log/postgresql/`.

By following these steps, you can ensure that your PostgreSQL database is correctly configured to accept connections only from the local machine, enhancing the security of your database server.

local all postgres peer

# TYPE DATABASE USER ADDRESS METHOD

# "local" is for Unix domain socket connections only

local all all peer

# IPv4 local connections:

host all all 127.0.0.1/32 scram-sha-256

# IPv6 local connections:

host all all ::1/128 scram-sha-256

# Allow replication connections from localhost, by a user with the

# replication privilege.

local replication all peer
host replication all 127.0.0.1/32 scram-sha-256
host replication all ::1/128 scram-sha-256

The configuration snippet from the `pg_hba.conf` file you've provided appears to be correctly set up for a variety of common PostgreSQL use cases. Here’s a breakdown of what each part does:

1. **Local Connections for `postgres` User**:

   - `local   all             postgres                                peer`
     - This line allows the `postgres` user to connect to all databases locally (via Unix domain sockets) using the `peer` authentication method, which matches the system user name to the database user name.

2. **Comments**:

   - The comments provide useful information about the configuration and are good practice for maintaining clarity in configuration files.

3. **General Local Connections**:

   - `local   all             all                                     peer`
     - Allows all users to connect to all databases locally using `peer` authentication.

4. **IPv4 Local Connections**:

   - `host    all             all             127.0.0.1/32            scram-sha-256`
     - Allows all users to connect to all databases from the local machine over IPv4 using `scram-sha-256` authentication, which is a secure method for password protection.

5. **IPv6 Local Connections**:

   - `host    all             all             ::1/128                 scram-sha-256`
     - Similar to the IPv4 rule, but for IPv6 connections, allowing secure connections from the local machine using `scram-sha-256`.

6. **Replication Connections**:
   - The lines concerning replication allow connections for the purpose of database replication. This includes both local (`peer` authentication) and network connections (IPv4 and IPv6) using `scram-sha-256` for security.

### Key Points:

- **Authentication Methods**: The use of `peer` for local connections is common and secure for environments where database users match system users. For network connections, `scram-sha-256` is recommended as a secure password authentication method.

- **Security**: The configuration differentiates between local (Unix socket) connections and network connections, applying appropriate authentication methods for each. This is a good security practice.

- **Replication Settings**: The specific settings for replication are important for setups that use PostgreSQL's replication features, ensuring secure and correctly authenticated connections for replication processes.

### Considerations:

- **Customization for Your Needs**: While this configuration works well for many setups, you might need to customize it further based on your specific security policies, network architecture, and PostgreSQL use cases.

- **Version Compatibility**: Ensure that your PostgreSQL version supports the `scram-sha-256` authentication method. It's supported in PostgreSQL 10 and above, which should be fine given the context, but always good to verify.

- **Testing**: After making changes to `pg_hba.conf`, always reload PostgreSQL to apply the changes (`sudo systemctl reload postgresql` or `SELECT pg_reload_conf();` in psql) and test to ensure that your connections are working as expected.

The configuration you've provided is a good starting point for a secure and functional PostgreSQL setup, covering both local and network connections with appropriate authentication methods.

The error message indicates that the task attempting to create a temporary database user without a password failed because Ansible couldn't connect to the PostgreSQL database. The failure reason, "FATAL: Peer authentication failed for user 'postgres'", suggests that the playbook tried to connect to the database using the `postgres` user but was unable to authenticate due to the PostgreSQL's `pg_hba.conf` configuration, which is set to use peer authentication for local connections.

### Understanding Peer Authentication

- **Peer Authentication**: This method is used for local connections and allows the connection if the PostgreSQL role name matches the operating system user name from which the connection request is made. In this case, since Ansible is likely running as a different user (not the `postgres` system user), peer authentication fails.

### Solutions

#### 1. Use `sudo` with the PostgreSQL User for Ansible Tasks

Modify your Ansible task to run as the `postgres` user for tasks that require database access. This aligns with the peer authentication requirements.

```yaml
- name: Create a temporary database user without a password
  ansible.builtin.postgresql_user:
    login_user: postgres
    name: dbtester
    state: present
  become: yes
  become_user: postgres
  become_method: sudo
```

Adding `become`, `become_user`, and `become_method` tells Ansible to execute this specific task as the `postgres` user, which should satisfy the peer authentication method.

#### 2. Adjust `pg_hba.conf` Configuration (Not Recommended for Production)

For a more permissive approach (which is generally not recommended, especially in production environments), you could modify your PostgreSQL's `pg_hba.conf` file to use a different authentication method for local connections, like `md5` or `trust`.

- **Trust**: Allows connection without a password. This is very insecure unless you fully trust all users on your server.
- **MD5**: Requires a password and encrypts it before sending it over the network.

For example, to temporarily allow password-less connections from your Ansible user:

```plaintext
# IPv4 local connections:
host    all             all             127.0.0.1/32            trust
# IPv6 local connections:
host    all             all             ::1/128                 trust
```

After making changes, reload or restart PostgreSQL to apply them:

```bash
sudo systemctl reload postgresql
```

**Note**: If you adjust `pg_hba.conf`, remember to revert the changes to a more secure setting after your tasks are complete.

### Conclusion

For security reasons, the first solution is preferred, as it maintains stricter access controls. Modifying `pg_hba.conf` to ease script execution should be done with caution and ideally only in a controlled environment. Always ensure your database's authentication methods are configured to balance ease of use with the security requirements of your environment.

## Verify the Secure Connection to Database

Testing an Ansible playbook that restricts PostgreSQL database connections to only the EC2 instance where the database server is running involves several steps. This process ensures that your playbook correctly configures PostgreSQL's network settings and firewall rules to limit connections. Here's a structured approach to testing your playbook:

### 1. Create a Testing Environment

- **Isolate the Environment**: Set up a separate EC2 instance in a non-production environment where you can safely apply changes without affecting live data or services.
- **Replicate Production Settings**: Ensure the testing EC2 instance resembles your production environment in terms of OS version, PostgreSQL version, and network configuration to ensure accurate test results.

### 2. Apply the Ansible Playbook

- **Run the Playbook**: Execute your Ansible playbook on the testing EC2 instance. The playbook should include tasks that configure PostgreSQL to listen on `localhost` (127.0.0.1) and set up firewall rules (e.g., using iptables or the UFW firewall) to restrict external access.

### 3. Verify PostgreSQL Configuration

- **postgresql.conf**: Check the PostgreSQL configuration file (`postgresql.conf`) to confirm that the `listen_addresses` parameter is set to `localhost` or `127.0.0.1`, indicating it's only accessible from the local machine.

  You can do this by running:

  ```bash
  grep listen_addresses /etc/postgresql/14/main/postgresql.conf
  ```

  Ensure the output shows `listen_addresses = 'localhost'` or `listen_addresses = '127.0.0.1'`.

- **pg_hba.conf**: Verify the `pg_hba.conf` file to ensure it's configured to allow local connections. Look for a line like:
  ```
  local   all             all                                     peer
  ```
  This line configures PostgreSQL to accept local connections.

To verify the `pg_hba.conf` file for a specific configuration, such as allowing local connections with the `peer` authentication method, you can use the `grep` command in Linux. This command searches through files for lines matching a pattern and prints the matching lines to the output.

Here's how you can use `grep` to check for the specified line in the `pg_hba.conf` file:

```bash
sudo grep "local\s*all\s*all\s*peer" /etc/postgresql/14/main/pg_hba.conf
```

This command looks for lines that match the pattern:

- `local` followed by any number of whitespace characters (`\s*`),
- `all` (again followed by any number of whitespace characters),
- another `all`, and
- `peer`.

For a standard PostgreSQL installation on Linux, the path is often `/etc/postgresql/<version>/main/pg_hba.conf`, where `<version>` is the version number of PostgreSQL you have installed, such as `14`.

If the `grep` command finds a matching line, it will print that line to the terminal. If there is no output, it means no matching line was found, and you may need to add or modify an entry in `pg_hba.conf` to allow local connections with `peer` authentication.

Here's a brief explanation of the components of the `pg_hba.conf` entry you're looking for:

- **local**: Indicates the connection type. In this case, `local` is for Unix domain socket connections.
- **all**: The first `all` specifies that this rule applies to all databases. The second `all` specifies that the rule applies to all users.
- **peer**: Specifies the authentication method. `Peer` authentication uses the operating system's user name of the client process to perform authentication.

Reload or restart your PostgreSQL server after making any changes to the `pg_hba.conf` file for the changes to take effect. You can usually do this with a command like `sudo systemctl reload postgresql` on systems using systemd.

sudo grep "local\s*all\s*all\s\*peer" /etc/postgresql/14/main/pg_hba.conf
local all all peer
local all all peer

The output of your command indicates that there are indeed entries in your `pg_hba.conf` file configured to allow local connections with `peer` authentication for all databases and users. Specifically, the fact that you're seeing two lines with this configuration suggests that there are either duplicate entries or potentially that the configuration is reinforced for different scopes or comments that also match the pattern.

The `peer` authentication method works by obtaining the client's operating system user name and using it for authentication, assuming a database role with the same name exists. This method is commonly used for local connections on the server where the PostgreSQL database is running.

Given that you have confirmed these entries exist, your PostgreSQL server should allow local connections for all users and databases using the `peer` authentication method. This setup is typical and recommended for local development environments or other scenarios where database access is controlled and limited to local users on the server.

If you're configuring PostgreSQL for production environments or need to allow access from external hosts, you would typically use different authentication methods (like `md5` for password-based authentication or `scram-sha-256` for improved security) and would need to adjust the `pg_hba.conf` file accordingly.

Remember, after making any changes to the `pg_hba.conf` file, you should reload the PostgreSQL service to apply the changes. On systems using `systemd`, this can be done with:

```bash
sudo systemctl reload postgresql
```

Or, within the PostgreSQL command-line interface:

```sql
SELECT pg_reload_conf();
```

This ensures your configuration changes are applied without needing to fully restart the PostgreSQL server.

The `pg_hba.conf` content you've provided outlines several rules governing how connections to your PostgreSQL server are authenticated. Here’s a breakdown of the key entries and their implications:

1. **Local Connections for the `postgres` User**:

   ```plaintext
   local   all             postgres                                peer
   ```

   This line allows local connections for the `postgres` user through Unix domain sockets using `peer` authentication, which matches the operating system user to the database user.

2. **General Local Connections**:

   ```plaintext
   local   all             all                                     peer
   ```

   These entries (including the one within the "ANSIBLE MANAGED BLOCK") permit local connections for all users to all databases using `peer` authentication. There's redundancy here with multiple lines providing the same directive, which is generally harmless but can be cleaned up for clarity.

3. **IPv4 and IPv6 Local Connections**:

   ```plaintext
   host    all             all             127.0.0.1/32            scram-sha-256
   host    all             all             ::1/128                 scram-sha-256
   ```

   These lines enable connections over IPv4 and IPv6 to all databases by all users from the localhost IP addresses, using `scram-sha-256` for password authentication. This method is more secure than `md5` and is recommended for connections requiring passwords.

4. **Replication Connections**:

   ```plaintext
   local   replication     all                                     peer
   host    replication     all             127.0.0.1/32            scram-sha-256
   host    replication     all             ::1/128                 scram-sha-256
   ```

   These entries allow connections for database replication purposes. Local connections use `peer` authentication, while network connections (both IPv4 and IPv6) use `scram-sha-256`.

5. **Comments and Structure**:
   The comments and structure (including the "ANSIBLE MANAGED BLOCK") help clarify the purpose of each entry and indicate that some configurations are managed by automation tools like Ansible, which can be helpful for maintaining and understanding the configuration file.

### Recommendations:

- **Review and Consolidate**: Given the redundancy (multiple `local   all             all                                     peer` entries), consider reviewing and potentially consolidating entries for simplicity and maintainability.
- **Security Considerations**: The current configuration is fairly standard and secure, particularly with the use of `scram-sha-256` for network connections. Ensure that all users have strong passwords, especially if accessible over the network.
- **Automation Marks**: The "ANSIBLE MANAGED BLOCK" indicates that part of the file is controlled by Ansible. Be cautious when manually editing these sections, as changes might be overwritten by Ansible runs.

After any modifications to `pg_hba.conf`, remember to reload the PostgreSQL configuration for the changes to take effect:

```bash
sudo systemctl reload postgresql
```

Or from within PostgreSQL:

```sql
SELECT pg_reload_conf();
```

This ensures your PostgreSQL server applies the latest authentication rules without requiring a full restart.

To avoid creating duplicate entries in the `pg_hba.conf` file when using the Ansible `blockinfile` module, you can leverage Ansible's idempotency feature by ensuring your playbook checks for the existence of a specific configuration before making changes. However, the `blockinfile` module is designed to ensure a block of text is present within a file, and if the exact block (including comments) is not found, it might append the block again, leading to duplicates over multiple playbook runs.

For configurations like the `pg_hba.conf` where you want to avoid duplicate lines but ensure specific settings are enforced, it's often more reliable to use a combination of `lineinfile`, custom scripts, or conditional tasks based on the output of a command checking the current configuration. However, these approaches require more complex logic and might not perfectly fit every scenario.

Given the constraints and the goal to avoid duplicates specifically for the `pg_hba.conf` configuration, here's a more nuanced approach using `lineinfile` for a single line change or considering a different strategy for managing PostgreSQL configurations:

### Modified Playbook Using `lineinfile`

This approach replaces the `blockinfile` task with a `lineinfile` task for adding a single line. This is effective for simple changes but may not cover complex configurations that require multiple lines:

```yaml
- name: Install PostgreSQL on Ubuntu 22.04
  hosts: all
  become: true # Use sudo
  tasks:
    - name: Update apt cache
      ansible.builtin.apt:
        update_cache: yes
        cache_valid_time: 3600

    - name: Install PostgreSQL
      ansible.builtin.apt:
        name: postgresql
        state: present

    - name: Ensure PostgreSQL is running and enabled on boot
      ansible.builtin.service:
        name: postgresql
        state: started
        enabled: yes

    - name: Configure PostgreSQL to listen on localhost only
      ansible.builtin.lineinfile:
        path: /etc/postgresql/14/main/postgresql.conf
        regexp: '^#?listen_addresses\s*='
        line: "listen_addresses = 'localhost'"
        state: present
      notify: restart postgresql

    - name: Ensure local all all peer exists in pg_hba.conf
      ansible.builtin.lineinfile:
        path: /etc/postgresql/14/main/pg_hba.conf
        regexp: '^local\s+all\s+all\s+peer$'
        line: "local   all             all                                     peer"
        state: present
      notify: restart postgresql

  handlers:
    - name: restart postgresql
      ansible.builtin.service:
        name: postgresql
        state: restarted
        enabled: yes
```

### Considerations

- This playbook uses `lineinfile` for ensuring a specific line is present without adding a block. It's effective for singular modifications but may not suffice for multi-line configurations.
- For more complex configurations requiring multiple lines or blocks, consider scripting the configuration check and update outside of Ansible, then invoking that script from Ansible.
- Regularly review the `pg_hba.conf` and other configuration files to ensure no unwanted duplications or configurations have been introduced over time.

### Advanced Configuration Management

For more advanced PostgreSQL configuration management where you need to ensure idempotency and avoid duplications for complex multi-line settings:

- **Template Module**: Use the Ansible `template` module to manage the entire `pg_hba.conf` file. This approach gives you full control over the file contents but requires managing the entire template, which might introduce its own challenges, especially with maintaining flexibility for changes across different environments.
- **Custom Scripting**: In cases where neither `lineinfile` nor `template` provides the desired level of control or idempotency, a custom script might be necessary. This script can be designed to intelligently manage PostgreSQL configurations, invoked by Ansible as needed.

### 4. Test Database Connections

- **Local Connection**: Test connecting to the PostgreSQL database locally from the EC2 instance to ensure the database accepts local connections.

  You can do this by running:

  ```bash
  psql -h localhost -U your_database_user -d your_database_name
  ```

  Replace `your_database_user` and `your_database_name` with your actual database user and name.

- **Remote Connection Attempt**: Attempt to connect to the PostgreSQL database from another machine to ensure the connection is refused. Use the `psql` command or a database management tool, specifying the IP address of the EC2 instance:

  ```bash
  psql -h <EC2_instance_IP> -U your_database_user -d your_database_name
  ```

  This attempt should fail if your playbook correctly restricted access.

When you install PostgreSQL, it typically creates a default user and database that you can use to connect to the PostgreSQL server. The default user is `postgres`, and there is also a default database named `postgres` created upon installation. This user is a superuser role in the PostgreSQL instance and has full access to all databases and operations.

To connect to the PostgreSQL server using `psql`, the command-line interface for PostgreSQL, with the default user and database, you can use:

```bash
psql -h localhost -U postgres -d postgres
```

Here's the breakdown of the command:

- `-h localhost`: Specifies the host where the PostgreSQL server is running. In this case, `localhost` indicates that the server is running on the local machine.
- `-U postgres`: Specifies the user to connect as, which is `postgres` by default.
- `-d postgres`: Specifies the database to connect to, which is also `postgres` by default.

Upon executing this command, you may be prompted to enter the password for the `postgres` user if a password has been set and password authentication is required by your `pg_hba.conf` configuration.

**Important**: For security reasons, it's recommended to create separate roles (users) with limited privileges for accessing specific databases, rather than using the `postgres` superuser role for routine database operations. This practice helps to enforce the principle of least privilege and reduces the risk of accidental or malicious changes to the database system.

### 5. Check Firewall Rules

- **List Firewall Rules**: If your playbook configures firewall rules, verify them by listing the current rules to ensure they're correctly applied to block remote connections to PostgreSQL's port (default is 5432).

  For UFW, you can use:

  ```bash
  sudo ufw status
  ```

  For iptables:

  ```bash
  sudo iptables -L
  ```

### 6. Automated Testing (Optional)

Consider automating these tests using a tool like Testinfra or Molecule, which can programmatically verify configurations and connection attempts, making it easier to integrate testing into a CI/CD pipeline.

### 7. Document the Testing Process

Document the steps, commands, and expected outcomes of your testing process. This documentation will be invaluable for future testing cycles or for other team members to understand and replicate the testing process.

### Conclusion

Testing your Ansible playbook for restricting PostgreSQL database connections ensures that your database configuration adheres to your security and operational requirements. Through a combination of configuration verification, connection testing, and firewall rule inspection, you can confidently deploy changes knowing they achieve the intended restrictions.

See playbooks/postgreql.yml:

Your Ansible playbook is well-structured and correctly set up for its intended tasks: installing PostgreSQL on Ubuntu 22.04, configuring it to only listen on `localhost`, restricting connections to the local machine using `peer` authentication, ensuring `psycopg2-binary` is installed for PostgreSQL modules to work, creating a temporary database user without a password, and finally creating a temporary database owned by that user.

However, there are a few considerations and best practices to keep in mind:

### 1. PostgreSQL Version

Ensure that PostgreSQL version 14 is available in the default Ubuntu 22.04 repository or any added repositories. The version specified in the configuration file paths (`/etc/postgresql/14/main/...`) needs to match the installed PostgreSQL version. If a different version gets installed, you'd need to adjust the paths accordingly.

### 2. `psycopg2-binary` Installation

The task to install `psycopg2-binary` is crucial for allowing Ansible's PostgreSQL modules to interact with the database. However, ensure that the control machine where Ansible is running has Python and `pip` installed. This task assumes that Python and `pip` are available globally. If you're using a Python virtual environment for Ansible, you might need to adjust the task to ensure `psycopg2-binary` is installed in the correct environment.

### 3. Encrypted Passwords

For the temporary database user (`dbtester`), you correctly noted that no password is set, and encryption is not relevant. This is fine for a temporary setup in a controlled environment, but always ensure to use strong, encrypted passwords for any user in production environments.

### 4. Temporary Database Naming

The temporary database is named `deleteme`, clearly indicating its purpose and temporary nature. This is a good practice for clarity. However, ensure that this temporary database and user are removed after testing to maintain security and cleanliness of your database server.

### 5. Notification for Restart

You have a handler to restart PostgreSQL after making changes to its configuration. This is good practice to ensure changes take effect. Just ensure that tasks which require PostgreSQL to be restarted (like modifying `postgresql.conf` or `pg_hba.conf`) correctly notify this handler.

### Conclusion

Your playbook seems ready for the purpose of setting up a test environment with PostgreSQL on Ubuntu 22.04. It's important to execute this playbook in a safe, test environment and not on production servers due to the creation of a user without a password and a clearly temporary database. After testing, you should follow up with tasks or another playbook to clean up these temporary configurations before moving into a production setup.

ubuntu@ip-172-31-31-124:~$ sudo ufw status
Status: inactive
ubuntu@ip-172-31-31-124:~$ sudo iptables -L
Chain INPUT (policy ACCEPT)
target prot opt source destination

Chain FORWARD (policy ACCEPT)
target prot opt source destination

Chain OUTPUT (policy ACCEPT)
target prot opt source destination

Your current firewall status and `iptables` rules indicate that:

1. **UFW (Uncomplicated Firewall) is Inactive**: The output from `sudo ufw status` shows that UFW is not currently active on your system. UFW is a user-friendly interface for managing `iptables` rules in Ubuntu and other Linux distributions. Since it's inactive, it's not currently enforcing any firewall rules.

2. **Default `iptables` Rules**: The output from `sudo iptables -L` shows the default policy for the INPUT, FORWARD, and OUTPUT chains is ACCEPT, and there are no specific rules defined. This means that your system is not blocking or filtering any network traffic on its own through `iptables`. All incoming, outgoing, and forwarded traffic is allowed.

### Actions to Consider

- **Activating UFW**: If you intend to use UFW to manage your firewall rules, you can activate it by running `sudo ufw enable`. Once enabled, you'll want to configure your rules before or immediately after enabling it to ensure you don't accidentally block yourself out, especially if you're connecting over SSH.

- **Configuring Basic UFW Rules**: For a basic setup, you might start by allowing SSH (if you're using it) to ensure remote access is maintained: `sudo ufw allow ssh`. Then, you can proceed to configure additional rules based on the services running on your server and your security requirements.

- **Using `iptables` Directly**: If you prefer more granular control over your firewall rules, you can use `iptables` directly to define specific rules. This approach requires a good understanding of network protocols and `iptables` syntax. For most users and common scenarios, UFW provides a simpler and sufficient interface.

- **Security Best Practices**: Regardless of whether you use UFW or `iptables`, it's important to follow security best practices:

  - **Minimum Necessary Access**: Only allow network traffic that is essential for the operation of your server and applications.
  - **Regular Reviews**: Periodically review your firewall rules to ensure they still meet your security needs and adjust as necessary.
  - **Logging**: Consider enabling logging for certain rules to monitor for potentially malicious activity or to troubleshoot connectivity issues.

- **Remember to Test**: After making changes to your firewall configuration, always test to ensure that your services are accessible as intended and that unauthorized access is blocked.

Activating and configuring a firewall is an essential step in securing your server. It helps protect against unauthorized access and can be configured to allow only the traffic necessary for your applications to function.

[UFW playbooks in pending]
