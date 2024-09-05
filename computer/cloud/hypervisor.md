Your understanding is generally correct, but let's break it down further for clarity:

1. Operating System and CPU sharing:
   You're correct that the operating system manages the CPU in a way that allows multiple applications to share it. This is done through a process called time-sharing or multitasking. The OS rapidly switches between different applications, giving each a slice of CPU time, creating the illusion that multiple programs are running simultaneously.

2. Hypervisor and resource sharing:
   You're also correct about the hypervisor. A hypervisor is a software layer that allows multiple virtual machines (VMs) to run on a single physical machine. It indeed manages and shares physical resources like CPU, memory, storage, and network interfaces among these VMs.

3. Virtualization of physical components:
   Your understanding here is spot-on. Virtualization technology allows the creation of multiple virtual instances of hardware components that map to a single physical component. This applies to various resources:

   - CPU: A single physical CPU can be divided into multiple virtual CPUs.
   - Memory: Physical RAM can be partitioned and allocated to different VMs.
   - Storage: A single physical hard drive can be divided into multiple virtual disks.
   - Network: A single physical network interface can be used to create multiple virtual network interfaces.

This ability to create multiple virtual components from a single physical component is one of the key benefits of virtualization. It allows for more efficient use of hardware resources and greater flexibility in resource allocation.

