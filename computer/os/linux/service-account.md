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
