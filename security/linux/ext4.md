### What is ext4 in Linux?

**ext4** (fourth extended filesystem) is a journaling file system used in Linux. It is the successor to ext3 and offers several improvements in terms of performance, reliability, and features.

### Key Features of ext4:

1. **Backward Compatibility**:
   - ext4 is backward compatible with ext3 and ext2, meaning it can read and mount ext3 and ext2 file systems.

2. **Journaling**:
   - Like ext3, ext4 is a journaling file system, which helps to protect the integrity of the data by keeping a record of changes that will be made to the files. This journal can quickly restore the system to a consistent state in case of a crash or power failure.

3. **Extents**:
   - Ext4 uses extents to improve the performance of large files. An extent is a range of contiguous physical blocks, making it more efficient to store large files and reducing fragmentation.

4. **Delayed Allocation**:
   - This feature improves performance and reduces fragmentation by delaying the allocation of disk blocks until data is actually written to the disk.

5. **Multiblock Allocation**:
   - Allows for allocating multiple blocks at once, improving the performance of operations that require writing a lot of data.

6. **64-bit File System Support**:
   - ext4 supports very large volumes and files, with maximum file size up to 16 TiB and a single volume size up to 1 EiB (exabyte).

7. **Improved Timestamp Support**:
   - ext4 extends timestamps to store the creation time of files, which ext3 did not support.

### Why is it Named ext4?

The name "ext4" stands for the **fourth extended filesystem**. It follows the naming convention of its predecessors:
- **ext**: The original extended filesystem.
- **ext2**: The second extended filesystem, which introduced several improvements over ext.
- **ext3**: The third extended filesystem, which introduced journaling.
- **ext4**: The fourth extended filesystem, which builds on ext3 with additional performance enhancements, features, and improved scalability.

The numerical sequence in the name reflects the evolution and enhancements introduced with each new version of the extended filesystem.

### Sources:
1. **Kernel.org Documentation**:
   - Provides detailed technical documentation and explanations about ext4 and other filesystems in the Linux kernel.
   - [ext4 Filesystem on Kernel.org](https://www.kernel.org/doc/html/latest/filesystems/ext4/index.html)

2. **Red Hat Documentation**:
   - Offers comprehensive guides and information on managing ext4 filesystems within Red Hat Enterprise Linux.
   - [Red Hat Documentation on ext4](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/storage_administration_guide/ch-ext4)

3. **Arch Linux Wiki**:
   - Contains practical information on setting up and using ext4 in Linux.
   - [Arch Linux Wiki: ext4](https://wiki.archlinux.org/title/ext4)

4. **"Linux Kernel Development" by Robert Love**:
   - This book provides insights into the development and functionality of the Linux kernel, including file systems like ext4.

ext4 improves the performance, reliability, and scalability of file storage in Linux systems. The name signifies its place as the latest iteration in the extended filesystem series, building on the capabilities of its predecessors.
