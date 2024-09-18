
denylist policy
allowlist policy

Lateral movement attack

netfilter

auditd tool
remote journaling

syslog
journald

systemd

- init system
- userspace service
- telinit
- system instance
- user instance

systemctl

## telinit

The `telinit` command in Linux is used to change the system's runlevel, which is a state that defines what system services are operating. It is closely linked to the `init` command, which is the first process started by the kernel and is responsible for initializing the system.

### Key Points about `telinit`:

1. **Runlevels**: 
   - **Runlevel 0**: Halt the system.
   - **Runlevel 1**: Single-user mode (maintenance mode).
   - **Runlevel 3**: Multi-user mode without a graphical interface.
   - **Runlevel 5**: Multi-user mode with a graphical interface.
   - **Runlevel 6**: Reboot the system¹.

2. **Usage**: 
   - To change the runlevel, you can use `telinit` followed by the desired runlevel number. For example, `telinit 3` would switch the system to runlevel 3.
   - It sends signals to the `init` process to perform the necessary actions to change the runlevel³.

3. **Systemd**: 
   - In modern Linux distributions that use `systemd` instead of the traditional SysV init system, runlevels are replaced by targets. For example, `runlevel 3` is equivalent to `multi-user.target` in `systemd`².

## System Instance

In Linux, the term **system instance** can refer to a few different concepts depending on the context:

### **Systemd Instance**
- **Definition**: Systemd is a system and service manager for Linux operating systems. It initializes the system and manages system processes after booting. A system instance of systemd is the primary instance that starts during the boot process and manages system-wide services³.
- **Purpose**: It handles the initialization of the system, starting and stopping services, and managing system states.

### **Virtual Machine Instance**
- **Definition**: In the context of virtualization, a system instance can refer to a virtual machine (VM) instance. This is a virtualized environment that runs its own operating system and applications, isolated from the host system.
- **Purpose**: VMs are used to run multiple operating systems on a single physical machine, providing flexibility and efficient resource utilization².

### **Container Instance**
- **Definition**: A container instance refers to a lightweight, standalone, and executable package that includes everything needed to run a piece of software, including the code, runtime, system tools, libraries, and settings.
- **Purpose**: Containers are used to deploy applications consistently across different environments, ensuring that they run the same way regardless of where they are deployed.

## User Instance

In Linux, a **user instance** typically refers to a specific instance of a user account or a user session. Here are a couple of contexts where this term might be used:

### **User Account Instance**
- **Definition**: This is an individual user account created on the system. Each user account has unique properties such as a username, user ID (UID), group ID (GID), home directory, and default shell.
- **Purpose**: User accounts are used to manage permissions and access control, ensuring that each user has the appropriate level of access to system resources¹.

### **User Session Instance**
- **Definition**: This refers to an active session where a user is logged into the system. Each session can be tracked and managed independently.
- **Purpose**: User sessions allow multiple users to be logged in simultaneously, each with their own environment and processes².

## Userspace Service

In Linux, a **userspace service** refers to any service or process that runs outside the kernel space, in the user space. User space is the memory area where application software and some system services execute, typically with less privilege than the kernel. This separation helps ensure system stability and security by preventing user applications from directly accessing critical system resources.

1. **Isolation**: Each userspace process runs in its own virtual memory space, which prevents it from interfering with other processes or the kernel¹.
2. **Interaction with Kernel**: Userspace services interact with the kernel through system calls, which are functions provided by the kernel to perform operations like file manipulation, process control, and network communication².
3. **Examples**: Common examples of userspace services include system daemons like `sshd` (for SSH access), `httpd` (web server), and `cron` (task scheduler)³.

## Service vs Process

While the terms "service" and "process" are related, they refer to different concepts in the context of operating systems like Linux:

### **Process**
- **Definition**: A process is an instance of a running program. It includes the program code and its current activity.
- **Characteristics**: Processes have their own memory space and system resources. They can be in various states such as running, waiting, or terminated.
- **Examples**: When you open a text editor or a web browser, each instance is a separate process.

### **Service**
- **Definition**: A service is a type of process that runs in the background and performs specific functions, often without direct user interaction.
- **Characteristics**: Services are typically started at boot time and run continuously to provide system functionalities like networking, logging, or scheduling tasks.
- **Examples**: Common services include `sshd` (for SSH access), `httpd` (web server), and `cron` (task scheduler).

In summary, while all services are processes, not all processes are services. Services are specialized processes designed to run in the background and provide ongoing system functions.

## Requires and Conflicts Relationships

Yes, it is possible to capture the "requires" and "conflicts" relationships between objects in a graph. This can be done using concepts from graph theory, particularly through the use of directed and undirected graphs.

### **Requires Relationship**
- **Directed Graphs**: A directed graph (or digraph) can represent "requires" relationships. In this type of graph, each edge has a direction, indicating dependency. For example, if object A requires object B, there would be a directed edge from A to B.

### **Conflicts Relationship**
- **Undirected Graphs**: An undirected graph can represent "conflicts" relationships. In this type of graph, edges have no direction, indicating mutual exclusivity or conflict. For example, if object A conflicts with object B, there would be an undirected edge between A and B.

### **Graph Coloring**
- **Adjacency and Conflicts**: In graph coloring, vertices represent objects, and edges represent conflicts. The goal is to color the vertices such that no two adjacent vertices (conflicting objects) share the same color¹. This concept can be extended to capture conflicts in various applications, such as scheduling and resource allocation.

### **Example**
Imagine you have a set of tasks where some tasks depend on others (requires relationship) and some tasks cannot be performed simultaneously (conflicts relationship). You can represent this scenario using a graph:
- **Vertices**: Represent tasks.
- **Directed Edges**: Represent dependencies (requires relationship).
- **Undirected Edges**: Represent conflicts.

