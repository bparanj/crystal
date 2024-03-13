## Desired Server State

### Goss Supported Resources

| Name         | Description                                           |
| ------------ | ----------------------------------------------------- |
| package      | Add new package                                       |
| file         | Add new file                                          |
| addr         | Add new remote address:port - ex: google.com:80       |
| port         | Add new listening [protocol]:port - ex: 80 or udp:123 |
| service      | Add new service                                       |
| user         | Add new user                                          |
| group        | Add new group                                         |
| command      | Add new command                                       |
| dns          | Add new DNS                                           |
| process      | Add new process name                                  |
| kernel-param | Add new kernel parameter                              |
| mount        | Add new mount                                         |
| interface    | Add new network interface                             |
| http         | Add new network HTTP URL with proxy support           |
| goss         | Add new Goss file, it will be imported from this one  |
| matching     | Test for matches in supplied content                  |

### Packages

| Name             | Version                                                                                  |
| ---------------- | ---------------------------------------------------------------------------------------- |
| Goss             | 0.4.4                                                                                    |
| Caddy            | 2.7.6                                                                                    |
| PostgreSQL       | psql (PostgreSQL) 16.2 (Ubuntu 16.2-1.pgdg22.04+1)                                       |
| Redis            | Redis server v=7.2.4 sha=00000000:0 malloc=jemalloc-5.3.0 bits=64 build=4a33ab3ec422ece7 |
| curl             | PENDING VERSION                                                                          |
| build-essential  | PENDING VERSION                                                                          |
| git              | (depends on installed version)                                                           |
| autoconf         | (depends on installed version)                                                           |
| bison            | (depends on installed version)                                                           |
| build-essential  | (depends on installed version)                                                           |
| libssl-dev       | (depends on installed OpenSSL version)                                                   |
| libyaml-dev      | (depends on installed version)                                                           |
| libreadline6-dev | (depends on installed version)                                                           |
| zlib1g-dev       | (depends on installed version)                                                           |
| libncurses5-dev  | (depends on installed version)                                                           |
| libffi-dev       | (depends on installed version)                                                           |
| libgdbm6         | (depends on installed version)                                                           |
| libgdbm-dev      | (depends on installed version)                                                           |
| libdb-dev        | (depends on installed version)                                                           |
| libpq-dev        | (depends on installed version)                                                           |
| pg               | (depends on installed version, usually related to PostgreSQL client tools)               |

The packages playbook must use this table. Pending task:

- Remove unnecessary packages from the packages playbook.

### Services

| Name     | Port           |
| -------- | -------------- |
| sshd     | 22 (default)   |
| fail2ban | 22 (default)   |
| caddy    | 80, 443        |
| postgres | 5432           |
| redis    | 6379           |
| goss     | 8080           |
| rails    | 3000 (default) |
