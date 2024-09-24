## Userspace Service

In Linux, a **userspace service** refers to any service or process that runs outside the kernel space, in the user space. User space is the memory area where application software and some system services execute, typically with less privilege than the kernel. This separation provides system stability and security by preventing user applications from directly accessing critical system resources.

1. **Isolation**: Each userspace process runs in its own virtual memory space, which prevents it from interfering with other processes or the kernel.
2. **Interaction with Kernel**: Userspace services interact with the kernel through system calls, which are functions provided by the kernel to perform operations like file manipulation, process control, and network communication.

Examples of userspace services include system daemons like `sshd` (for SSH access), `httpd` (web server), and `cron` (task scheduler).

## Terms

- Kernel Space
- User Space
- Virtual Memory Space
- System Call
