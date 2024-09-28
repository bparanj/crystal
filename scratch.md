
denylist policy
allowlist policy

Lateral movement attack

netfilter

auditd tool
remote journaling

syslog
journald

systemd

- init system
- userspace service
- telinit
- system instance
- user instance

systemctl

cron, systemd timer


Check user name used to run nginx process in configuration file

grep "user" /etc/nginx/nginx.conf

Check sudo access for the user:

sudo -l -U www-data

Check for login:

grep "www-data" /etc/passwd

Check for groups:

groups www-data



sudo sed -i 's/user www-data/user nginx/' /etc/nginx/nginx.conf

Let's break down the command `sudo sed -i 's/user www-data/user nginx/' /etc/nginx/nginx.conf`:

1. **`sudo`**: This command runs the following command with superuser (root) privileges. It's necessary here because modifying system configuration files typically requires elevated permissions.

2. **`sed`**: This stands for "stream editor." It's a powerful tool used for parsing and transforming text in a file or input stream.

3. **`-i`**: This option tells `sed` to edit the file in place. Without this, `sed` would output the changes to the terminal instead of saving them back to the file.

4. **`'s/user www-data/user nginx/'`**: This is the substitution command for `sed`. It breaks down as follows:
   - **`s`**: Stands for "substitute."
   - **`user www-data`**: This is the pattern to search for in the file.
   - **`user nginx`**: This is the replacement text.
   - The entire command tells `sed` to find occurrences of `user www-data` and replace them with `user nginx`.

5. **`/etc/nginx/nginx.conf`**: This is the path to the Nginx configuration file that is being modified.

In summary, this command changes the user that Nginx runs as from `www-data` to `nginx` in the Nginx configuration file. This might be necessary if your system or setup requires Nginx to run under a different user for permissions or security reasons¹².


 What command would we use to make an account called akhtar a service account?

 To create a service account named `akhtar`, you can use the `useradd` command with specific options to set it up as a service account. Here’s a command you can use:

```bash
sudo useradd -r -s /sbin/nologin akhtar
```

Here's a breakdown of the command:

1. **`sudo`**: Runs the command with superuser privileges.
2. **`useradd`**: The command to add a new user.
3. **`-r`**: Creates a system account (service account). System accounts typically have a UID less than 1000 and are used for running services.
4. **`-s /sbin/nologin`**: Sets the shell to `/sbin/nologin`, which prevents the account from being used to log in interactively.

This command will create a service account named `akhtar` that cannot be used to log in interactively, which is typical for service accounts.


sudo passwd -S akhtar

Sure! Let's break down the command `find /etc/nginx -type d | xargs ls -ld`:

1. **`find /etc/nginx -type d`**:
   - `find` is a command used to search for files and directories.
   - `/etc/nginx` specifies the directory to search within.
   - `-type d` tells `find` to look for directories only.

2. **`|` (pipe)**:
   - The pipe symbol `|` takes the output of the command on its left (`find /etc/nginx -type d`) and uses it as the input for the command on its right (`xargs ls -ld`).

3. **`xargs ls -ld`**:
   - `xargs` is a command that builds and executes command lines from standard input.
   - `ls -ld` lists the details of directories. The `-l` option provides a long listing format, and the `-d` option ensures that directories themselves are listed, not their contents.

In summary, this command finds all directories within `/etc/nginx` and then lists detailed information about each of those directories¹³.

The proxy_pass directive in Nginx is used to forward client requests to another server. It’s commonly used in reverse proxy setups, where Nginx acts as an intermediary between clients and backend servers.

Here’s a basic example of how it’s used:

location / {
    proxy_pass http://example.com;
}

In this configuration, any request to the root URL (“/”) will be forwarded to http://example.com1.

Key Points:
Context: The proxy_pass directive is typically placed inside a location block, but it can also be used in server or http blocks1.
URL Handling: The URL specified in proxy_pass can be a complete URL or just a protocol and host. If it’s a complete URL, the path part of the request is replaced by the path in the proxy_pass URL2.
Variables: You can use variables in the proxy_pass directive, but if you do, you need to specify a resolver to handle DNS resolution3.

Nginx offers several modules for performing authentication checks. Here are some of the most commonly used ones:

1. **ngx_http_auth_basic_module**: This module allows you to limit access to resources using HTTP Basic Authentication. It validates the username and password provided by the client³.

    ```nginx
    location /secure {
        auth_basic "Restricted Area";
        auth_basic_user_file /etc/nginx/.htpasswd;
    }
    ```

2. **ngx_http_auth_request_module**: This module enables client authorization based on the result of a subrequest. If the subrequest returns a 2xx response code, access is allowed⁴.

    ```nginx
    location / {
        auth_request /auth;
    }

    location = /auth {
        proxy_pass http://auth-server;
    }
    ```

3. **ngx_http_auth_jwt_module**: This module allows for JSON Web Token (JWT) authentication. It verifies the JWT provided by the client and grants access based on the token's validity³.

4. **Third-Party Modules**: There are also third-party modules like `ngx_http_auth_pam_module` for PAM authentication and `ngx_http_auth_ldap_module` for LDAP authentication.
