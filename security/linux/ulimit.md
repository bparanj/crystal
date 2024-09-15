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

To make these limits permanent, you can add them to the `/etc/security/limits.conf` file.
