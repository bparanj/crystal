---
- name: Common setup for all AMIs
  hosts: all
  become: true
  tasks:
    - name: Create deploy user
      ansible.builtin.user:
        name: deploy
        shell: /bin/bash
        create_home: yes


To manually verify that the `deploy` user has been created on an EC2 instance from the terminal, you can use the following methods:

### Method 1: Check the `/etc/passwd` File

- Run the following command to look for the `deploy` user in the `/etc/passwd` file:
  ```bash
  grep deploy /etc/passwd
  ```
- If the user exists, this command will output a line with user information, including the username `deploy`.

### Method 2: Use the `id` Command

- You can also check if the user exists by using the `id` command:
  ```bash
  id deploy
  ```
- If the user exists, this command will show the user and group information for `deploy`.
- If the user does not exist, you'll see an error message indicating there is no such user.

### Method 3: Use the `getent` Command

- Another method to verify the existence of the user is by using the `getent` command:
  ```bash
  getent passwd deploy
  ```
- This command queries the password database for the `deploy` user. If the user exists, it will display the user's entry from the database.

### Connecting to the EC2 Instance

To run these commands, you must first connect to your EC2 instance via SSH. Use the following command, replacing `/path/to/your-key.pem` with the path to your private key file and `your-instance-ip` with the public IP address of your EC2 instance:

```bash
ssh -i /path/to/your-key.pem ubuntu@your-instance-ip
```

After logging in, you can use one of the methods described above to verify the `deploy` user's existence.
