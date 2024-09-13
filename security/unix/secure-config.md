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
Device Number




## Terms

- ext4 Format File System
- Boot Partition
- Swap File
- Special Device
- Run Binaries
