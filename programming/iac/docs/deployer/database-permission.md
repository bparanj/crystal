The error message you're seeing is related to PostgreSQL authentication issues. Specifically, the `FATAL: Peer authentication failed for user "deploy"` part indicates that the PostgreSQL server did not allow the connection attempt based on the current authentication method configured in its `pg_hba.conf` file.

To solve this issue, consider the following steps:

1. **Review the PostgreSQL `pg_hba.conf` File**:

   - Locate the `pg_hba.conf` file, usually found in the PostgreSQL data directory (e.g., `/etc/postgresql/<version>/main/pg_hba.conf` on Ubuntu).
   - Look for lines that configure the authentication method for connections. You might see a line like this for local connections:
     ```
     local   all   all   peer
     ```
     The `peer` method is likely causing the issue, as it requires the connecting system user to have the same name as the database user. For non-local connections, you might see `md5`, `scram-sha-256`, or another method specified.

2. **Adjust the Authentication Method**:

   - For a development or testing environment where security is less of a concern, you could temporarily change `peer` to `trust` for local connections. This allows connections without authentication (be very cautious with this in a production environment):
     ```
     local   all   all   trust
     ```
   - For production environments or if you want a more secure setup, consider using `md5` or `scram-sha-256` for password-based authentication:
     ```
     local   all   all   md5
     ```
   - After making changes, save the file and restart the PostgreSQL service to apply the changes:
     ```bash
     sudo systemctl restart postgresql
     ```

3. **Ensure the Database User Exists**:

   - Ensure that the `deploy` user exists in PostgreSQL and has the necessary permissions. You can create a user (role) with:
     ```sql
     CREATE ROLE deploy LOGIN PASSWORD 'your_secure_password';
     ```
   - And then ensure the user has permission to create a database if your Rails app requires it to:
     ```sql
     ALTER ROLE deploy CREATEDB;
     ```

4. **Adjust Your Rails Database Configuration**:
   - Make sure your Rails `database.yml` configuration file is correctly set up to use the correct username, password (if you're switching from `peer` to `md5`), and host for your PostgreSQL connection.

Consider security implications when adjusting authentication methods in PostgreSQL and to use secure passwords and connections (e.g., SSL) especially in production environments.

To grant database creation privileges to the `deploy` database user from the PostgreSQL prompt (`psql`), you can use the `ALTER USER` command. This command modifies the attributes of a PostgreSQL role, which in this context is the `deploy` user. The specific attribute you'll modify is the `CREATEDB` privilege, which allows the user to create databases.

Here's how you can do it:

1. Log into the PostgreSQL database as a superuser (, the `postgres` user):

   ```bash
   sudo -u postgres psql
   ```

   This command opens the `psql` prompt for the `postgres` user.

2. At the `psql` prompt, run the following command to grant the `CREATEDB` privilege to the `deploy` user:

   ```sql
   ALTER USER deploy CREATEDB;
   ```

   This command alters the role for `deploy`, enabling it to create databases.

3. To exit the `psql` prompt, type `\q` and press **Enter**.

After executing this command, the `deploy` user will have the privilege to create databases in PostgreSQL. You can also grant additional privileges or configure further access controls depending on your application's needs.

Granting high-level privileges like `CREATEDB` should be done with consideration to your application's security requirements and the principle of least privilege.

To grant the `deploy` database user the privilege to create databases in PostgreSQL, you can use the `ansible.builtin.postgresql_user` module and set the `db` parameter to specify the database where the privilege should be applied, and use the `priv` parameter to specify the privileges. Since the privilege to create databases is  a server-wide setting rather than a specific database setting, you'll need to adjust your approach to use the `postgresql_privs` module instead, as the `postgresql_user` module does not directly support granting the CREATE DATABASE privilege.

However, the direct method to grant such privilege is to set the `CREATEDB` option for the user. Here is how you can modify your playbook to include this:

```yaml
- name: Create database user with a password and grant CREATE DB privilege
  ansible.builtin.postgresql_user:
    login_user: postgres
    name: deploy
    password: "password"
    state: present
    role_attr_flags: CREATEDB
  become: true
  become_user: postgres
```

In this revised task:

- The `role_attr_flags` parameter is used with the `CREATEDB` flag, which allows the `deploy` user to create databases.
- The rest of the task ensures that the `deploy` user is created with the specified password if it doesn't already exist.

This approach sets the user's ability to create databases directly during user creation, simplifying the process and ensuring that the `deploy` user has the necessary privileges.

Yes, that line in the PostgreSQL `pg_hba.conf` file is used to configure client authentication. The line you've provided:

```
local   all             deploy                                  md5
```

Means that for connections to all databases (`all`) from the local machine (`local`), the user `deploy` is required to authenticate using MD5-encrypted passwords (`md5`). This setup is correct if you want the `deploy` user to authenticate with an MD5 password for local connections to any database on the PostgreSQL server.

After making changes to the `pg_hba.conf` file, remember to reload the PostgreSQL service for the changes to take effect. This can  be done with a command like `sudo systemctl reload postgresql` on systems using systemd, or by using the SQL command `SELECT pg_reload_conf();` executed as a superuser within the PostgreSQL environment.
