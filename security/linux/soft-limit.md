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
