What is extended type device?

In Debian, an "extended type device" typically refers to an **extended partition**. Here's a brief overview:

### **Extended Partition**
- **Purpose**: Allows you to bypass the limitation of having only four primary partitions on a disk.
- **Structure**: An extended partition acts as a container for multiple **logical partitions**.
- **Usage**: Useful when you need more than four partitions on a disk. You can create one extended partition and then create multiple logical partitions within it.

### **Creating and Managing Extended Partitions**
- **Tools**: Common tools for managing partitions include `fdisk`, `parted`, and `gparted`.
- **Commands**: Using `fdisk`, you can create an extended partition by selecting the partition type as "extended" during the partition creation process.
