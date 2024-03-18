The error message you're encountering indicates that the `deploy` user does not exist on your system. To use the `deploy` user with PostgreSQL or for other purposes, you'll first need to create this user on your Ubuntu system. Here's how you can do it:

### Creating the `deploy` User

1. **Create the User**: Use the `adduser` command to create a new user named `deploy`. You'll be prompted to set a password for the user and optionally fill in additional information. The `adduser` command also creates a home directory for the user by default.

    ```bash
    sudo adduser deploy
    ```

2. **Grant Sudo Privileges (Optional)**: If you want the `deploy` user to have `sudo` privileges, allowing them to execute commands as the superuser, you need to add them to the `sudo` group. In Ubuntu, members of the `sudo` group are granted superuser privileges.

    ```bash
    sudo usermod -aG sudo deploy
    ```

### Accessing PostgreSQL as the `deploy` User

After you've successfully created the `deploy` user, there are a couple of ways to access PostgreSQL as this user:

- **If `deploy` is a PostgreSQL User**: If you've created a PostgreSQL user named `deploy` (distinct from the Linux system user) and you want to access `psql` as this PostgreSQL user, you don't need to switch to the Linux `deploy` user first. Instead, you can directly use `psql` with the `-U` flag to specify the PostgreSQL user:

    ```bash
    psql -U deploy -d database_name
    ```
  
  Replace `database_name` with the name of the database you wish to connect to. You might also need to use the `-h` flag to specify the hostname if connecting to a remote database.

- **Switch to the `deploy` Linux User**: If you've specific scripts or applications to run under the Linux `deploy` user that interact with PostgreSQL, now that the `deploy` user exists, you can switch to it with:

    ```bash
    sudo -i -u deploy
    ```
  
  Once switched, you can run `psql` or any other command as the `deploy` user.

### Troubleshooting

- **User Exists but Can't Switch**: If you're certain the `deploy` user exists but still face issues switching to it, ensure there are no typos in the username and that the user has not been locked or disabled.
- **PostgreSQL User vs. Linux User**: Keep in mind the distinction between PostgreSQL users (roles) and Linux system users. PostgreSQL users are used to control access within the PostgreSQL system, while Linux users are part of the operating system's user management. They can have the same names but are managed separately.

By following these steps, you should be able to create the `deploy` user on your system and use it as needed, including accessing PostgreSQL.

### Common Errors

```
psql -U deploy
psql: error: connection to server on socket "/var/run/postgresql/.s.PGSQL.5432" failed: FATAL:  Peer authentication failed for user "deploy"
```

The error you're encountering, `FATAL: Peer authentication failed for user "deploy"`, typically occurs because of how PostgreSQL's authentication is configured in the `pg_hba.conf` file for local connections. By default, PostgreSQL uses 'peer' authentication for local connections, which requires the system user's name to be the same as the database user's name you're trying to log in as.

Since you're likely running `psql -U deploy` as a different system user (not as a system user named `deploy`), PostgreSQL's peer authentication is failing. Here's how you can resolve the issue:

### Method 1: Switch to the `deploy` System User Before Connecting

If a system user named `deploy` exists and matches the PostgreSQL user, switch to that user before connecting:

```bash
sudo -i -u deploy
psql
```

This method complies with the 'peer' authentication requirements.

### Method 2: Use `sudo -u` with `psql` for a Quick Test

For a quick test without changing the authentication method, you can use `sudo` to run `psql` as the `deploy` system user:

```bash
sudo -u deploy psql -U deploy
```

This command assumes a system user named `deploy` exists and is also a PostgreSQL user.

### Method 3: Modify `pg_hba.conf` for Password Authentication

For more flexibility, especially if you cannot or prefer not to use the same names for system and database users, you might want to change the authentication method from 'peer' to 'md5' (password authentication) for local connections.

1. **Edit the `pg_hba.conf` File**: Locate and edit the `pg_hba.conf` file, which is typically found in the PostgreSQL data directory. Its location varies depending on the installation method and the operating system. Common paths include `/etc/postgresql/<version>/main/pg_hba.conf` for Ubuntu and similar distributions.

2. **Change Authentication Method**: Find the line(s) related to local connections. It might look something like this:

    ```
    # TYPE  DATABASE        USER            ADDRESS                 METHOD
    local   all             all                                     peer
    ```

    Change `peer` to `md5`:

    ```
    # TYPE  DATABASE        USER            ADDRESS                 METHOD
    local   all             all                                     md5
    ```

    This change requires users to authenticate with a password when connecting locally.

3. **Reload PostgreSQL Configuration**: After saving changes to `pg_hba.conf`, reload the PostgreSQL service for the changes to take effect. You can do this with the following command:

    ```bash
    sudo systemctl reload postgresql
    ```

    or, within the PostgreSQL CLI as the PostgreSQL superuser (e.g., `postgres`):

    ```sql
    SELECT pg_reload_conf();
    ```

4. **Connect Using Password Authentication**: Now you should be able to connect using the `deploy` PostgreSQL user and its password:

    ```bash
    psql -U deploy -W
    ```

    The `-W` flag prompts you for the password.

### Security Note

When switching to password authentication, ensure that passwords are strong and securely managed. Also, be aware that changing authentication methods can affect other local connections, so adjust `pg_hba.conf` with consideration for your entire application environment.

~$ sudo -i -u deploy
To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

deploy@ip-172-31-44-28:~$ psql -U deploy
psql: error: connection to server on socket "/var/run/postgresql/.s.PGSQL.5432" failed: FATAL:  database "deploy" does not exist

The error `FATAL: database "deploy" does not exist` indicates that PostgreSQL is trying to connect to a default database named `deploy`, which matches the username, but such a database doesn't exist. When you run `psql -U deploy` without specifying a database, PostgreSQL defaults to trying to connect to a database with the same name as the user.

Here's how you can address this:

### Option 1: Specify a Database When Connecting

If there's another database you intend to connect to, specify it explicitly with the `-d` option. For example, if you want to connect to the `postgres` database (a common default database in PostgreSQL), you can use:

```bash
psql -U deploy -d postgres
```

Replace `postgres` with the name of any database that the `deploy` user has permission to access.

### Option 2: Create a Database Named `deploy`

If you want the `deploy` user to have a personal database or if your application expects a database with that name, you can create it using the PostgreSQL superuser (usually `postgres`). First, switch to the `postgres` user:

```bash
sudo -i -u postgres
```

Then, create the database:

```bash
createdb -O deploy deploy
```

This command creates a new database named `deploy` and assigns the `deploy` user as the owner. After creating the database, you can exit back to the `deploy` user:

```bash
exit
```

And now, running `psql -U deploy` should connect to the newly created `deploy` database without specifying it explicitly.

### Option 3: Configure PostgreSQL to Use a Different Default Database

If for some reason, you frequently run into this issue and prefer to set a different default database for users when they don't specify one, you can consider configuring PostgreSQL or your application's connection settings to explicitly specify a default database. However, this behavior is primarily controlled by how you connect to PostgreSQL (e.g., command-line options, application database configuration) rather than a PostgreSQL server setting.

### Summary

The most straightforward approach is usually to explicitly specify the database you want to connect to with `psql`. If a specific setup requires users to have databases named after their usernames, you'll need to ensure those databases are created as part of your user setup process.

## Test Deploy User Connection

How to test that the deploy user that was created with the password can connect to the database with that given password

To test that the `deploy` user can connect to a PostgreSQL database using the given password, follow these steps. This process assumes you have already created the `deploy` user with login capabilities and a password, and that you have specified a database that `deploy` has permission to access.

### Step 1: Attempt to Connect Using `psql`

The basic syntax to connect to a PostgreSQL database using the `psql` command-line tool is as follows:

```bash
psql -U username -d databasename -h hostname -W
```

- `-U` specifies the PostgreSQL user you're connecting as.
- `-d` specifies the name of the database you're connecting to.
- `-h` specifies the hostname of the PostgreSQL server. Use `localhost` if you're connecting to a server on the same machine. Omit this option if the server is local and you're using Unix domain sockets.
- `-W` prompts `psql` to ask for a password.

As the `deploy` user attempting to connect to the `postgres` database (as an example), you would run:

```bash
psql -U deploy -d postgres -W
```

If not specified, `-h localhost` is implied for network connections, but it's often omitted for local connections using Unix domain sockets.

### Step 2: Enter the Password

After executing the command, `psql` will prompt you for the `deploy` user's password. Enter the password you specified when creating the user. If the connection is successful, you will be logged into the `psql` command-line interface for the `postgres` database (or whichever database you chose to connect to).

### Step 3: Test Permissions (Optional)

Once connected, you might want to test the permissions of the `deploy` user by performing some database operations that the user should be authorized to do, such as creating a table or selecting data from allowed tables. For example, to create a new table, you could run:

```sql
CREATE TABLE test_table (id serial PRIMARY KEY, name VARCHAR(50));
```

To exit `psql`, type `\q` and press Enter.

### Troubleshooting

- **Connection Failure**: If the connection fails, double-check the user's name, password, and the database name for typos. Also, ensure that the PostgreSQL server is running and accessible.
  
- **Permission Denied**: If you're able to connect but cannot perform certain operations, it may be due to insufficient privileges. Review the permissions granted to the `deploy` user.

- **Host Connection Issues**: If you specified `-h localhost` and cannot connect, ensure that PostgreSQL is configured to accept network connections. You might need to adjust `postgresql.conf` (setting `listen_addresses`) and `pg_hba.conf` for the correct client authentication configuration.

Remember, storing and handling database credentials securely is crucial. Always use strong, unique passwords and limit the permissions granted to database users according to the principle of least privilege.

## Database User and Ubuntu User

The authentication of a PostgreSQL database user to access the `psql` prompt is independent of the Unix/Linux system user's group memberships, including whether or not the system user is in the `sudo` group. PostgreSQL uses its own authentication system, defined in the `pg_hba.conf` file, to control database access.

### PostgreSQL User Authentication

When a PostgreSQL user (`deploy` database user in your case) attempts to connect to a database using `psql`, PostgreSQL checks the `pg_hba.conf` file to determine the required authentication method for that connection. Common methods include:

- **Peer**: For local connections, PostgreSQL compares the operating system user's name with the requested PostgreSQL username. If they match, and if the operating system user can prove its identity (without using a password), the connection is allowed. This method does not apply when accessing PostgreSQL over the network.
  
- **MD5** or **SCRAM-SHA-256**: These methods require the PostgreSQL user to supply a password when connecting.

### System User in `sudo` Group

Being a member of the `sudo` group grants a Linux system user (`deploy` Ubuntu user in your case) the ability to execute commands as the root user or another user via the `sudo` command. It does not affect how the user authenticates to PostgreSQL. Regardless of whether the `deploy` Ubuntu user is in the `sudo` group:

- If the `pg_hba.conf` configuration requires the `deploy` PostgreSQL user to authenticate with a password (e.g., using `md5` or `scram-sha-256` authentication methods), the `deploy` database user will need to provide the correct password to access the `psql` prompt.
  
- If the `pg_hba.conf` configuration allows peer authentication for the `deploy` PostgreSQL user and the system user's name attempting to connect matches the PostgreSQL username, no password would be required for local connections.

### Example

If you wish for the `deploy` database user to use a password when accessing the `psql` prompt, ensure the `pg_hba.conf` file has an appropriate line for local or host connections that specifies `md5` or `scram-sha-256` as the authentication method, for example:

```conf
# TYPE  DATABASE        USER            ADDRESS                 METHOD
local   all             deploy                                  md5
# or for network connections
host    all             deploy          127.0.0.1/32            md5
host    all             deploy          ::1/128                 md5
```

After modifying `pg_hba.conf`, remember to reload PostgreSQL's configuration (e.g., `sudo systemctl reload postgresql`) for the changes to take effect.
