To read 2 TB of data from one SATA3 drive at a time, you can follow these simple steps:

### 1. **Mount the Drive (if needed)**
   - If the drive isn’t automatically mounted, you may need to manually mount it.
   - Identify the drive:
     ```bash
     lsblk
     ```
   - Mount the drive:
     ```bash
     sudo mount /dev/sdX1 /mnt/drive
     ```
     Replace `/dev/sdX1` with your specific drive partition.

### 2. **Copy/Read the Data**
   - Use a command like `cp` or `rsync` to copy data from the drive to your desired location:
     ```bash
     cp -r /mnt/drive /path/to/destination
     ```
   - Alternatively, you can use `dd` to create an image of the drive:
     ```bash
     dd if=/dev/sdX of=/path/to/destination/drive.img bs=4M status=progress
     ```
     Replace `/dev/sdX` with your specific drive identifier.

### 3. **Unmount the Drive**
   - After you finish reading, safely unmount the drive:
     ```bash
     sudo umount /mnt/drive
     ```

You can repeat these steps for each of the drives. This method is straightforward and allows you to handle one drive at a time without needing to manage multiple processes simultaneously.

To connect a SATA3 drive to your Ubuntu ThinkPad laptop, you'll need to use an external connection method since most laptops don’t have direct SATA ports. Here's how you can do it:

### 1. **Using a SATA-to-USB Adapter or Docking Station**
   - **SATA-to-USB Adapter**: This is a simple cable that connects the SATA data and power connectors on your drive to a USB port on your laptop. 
   - **Docking Station**: A docking station usually has multiple slots for different types of drives (e.g., 2.5-inch and 3.5-inch SATA drives) and connects to your laptop via USB.

   **Steps**:
   1. **Connect the Drive**: 
      - Attach the SATA-to-USB adapter or place the drive in the docking station.
      - Connect the USB end to your laptop.

   2. **Power the Drive (if needed)**: 
      - Some adapters or docking stations require an external power source, especially for 3.5-inch drives. Make sure the drive is powered on.

   3. **Verify the Connection**:
      - Open a terminal and run:
        ```bash
        lsblk
        ```
      - Your drive should appear in the list with a device identifier like `/dev/sdX`.

### 2. **Mount the Drive**
   - Once connected, the drive may auto-mount, and you’ll see it in the file manager under "Devices."
   - If not, you can manually mount it:
     ```bash
     sudo mount /dev/sdX1 /mnt/drive
     ```
     Replace `/dev/sdX1` with the correct identifier from the `lsblk` output.

### 3. **Access and Manage the Data**
   - Now, you can access the drive's data through `/mnt/drive` or directly from the file manager.

### 4. **Safely Eject the Drive**
   - Before disconnecting the drive, unmount it to ensure all data operations are complete:
     ```bash
     sudo umount /mnt/drive
     ```
   - Then, safely disconnect the USB adapter or docking station.

This method allows you to connect and manage SATA3 drives easily on your laptop, making it convenient to access large amounts of data or perform backups.
