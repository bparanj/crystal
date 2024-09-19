
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

Check cron status:

sudo systemctl status cron

Check timers defined using systemctl:

systemclt list-timers

Why is the file folder name using .d for cron.d?

The `.d` extension in Linux, including for the `cron.d` directory, is used to organize configuration files in a modular way. This approach allows for easier management and scalability of configuration settings. Here are some key reasons:

1. **Modularity**: By placing configuration files in a `.d` directory, each application or service can have its own configuration file. This modular approach makes it easier to manage and update configurations without affecting other services¹.

2. **Ease of Maintenance**: Instead of having a single, large configuration file, smaller, individual files can be managed separately. This reduces the risk of errors and makes it easier to troubleshoot issues¹.

3. **Package Management**: When installing or uninstalling software packages, the package manager can add or remove specific configuration files in the `.d` directories. This ensures that configurations are correctly applied and removed as needed¹.

4. **Flexibility**: The `.d` directories allow for more flexible and dynamic configurations. For example, the `cron.d` directory can contain multiple cron job files, each defining different scheduled tasks².

This method is not limited to cron; it's also used in other parts of the system, such as `logrotate.d` for log rotation configurations and `pam.d` for Pluggable Authentication Modules (PAM) configurations¹.

The `.d` in `cron.d` stands for "directory." It indicates that `cron.d` is a directory containing configuration files. This naming convention is used to organize related configuration files in a modular and manageable way. Each file within the `cron.d` directory can define individual cron jobs, making it easier to manage and update scheduled tasks without modifying a single, large configuration file.

The name "crontab" is derived from "cron table." The term "cron" itself comes from the Greek word "Chronos," which means time¹. The `crontab` file is essentially a table that specifies the schedule for running periodic tasks, known as cron jobs, on Unix-like operating systems.

The name "systemd" follows the Unix convention of naming daemons by appending the letter "d" to indicate a background process or daemon. Additionally, it plays on the term "System D," which refers to a person's ability to adapt quickly and improvise to solve problems¹.

Check schedule in cron:

cat /etc/crontab

System Job

In Linux, a "system job" typically refers to a background process or task managed by the system to perform various functions. These jobs can include scheduled tasks, services, and daemons that run without direct user interaction. Here are a few key types of system jobs:

1. **Cron Jobs**: These are scheduled tasks that run at specified times or intervals. They are managed by the `cron` daemon and defined in `crontab` files or directories like `cron.d`¹.

2. **Systemd Units**: Managed by the `systemd` init system, these units can be services, timers, sockets, or other types of jobs. They are defined in unit files and can be controlled using the `systemctl` command².

3. **At Jobs**: These are one-time tasks scheduled to run at a specific time using the `at` command. They are useful for tasks that don't need to be repeated³.

4. **Background Processes**: Any command or script that is run in the background using `&` at the end of the command. These jobs can be managed using job control commands like `jobs`, `bg`, and `fg`⁴.

Create a user crontab:

crontab -e

User crontabs:

User crontabs are typically stored in the `/var/spool/cron/crontabs` directory on most Linux distributions¹². Each user's crontab file is named after their username. For example, if your username is `john`, your crontab file would be located at `/var/spool/cron/crontabs/john`.






