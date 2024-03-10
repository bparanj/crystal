To become the `deploy` user when you are logged in as the `ubuntu` user on an EC2 instance, you can use the `su` (substitute user) or `sudo` command to switch users. Here's how to do it with both methods:

### Using `sudo`

The `sudo` command is used to run commands as another user, typically the root user. However, you can specify any user with the `-u` option. This method is preferred when you have `sudo` privileges but not the password of the target user.

```bash
sudo -u deploy -i
```

The `-i` (simulate initial login) option will give you the environment variables and the shell of the `deploy` user. This is similar to what would happen if the `deploy` user logged in to the system directly.

### Using `su`

If you know the password of the `deploy` user, you can switch to it using `su`:

```bash
su - deploy
```

The `-` option provides an environment similar to what the user would expect had the user logged in directly.

### Note

- You may need to adjust permissions or group memberships to allow switching users without a password. This typically involves adding the `ubuntu` user to a group that has `sudo` or `su` permissions for the `deploy` user without requiring a password. This setup requires editing the `/etc/sudoers` file through the `visudo` command for safety.
- For automated scripts or Ansible playbooks, it's common to use `sudo` for its flexibility and logging capabilities. To allow the `ubuntu` user to switch to the `deploy` user without a password, you might add a line like this to the `/etc/sudoers` file (using `visudo` to edit):
  ```sudoers
  ubuntu ALL=(deploy) NOPASSWD: ALL
  ```
  This line allows the `ubuntu` user to execute any command as the `deploy` user without being prompted for a password.

Giving users the ability to switch to other users without a password can introduce security risks if not managed carefully. Always restrict this capability to trusted users and for specific purposes.
