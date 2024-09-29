
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

sudo passwd -S akhtar

