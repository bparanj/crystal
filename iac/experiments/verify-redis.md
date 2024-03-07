To manually verify that specific Redis commands (`FLUSHDB`, `FLUSHALL`, `KEYS`) are disabled on a terminal, you can directly attempt to execute these commands via the Redis CLI and observe the responses. When a command is disabled in Redis (often done for security reasons by renaming the command to an empty string), attempting to execute it should result in an error message indicating that the command is not allowed or does not exist.

Here's how to proceed:

### 1. Connect to Redis

First, connect to your Redis instance using the Redis CLI. If Redis is running on the same machine and using the default port, you can simply run:

```sh
redis-cli
```

If Redis is running on a different host or port, you might connect with:

```sh
redis-cli -h <host> -p <port>
```

### 2. Attempt to Execute the Disabled Commands

Once connected, try executing each of the commands you've disabled. For example:

```sh
FLUSHDB
```

```sh
FLUSHALL
```

```sh
KEYS *
```

### Expected Responses

If the commands have been successfully disabled (renamed to an empty string or another unknown command), Redis should return an error similar to:

```
(error) ERR unknown command `FLUSHDB`, with args beginning with:
```

### Note on Security

Disabling sensitive commands in Redis, especially in production environments, is a common security practice to mitigate risks associated with accidental or malicious data loss. However, remember that disabling commands does not eliminate all security risks, and access to the Redis server should still be tightly controlled and monitored.

### Verifying Renamed Commands

If you've renamed the commands to something other than an empty string (for example, `FLUSHDB` to `FLUSHDB_DISABLED`), you can verify the renaming by attempting to use the new command name. If you don't remember the new names, reviewing the Redis configuration file (`redis.conf`) or checking your deployment automation scripts (Ansible playbook in your case) would be necessary to find out the new command names.

### Conclusion

By following these steps, you can manually verify that specific Redis commands have been disabled as intended. This manual verification process can be an important part of your security audit or routine maintenance checks.
