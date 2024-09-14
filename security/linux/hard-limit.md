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
