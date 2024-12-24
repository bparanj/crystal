- Mapping the application’s functionality
- Scrutinizing and attacking its core defense mechanisms
- Probing for specific categories of security flaws

http://mdsec.net/wahh

- Broken authentication (62%)
  - Guess weak passwords
  - Brute-force attack
  - Bypass the login

- Broken access controls (71%)

- SQL injection (32%)

- Cross-site scripting (94%)

- Information leakage (78%) 

- Cross-site request forgery (92%) 

## Force a Root Shell

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

