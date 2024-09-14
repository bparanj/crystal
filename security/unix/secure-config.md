- [CIS](https://www.cisecurity.org/)
- [Benchmarks](https://www.cisecurity.org/cis-benchmarks)
- [Wazuh](https://wazuh.com)

- Connect to VPN
- Access the Wazuh portal
- Login using credentials
- Select Security Configuration Assessment
- Select agent
- View overview page
- Select Events tab

Check the default file system on Debian:

```
lsblk -f
```

List Debian partition table:

```
sudo cat /etc/fstab
```

A device file is an interface to a device driver that appears as a normal file.

Check the details of the file system on /dev/sda:

```
sudo fdisk -l /dev/sda
```

nexec

nodev

mknod
fdisk

Single Partition

## Terms

- ext4 Format File System
- Boot Partition
- Swap File
- Special Device
- Run Binaries
- AIDE

## Configuring Secure Boot

- GRUB
- Boot Loader

Without a grub password, what clause can we add to the linux line during grub boot to force a root shell?

init=/bin/bash

What file do we need to update to enable apparmor security at boot time?

To enable AppArmor security at boot time, you need to update the GRUB configuration file. Here are the steps:

1. **Open the `/etc/default/grub` file** in a text editor:
   ```bash
   sudo nano /etc/default/grub
   ```

2. **Add the following parameters** to the `GRUB_CMDLINE_LINUX` line:
   ```plaintext
   GRUB_CMDLINE_LINUX="apparmor=1 security=apparmor"
   ```

3. **Save and exit** the editor.

4. **Update the GRUB configuration** to apply the changes:
   ```bash
   sudo update-grub
   ```

5. **Reboot your system** to enable AppArmor:
   ```bash
   sudo reboot
   ```

After rebooting, you can verify that AppArmor is enabled by running:
```bash
sudo aa-status
```

This will show the status of AppArmor and the loaded profiles³⁶⁷.




pgrep

suid

sysctl



