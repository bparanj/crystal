In Debian, the `/etc/login.defs` file is used to set default values for various user account parameters, including password aging policies. These settings apply to all new user accounts created on the system. Here are the key parameters related to password aging that you can configure in this file:

1. **PASS_MAX_DAYS**:
   - This parameter sets the maximum number of days a password is valid before it must be changed.
   - Example:
     ```plaintext
     PASS_MAX_DAYS 90
     ```
     This means passwords will expire after 90 days.

2. **PASS_MIN_DAYS**:
   - This parameter sets the minimum number of days that must pass before a user can change their password again.
   - Example:
     ```plaintext
     PASS_MIN_DAYS 7
     ```
     This means users must wait at least 7 days before changing their password again.

3. **PASS_WARN_AGE**:
   - This parameter sets the number of days before password expiration that the user will receive a warning.
   - Example:
     ```plaintext
     PASS_WARN_AGE 7
     ```
     This means users will be warned 7 days before their password expires.

Here's an example of how these settings might look in the `/etc/login.defs` file:
```plaintext
# Maximum number of days a password may be used.
PASS_MAX_DAYS 90

# Minimum number of days allowed between password changes.
PASS_MIN_DAYS 7

# Number of days warning given before a password expires.
PASS_WARN_AGE 7
```

These settings ensure that users are prompted to change their passwords regularly, enhancing security by reducing the risk of compromised passwords.

Password aging in Debian is a security feature that helps enforce regular password changes to enhance account security. This is typically managed using the `chage` command, which allows administrators to set various parameters for password expiration and aging.

Here are some key aspects of password aging in Debian:

1. **Setting Password Expiration**:
   - To set a password to expire after a certain number of days, use:
     ```bash
     sudo chage -M <days> <username>
     ```
     For example, to set a password to expire every 90 days:
     ```bash
     sudo chage -M 90 user1
     ```

2. **Forcing Password Change on First Login**:
   - To force a user to change their password on their next login, use:
     ```bash
     sudo chage -d 0 <username>
     ```

3. **Setting Account Expiry Date**:
   - To set an account to expire on a specific date, use:
     ```bash
     sudo chage -E <YYYY-MM-DD> <username>
     ```
     For example, to set an account to expire on June 11, 2024:
     ```bash
     sudo chage -E 2024-06-11 user1
     ```

4. **Viewing Password Aging Information**:
   - To view the current password aging settings for a user, use:
     ```bash
     sudo chage -l <username>
     ```

5. **Setting Warning Days**:
   - To set the number of days before a password expires that the user will receive a warning, use:
     ```bash
     sudo chage -W <days> <username>
     ```
     For example, to warn the user 7 days before their password expires:
     ```bash
     sudo chage -W 7 user1
     ```

These commands help ensure that users regularly update their passwords, reducing the risk of unauthorized access¹².

#       PASS_MAX_DAYS   Maximum number of days a password may be used.
#       PASS_MIN_DAYS   Minimum number of days allowed between password changes.
#       PASS_WARN_AGE   Number of days warning given before a password expires.

Change Inactivity Period

sudo useradd -D -f 30

The command `sudo useradd -D -f 30` is used to set default values for new user accounts created on the system. Here's a breakdown of what each part of the command does:

- **`sudo`**: This allows you to run the command with superuser (root) privileges, which is necessary for modifying user account settings.
- **`useradd`**: This is the command used to create new user accounts.
- **`-D`**: This option is used to display or change the default values for new user accounts.
- **`-f 30`**: This sets the default number of days after a password expires before the account is permanently disabled. In this case, it sets the default to 30 days.

So, when you run `sudo useradd -D -f 30`, you are configuring the system to disable any new user account 30 days after their password has expired, unless the password is changed within that period.
