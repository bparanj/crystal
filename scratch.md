
denylist policy
allowlist policy

When using nftables what network protocol family name do we use to indicate both IPv4 and IPv6?

inet


auditd tool
remote journaling



 list the audit rules using auditctl

sudo auditctl -l

What key word would we search for to detect a filesystem mount?

mount

Without a grub password, what clause can we add to the linux line during grub boot to force a root shell

To force a root shell during GRUB boot without a GRUB password, you can modify the `linux` line with the `init=/bin/bash` clause. Here’s how you can do it:

1. At the GRUB menu, highlight the kernel you want to boot.
2. Press `e` to edit the boot entry.
3. Find the line starting with `linux` or `linuxefi`.
4. Append `init=/bin/bash` to the end of this line.
5. Press `Ctrl + X` or `F10` to boot with the modified entry.

This will boot the system into a root shell. Note that the filesystem will be mounted as read-only. To make changes, remount it as read-write using:

```bash
mount -o remount,rw /
```

Search for an exact match of a flag in man page:

Ex:

```
dpkg -s
```

To search for the -s flag.

```
man dpkg
```

```
/-s\b
```

Find the path of the given file:

```
sudo find / -name timesyncd.conf
```

Lateral movement attack

netfilter
