
denylist policy
allowlist policy

When using nftables what network protocol family name do we use to indicate both IPv4 and IPv6?

inet

If we wanted to allow everybody access to an HTTP server running on port 80 on Debian, how would we write the rule to add to our nftables.conf?

To allow everyone access to an HTTP server running on port 80 using nftables on Debian, you can add the following rule to your `nftables.conf` file:

```nft
table inet filter {
    chain input {
        type filter hook input priority 0; policy accept;
        
        # Allow HTTP traffic on port 80
        tcp dport 80 accept
    }
}
```

This configuration does the following:
1. **Defines a table** named `filter` in the `inet` family, which applies to both IPv4 and IPv6.
2. **Creates a chain** named `input` with a filter type, hooked into the input path with a priority of 0, and sets the default policy to accept.
3. **Adds a rule** to accept TCP traffic destined for port 80.

Make sure to reload the nftables configuration after making changes:

```bash
sudo nft -f /etc/nftables.conf
```

This will apply the new rules.

auditd tool
remote journaling

df

The `df` command in Linux stands for **"disk free"**. It's used to display information about the file systems on your system, including the total space, used space, available space, and the percentage of use for each mounted file system.

dd

The `dd` command in Linux stands for **"data duplicator"** or **"disk dump"**³⁵. It's a powerful utility used for low-level data copying and conversion, often employed to create exact copies of files, partitions, or entire disks. This makes it useful for tasks like creating backups, cloning drives, or writing disk images to physical media.

What is /dev/zero stream in Debian?
What is SIEM ?

Emulation refers to the process of imitating or replicating the functionality of one system using another system. This can be applied in various contexts:

1. **Computing**: In the realm of computers, emulation involves using software or hardware to mimic the behavior of another system. For example, a program that allows a computer to run software designed for a different operating system or hardware platform is an emulator⁴. This is commonly used for running old video games on modern systems or for testing software across different environments.

2. **General Usage**: Emulation can also mean striving to match or surpass someone else's achievements or qualities. This form of emulation is often driven by admiration and the desire to achieve similar success¹.




Monitoring System Calls

Yes, you can configure the monitoring of system calls in a configuration file using tools like **auditd** or **Wazuh**. These tools allow you to set up rules that specify which system calls to monitor and log.

### Using auditd
With **auditd**, you can define rules in the `/etc/audit/audit.rules` file. For example, to monitor all `open` system calls, you can add the following rule:

```bash
-a always,exit -F arch=b64 -S open -k open_monitor
```

This rule logs every `open` system call on a 64-bit architecture and tags the log entries with the key `open_monitor`.

### Using Wazuh
**Wazuh** also supports monitoring system calls through its configuration. You can add rules to the Wazuh configuration file to monitor specific system calls. For example, you can add a rule to monitor `execve` system calls:

```xml
<localfile>
    <log_format>audit</log_format>
    <location>/var/log/audit/audit.log</location>
</localfile>
```

Then, create an audit rule to monitor `execve`:

```bash
auditctl -a always,exit -F arch=b64 -S execve -k exec_monitor
```

This setup will log all `execve` system calls and tag them with the key `exec_monitor`.

 list the audit rules using auditctl

sudo auditctl -l

What key word would we search for to detect a filesystem mount?

mount



Running all docker process for websploit makes Thinkpad heat up and blow hot air through the fan. Stop all Docker processes :

```
docker stop $(docker ps -a -q
```

This will stop all the Docker process. No more hot blowing or heating up the laptop. This laptop has 16 GB RAM. 

- Install websploit on 64 GB Yoga and see if the problem goes away.


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

What are the use cases for BeagleBone Black?

The BeagleBone Black is a versatile single-board computer with various use cases, :

1. **Embedded Systems Development**: Ideal for creating and testing embedded systems due to its GPIO, PWM, and ADC capabilities.
   
2. **Industrial Control**: Used in industrial automation for controlling machinery, data acquisition, and process monitoring.

3. **IoT Projects**: Great for Internet of Things (IoT) applications, such as smart home devices and remote sensors, due to its connectivity options and processing power.

4. **Robotics**: Supports robotics projects with its real-time processing capabilities and extensive I/O options.

5. **Educational Purposes**: Useful for learning and teaching about Linux, embedded systems, and electronics.

6. **Prototyping**: Effective for rapid prototyping of hardware and software solutions.

7. **Media Centers**: Can be used as a low-power media center or home automation hub.

These use cases leverage the BeagleBone Black’s processing power, GPIO pins, and connectivity features.

Can it be used as a file server in home network

Yes, the BeagleBone Black can be used as a file server in a home network. You can set it up to share files by installing and configuring software such as:

1. **Samba**: For sharing files with Windows and other networked devices.
2. **NFS (Network File System)**: For sharing files with Unix-like systems.

Here’s a basic outline to set up Samba:

1. **Install Samba**:
   ```bash
   sudo apt-get update
   sudo apt-get install samba
   ```

2. **Configure Samba**:
   Edit the Samba configuration file:
   ```bash
   sudo nano /etc/samba/smb.conf
   ```
   Add a new share definition at the end of the file:
   ```ini
   [shared]
   path = /home/debian/shared
   browseable = yes
   writable = yes
   guest ok = yes
   ```

3. **Create and set permissions for the shared directory**:
   ```bash
   sudo mkdir -p /home/debian/shared
   sudo chmod 777 /home/debian/shared
   ```

4. **Restart Samba**:
   ```bash
   sudo systemctl restart smbd
   ```

You can now access the shared directory from other devices on your network by connecting to the BeagleBone Black’s IP address.

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



