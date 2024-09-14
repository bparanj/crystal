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

What is extended type device?

In Debian, an "extended type device" typically refers to an **extended partition**. Here's a brief overview:

### **Extended Partition**
- **Purpose**: Allows you to bypass the limitation of having only four primary partitions on a disk.
- **Structure**: An extended partition acts as a container for multiple **logical partitions**.
- **Usage**: Useful when you need more than four partitions on a disk. You can create one extended partition and then create multiple logical partitions within it.

### **Creating and Managing Extended Partitions**
- **Tools**: Common tools for managing partitions include `fdisk`, `parted`, and `gparted`.
- **Commands**: Using `fdisk`, you can create an extended partition by selecting the partition type as "extended" during the partition creation process.

## Special Device

In Debian, a "special device" refers to a **device file** or **device node**. These files are located in the `/dev` directory and represent hardware devices attached to the system. Here are some key points:

### **Types of Special Devices**
1. **Character Devices**:
   - **Function**: Handle data one character at a time.
   - **Examples**: Serial ports, keyboards, and mice.
   - **Identification**: Denoted by a 'c' in the file listing (e.g., `crw-r--r--`).

2. **Block Devices**:
   - **Function**: Handle data in blocks.
   - **Examples**: Hard drives, USB drives.
   - **Identification**: Denoted by a 'b' in the file listing (e.g., `brw-r--r--`).

### **Purpose of Special Devices**
- **Abstraction**: Provide a standardized interface for software to interact with hardware.
- **Access**: Allow user space applications to communicate with hardware through system calls.

### **Example**
```bash
ls -l /dev/sda
```
This command lists the details of the device file for the first hard drive, showing whether it's a character or block device.

## sda

In Debian, `/dev/sda` represents the first SCSI (or SATA) disk drive on your system. Here's a bit more detail:

### **Understanding `/dev/sda`**
- **Device Naming**: The naming convention `/dev/sda` is used for the first disk, `/dev/sdb` for the second, and so on.
- **Partitions**: Partitions on these disks are named sequentially, such as `/dev/sda1`, `/dev/sda2`, etc.
- **Role**: This device file is crucial for managing and interacting with your storage devices. It acts as an interface between the operating system and the physical hardware².

### **Example Usage**
- **Listing Partitions**:
  ```bash
  lsblk
  ```
  This command will show all block devices and their partitions, including `/dev/sda` and its partitions.

- **Checking Disk Information**:
  ```bash
  sudo fdisk -l /dev/sda
  ```
  This command provides detailed information about the disk and its partitions.

Yes, the naming convention `/dev/sdX` is still applicable even if the hardware is not using SCSI or SATA. This is because the Linux kernel uses the same naming scheme for various types of storage devices, including:

- **SCSI** (Small Computer System Interface)
- **SATA** (Serial ATA)
- **USB** (Universal Serial Bus) storage devices
- **NVMe** (Non-Volatile Memory Express) drives

So, whether your storage device is connected via SCSI, SATA, USB, or NVMe, it will still be represented as `/dev/sdX` (e.g., `/dev/sda`, `/dev/sdb`, etc.) in Debian.

In Debian, the **boot partition** is a dedicated partition on your hard drive that contains the files necessary to boot the operating system. Here are some key points:

### **Purpose of the Boot Partition**
- **Storage**: It stores the bootloader (like GRUB) and other essential files needed to start the operating system.
- **Isolation**: By isolating these files, it ensures that they are not affected by other system operations, which can help in maintaining system stability and security.

### **Types of Boot Partitions**
1. **/boot**:
   - **Content**: Contains the kernel, initial RAM disk (initrd), and GRUB configuration files.
   - **Format**: Typically formatted with a filesystem like ext4.

2. **/boot/efi** (for UEFI systems):
   - **Content**: Contains the EFI bootloader and related files.
   - **Format**: Usually formatted with FAT32.
   - **Usage**: Required for systems using UEFI firmware³.

### **Example Configuration**
- **Standard BIOS System**:
  - `/boot` partition might be around 500MB.
- **UEFI System**:
  - `/boot/efi` partition is typically around 100-200MB.

### **Creating a Boot Partition**
When installing Debian, you can create a boot partition during the partitioning step. Here’s a basic outline:
1. **Select the disk** where you want to create the partition.
2. **Create a new partition** and set its mount point to `/boot` or `/boot/efi`.
3. **Choose the filesystem** (ext4 for `/boot`, FAT32 for `/boot/efi`).

The **ext4** (fourth extended filesystem) is a widely used file system in Debian and other Linux distributions. Here are some key points about ext4:

### **Features of ext4**
- **Journaling**: Helps protect the integrity of the file system by keeping a journal of changes, which can be used to recover from crashes.
- **Large File and Volume Support**: Supports volumes up to 1 exabyte and files up to 16 terabytes.
- **Extents**: Uses extents instead of traditional block mapping, which improves performance and reduces fragmentation.
- **Backward Compatibility**: Can mount ext3 and ext2 file systems, making it easier to upgrade from older file systems.

### **Creating an ext4 File System**
To format a partition with the ext4 file system, you can use the `mkfs.ext4` command. Here’s an example:

```bash
sudo mkfs.ext4 /dev/sdXn
```
Replace `/dev/sdXn` with the appropriate partition identifier (e.g., `/dev/sda1`).

### **Checking the File System**
After formatting, you can verify the file system using the `lsblk` command:

```bash
lsblk -f
```
This command lists all block devices and their file systems¹.

### **Advantages of ext4**
- **Performance**: Ext4 is optimized for performance, making it suitable for a wide range of applications.
- **Reliability**: The journaling feature helps ensure data integrity, even in the event of a system crash.
- **Flexibility**: Supports a wide range of features and configurations, making it adaptable to different use cases.

The `/etc/fstab` file in Debian is a critical system configuration file that defines how disk partitions, storage devices, and other file systems should be mounted and integrated into the system's file structure at boot time. Here are some key points:

### **Purpose of `/etc/fstab`**
- **Mounting**: Specifies which file systems should be mounted automatically at boot.
- **Configuration**: Defines mount points, file system types, and mount options for each file system.

### **Structure of `/etc/fstab`**
Each line in the `/etc/fstab` file represents a file system and contains six fields, separated by spaces or tabs:

1. **File System**: The device or partition to be mounted (e.g., `/dev/sda1`).
2. **Mount Point**: The directory where the file system will be mounted (e.g., `/` for the root file system).
3. **Type**: The type of file system (e.g., `ext4`, `swap`).
4. **Options**: Mount options (e.g., `defaults`, `noatime`).
5. **Dump**: Backup utility option (usually set to `0` or `1`).
6. **Pass**: File system check order at boot (usually `0`, `1`, or `2`).

### **Example Entry**
```plaintext
/dev/sda1  /  ext4  defaults  1  1
```
This entry mounts the first partition of the first disk (`/dev/sda1`) to the root directory (`/`) with default options, and it will be checked during boot.

### **Common Options**
- **defaults**: Uses default mount options (`rw`, `suid`, `dev`, `exec`, `auto`, `nouser`, `async`).
- **noatime**: Prevents updating access times, which can improve performance.
- **ro**: Mounts the file system as read-only.
- **rw**: Mounts the file system as read-write.

### **Managing `/etc/fstab`**
- **Editing**: Use a text editor like `nano` or `vim` to edit the file.
  ```bash
  sudo nano /etc/fstab
  ```
- **Testing**: After editing, you can test the changes by remounting all file systems.
  ```bash
  sudo mount -a
  ```

Yes, `fstab` is an acronym. It stands for **File System Table**. This file is crucial for defining how disk partitions and other file systems are mounted and integrated into the system's file structure at boot time.

In Debian, **tmpfs** is a temporary file system that resides in virtual memory. Here are some key points about tmpfs:

### **Features of tmpfs**
- **Memory-Based**: Stores files in RAM, making file access extremely fast.
- **Temporary Storage**: Contents are lost upon unmounting or rebooting, as they are not written to the disk.
- **Dynamic Sizing**: Automatically grows and shrinks to accommodate the files it contains, within the limits of available RAM and swap space².

### **Common Uses**
- **/tmp Directory**: Often used for the `/tmp` directory to speed up access to temporary files and ensure they are cleared on reboot.
- **/run and /dev/shm**: Used for runtime data and shared memory, respectively¹.

### **Example Configuration**
To mount a tmpfs file system, you can use the following command:
```bash
sudo mount -t tmpfs -o size=128m tmpfs /mnt/ramdisk
```
This command creates a tmpfs of 128MB mounted at `/mnt/ramdisk`⁴.

### **Advantages of tmpfs**
- **Speed**: Faster access to files compared to disk-based file systems.
- **Flexibility**: Can be resized dynamically and supports various mount options.
- **Security**: Ensures that sensitive data stored temporarily is not left on the disk after a reboot.

In Debian, the `nosuid` option is used when mounting a file system to enhance security. Here's what it does:

### **Function of `nosuid`**
- **Disables SUID/SGID Bits**: The `nosuid` option prevents the execution of programs with the **set-user-identifier (SUID)** and **set-group-identifier (SGID)** bits set. These bits allow a program to run with the privileges of the file's owner or group, which can be a security risk if misused¹.

### **Usage in `/etc/fstab`**
You can add the `nosuid` option to a file system entry in the `/etc/fstab` file to ensure it is mounted with this option. Here’s an example entry:
```plaintext
/dev/sda1  /mnt/data  ext4  defaults,nosuid  0  2
```
This entry mounts the `/dev/sda1` partition at `/mnt/data` with the `nosuid` option, preventing any SUID/SGID programs on this partition from running with elevated privileges¹.

### **Common Use Cases**
- **Temporary Directories**: Often used for directories like `/tmp` to prevent the execution of potentially malicious scripts or binaries.
- **Shared Storage**: Useful for shared storage locations to limit the risk of privilege escalation attacks.


nexec



nodev

mknod
fdisk

Single Partition
Multi Partition

In Debian, a multi-partition setup involves dividing your hard drive into several partitions, each serving a specific purpose. This approach can enhance system performance, security, and manageability. Here are some common partitions you might consider:

1. **Root Partition (`/`)**: This is the main partition where the operating system is installed. It contains all the essential system files.
2. **Home Partition (`/home`)**: This partition stores user data and personal files. Keeping it separate from the root partition can make system upgrades and reinstalls easier.
3. **Swap Partition**: This is used for virtual memory. It's a space on the hard drive that the system can use as RAM when the physical RAM is full.
4. **Boot Partition (`/boot`)**: This partition contains the files needed to boot the system, such as the kernel and bootloader.
5. **Var Partition (`/var`)**: This partition holds variable data like logs, databases, and spool files. It's useful to separate it to prevent large log files from filling up the root partition.
6. **Tmp Partition (`/tmp`)**: This is used for temporary files. Keeping it separate can improve security and prevent temporary files from filling up the root partition.

For more complex setups, you might also consider separate partitions for `/usr`, `/opt`, and `/srv`².

Partition is the term used for logical division of physical hard drives to separate areas in the hardware for different purposes. Is this correct.

Yes, that's correct! A partition is a logical division of a physical hard drive into separate areas, each of which can be used for different purposes. This allows you to organize your data more efficiently and can help with system management and performance.

For example, you might have one partition for your operating system, another for your personal files, and another for backups. Each partition can be formatted with a different file system and can be managed independently.

Device Number

In Debian Linux, a device number is used to uniquely identify devices within the system. Each device is assigned a **major number** and a **minor number**:

1. **Major Number**: This identifies the driver associated with the device. For example, all hard drives might have the same major number because they use the same driver.
2. **Minor Number**: This differentiates between devices that use the same driver. For instance, different partitions on the same hard drive will have different minor numbers.

You can view device numbers using the `ls -l /dev` command, which lists all devices in the `/dev` directory along with their major and minor numbers. Here's an example output:

```bash
brw-rw---- 1 root disk 8, 0 Sep 13 12:00 sda
brw-rw---- 1 root disk 8, 1 Sep 13 12:00 sda1
```

In this example:
- `sda` has a major number of 8 and a minor number of 0.
- `sda1` (a partition on `sda`) has a major number of 8 and a minor number of 1.


Binaries

In Linux, the term **binaries** refers to executable files that contain compiled code. These files are essential for running programs, scripts, and commands on the system. When you execute a command like `ls` to list directory contents or `cp` to copy files, you're actually running binaries that reside in directories such as `/bin`, `/usr/bin`, and `/sbin`¹².

Here's a quick breakdown:
- **/bin**: Contains essential command binaries needed for the system to function, like `ls`, `cp`, and `mv`.
- **/sbin**: Holds system binaries, typically used by the root user for administrative tasks.
- **/usr/bin**: Stores user binaries, which are non-essential but commonly used commands and applications.
- **/usr/sbin**: Contains non-essential system binaries used by the root user.

Binaries allow the operating system to perform a wide range of tasks, from basic file manipulations to running complex applications¹³.

Programs are called "binaries" because they are compiled into binary code, which is the machine-readable format that computers understand. At the lowest level, computers operate using binary (base-2) number systems, which consist of only two digits: 0 and 1¹².

Here's a bit more detail:
- **Binary Code**: This is the fundamental language of computers, representing data and instructions using combinations of 0s and 1s. Each binary digit (bit) corresponds to an electrical state: on (1) or off (0)¹.
- **Compilation**: When source code (written in high-level programming languages like C or Python) is compiled, it is translated into binary code. This process converts human-readable instructions into a format that the computer's processor can execute directly².

So, the term "binaries" reflects the fact that these executable files are in a binary format, ready for the computer to run.

So the programs are already compiled and the executable program is in the binary format.

Yes. When a program is compiled, the source code (written in a high-level programming language) is translated into machine code, which is in binary format. This machine code is what the computer's processor can execute directly. The resulting file is called a binary or an executable.

For example, when you compile a C program using `gcc`, the output is a binary file that you can run on your system. Here's a simple illustration:

1. **Source Code**: Written in a high-level language (e.g., C).
   ```c
   #include <stdio.h>

   int main() {
       printf("Hello, World!\n");
       return 0;
   }
   ```

2. **Compilation**: Using a compiler like `gcc`.
   ```bash
   gcc -o hello hello.c
   ```

3. **Binary/Executable**: The output file (`hello`) is in binary format.
   ```bash
   ./hello
   ```

When you run `./hello`, the binary code is executed by the processor, and you see the output "Hello, World!" on your screen.

The binaries that are shipped with the any Linux distro distribution is already compiled in a format and stored in standard directories for the users to run them from command line.

Yes, that's correct! When you install a Linux distribution, it comes with a set of pre-compiled binaries that are ready to use. These binaries are stored in standard directories, making it easy for users to run them from the command line. Here are some of the common directories where these binaries are stored:

- **/bin**: Contains essential command binaries needed for the system to function, like `ls`, `cp`, and `mv`.
- **/sbin**: Holds system binaries, typically used by the root user for administrative tasks.
- **/usr/bin**: Stores user binaries, which are non-essential but commonly used commands and applications.
- **/usr/sbin**: Contains non-essential system binaries used by the root user.
- **/usr/local/bin**: Used for binaries that are installed locally, often by the system administrator or user.

These directories are included in the system's PATH environment variable, so you can run the commands without needing to specify their full path.

Here's a table comparing and contrasting system binaries, user binaries, and other types of binaries found in a Linux distribution:

| **Type of Binary** | **Description** | **Location** | **Usage** | **Examples** |
|--------------------|-----------------|--------------|-----------|--------------|
| **System Binaries** | Essential binaries required for the system to function. Typically used for system-level tasks. | `/bin`, `/sbin` | Used by both the system and users for basic operations and administrative tasks. | `ls`, `cp`, `mv`, `init`, `shutdown` |
| **User Binaries** | Non-essential binaries used by users for various applications and commands. | `/usr/bin`, `/usr/sbin` | Used by users for everyday tasks and applications. | `firefox`, `gcc`, `nano`, `htop` |
| **Local Binaries** | Binaries installed locally, often by the system administrator or user. | `/usr/local/bin`, `/usr/local/sbin` | Used for custom or locally installed applications and scripts. | Custom scripts, locally compiled programs |
| **Temporary Binaries** | Binaries used temporarily, often during the boot process or for temporary tasks. | `/tmp`, `/var/tmp` | Used for temporary tasks and are usually cleaned up after use. | Temporary installation files, temporary scripts |
| **Library Binaries** | Shared libraries used by various programs to perform common tasks. | `/lib`, `/usr/lib`, `/lib64` | Used by programs to access shared functions and routines. | `libc.so`, `libm.so` |

This table highlights the different types of binaries, their locations, usage, and some examples. Each type of binary serves a specific purpose and is stored in standard directories to ensure the system operates smoothly.

Different kinds of binaries in Linux serve various purposes, ensuring the system operates efficiently, securely, and flexibly. Here's why having different types of binaries is important:

1. **Organization and Management**: Separating binaries into different categories helps keep the system organized. Essential system binaries are kept separate from user applications, making it easier to manage and maintain the system.

2. **Security**: By isolating system binaries from user binaries, you can apply different security policies and permissions. For example, system binaries in `/sbin` might require root access, while user binaries in `/usr/bin` can be executed by any user.

3. **Performance**: Different types of binaries can be optimized for their specific tasks. System binaries are often optimized for performance and stability, while user binaries might prioritize features and usability.

4. **Flexibility**: Having separate locations for different binaries allows for more flexible system configurations. For instance, you can easily add custom binaries to `/usr/local/bin` without interfering with the system's default binaries.

5. **Maintenance and Upgrades**: When binaries are categorized, it simplifies system maintenance and upgrades. You can update system binaries without affecting user applications, and vice versa.

6. **Compatibility**: Different binaries might be compiled for different architectures or purposes. Keeping them separate ensures that the right binaries are used for the right tasks, maintaining system compatibility.

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


kexec

In the context of Debian and Linux, you might be referring to **kexec**.

**kexec** is a system call that allows you to load and boot into another kernel from the currently running kernel without going through the BIOS or firmware initialization. This can significantly reduce the time required for a reboot⁹¹¹. Here's a brief overview of how it works:

1. **Loading the Kernel**: You load the new kernel into memory using the command:
   ```bash
   kexec -l /path/to/kernel --append="command-line-options" --initrd=/path/to/initrd
   ```
   This prepares the new kernel to be booted.

2. **Executing the Kernel**: Once the kernel is loaded, you can boot into it using:
   ```bash
   kexec -e
   ```
   This command will immediately switch to the new kernel.

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

ulimit

Get and set user limits

The `ulimit` command in Linux is a built-in shell command used to control the resources available to the shell and the processes started by it. It allows you to set limits on various system resources, such as the number of open files, the maximum size of files, and the amount of memory a process can use¹².

Here are some common uses of the `ulimit` command:

- **View all current limits**:
  ```bash
  ulimit -a
  ```

- **Set the maximum number of open file descriptors**:
  ```bash
  ulimit -n 1024
  ```

- **Set the maximum size of files created by the shell**:
  ```bash
  ulimit -f 1000
  ```

- **Set the maximum number of processes available to a user**:
  ```bash
  ulimit -u 200
  ```

There are two types of limits you can set with `ulimit`:

1. **Soft limits**: These are the current limits enforced by the kernel for the corresponding resource. They can be increased up to the value of the hard limit.
2. **Hard limits**: These are the maximum limits that can be set for the resource. Only the root user can increase hard limits.

To make these limits permanent, you can add them to the `/etc/security/limits.conf` file¹².


pgrep

SIGTRAP signal

The `SIGTRAP` signal, short for "Signal Trap," is used primarily for debugging purposes in Unix-like operating systems, including Linux. It is sent to a process when an exception or trap occurs, such as when a debugger has requested to be informed of specific conditions¹².

- **Debugging**: It is commonly used by debuggers like `gdb` to set breakpoints or watchpoints. When the program execution reaches a breakpoint, the `SIGTRAP` signal is sent to the process, allowing the debugger to take control and inspect the program's state¹³.
- **Exception Handling**: It can also be triggered by certain exceptions or conditions that the programmer wants to investigate further².
- **Process Control**: When a process receives a `SIGTRAP` signal, it typically stops execution, allowing the debugger to analyze the situation³.

What is a signal in Linux?

In Linux, a signal is a form of inter-process communication used to notify a process that a specific event has occurred. Signals can be sent by the operating system, hardware, or other processes to indicate various conditions or to control the behavior of processes¹².

Here are some key points about signals:

- **Types of Signals**: There are standard signals (like `SIGINT`, `SIGTERM`, `SIGKILL`) and real-time signals. Standard signals are predefined and have specific meanings, while real-time signals are user-defined and can carry additional data¹².
- **Signal Handling**: Each signal has a default action, such as terminating the process, ignoring the signal, or stopping the process. Processes can change the default action by defining custom signal handlers¹³.
- **Common Signals**:
  - `SIGINT` (Interrupt): Sent when the user types Ctrl+C. It usually terminates the process.
  - `SIGTERM` (Terminate): Requests a process to terminate gracefully.
  - `SIGKILL` (Kill): Forces a process to terminate immediately. This signal cannot be caught or ignored².
  - `SIGTRAP`: Used for debugging purposes, such as setting breakpoints³.

- **Sending Signals**: Signals can be sent using commands like `kill`, `pkill`, or `killall`, or programmatically using functions like `raise()` or `kill()`¹².

What is a core dump in Linux?

A core dump in Linux is a file that captures the memory, register values, and call stack of a program at the moment it crashes. This file is automatically generated by the Linux kernel when a program terminates unexpectedly.

- **Purpose**: Core dumps are primarily used for debugging. They provide a snapshot of the program's state at the time of the crash, which can be analyzed to determine the cause of the failure¹².
- **Contents**: The core dump file contains the process's address space (memory), including the values of registers and the call stack²³.
- **Generation**: Core dumps can be triggered by certain signals (e.g., `SIGSEGV` for segmentation faults) or manually using debugging tools³.
- **Configuration**: The behavior of core dumps can be configured using the `kernel.core_pattern` parameter and other settings in `/etc/sysctl.conf` or `/etc/security/limits.conf`¹².


What is soft core in ulimit?

In the context of `ulimit`, the term "soft core" refers to the soft limit on the size of core dumps that can be created by a process. Core dumps are files that capture the memory and state of a process at the time it crashes, which are useful for debugging.

The soft limit is the value that can be changed by the user or processes up to the hard limit. The hard limit, on the other hand, can only be increased by the root user.

To view or set the soft core limit, you can use the `ulimit` command:

- **View the current soft core limit**:
  ```bash
  ulimit -c
  ```

- **Set the soft core limit** (e.g., to 100 MB):
  ```bash
  ulimit -c 100000
  ```

- **Set the soft core limit to unlimited**:
  ```bash
  ulimit -c unlimited
  ```

To make these changes permanent, you can add them to the `/etc/security/limits.conf` file:

```plaintext
* soft core unlimited
```

This configuration will ensure that the soft core limit is set to unlimited for all users.

What is hard limit in ulimit?

In the context of `ulimit`, the "hard limit" is the maximum value that can be set for a particular resource limit. Unlike the soft limit, which can be adjusted by the user or processes up to the hard limit, the hard limit can only be increased by the root user. This ensures that non-privileged users cannot set resource limits beyond what the system administrator has allowed.

Here are some key points about hard limits:

- **Purpose**: Hard limits provide a safeguard to prevent users from consuming excessive system resources, which could affect system stability and performance.
- **Setting Hard Limits**: Hard limits can be set using the `ulimit` command with the `-H` option. For example, to set the maximum number of open file descriptors to 4096:
  ```bash
  sudo ulimit -Hn 4096
  ```

- **Viewing Hard Limits**: You can view the current hard limits by using the `-H` option with `ulimit`:
  ```bash
  ulimit -H -a
  ```

- **Configuration**: To make hard limits permanent, you can add them to the `/etc/security/limits.conf` file. For example:
  ```plaintext
  * hard nofile 4096
  ```


suid

sysctl



