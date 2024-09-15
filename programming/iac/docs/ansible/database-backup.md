To create a CRON job that makes a PostgreSQL database backup every midnight using an Ansible playbook, you can follow these steps:

1. Create a new playbook file (e.g., `postgres_backup.yml`) with the following content:

```yaml
---
- hosts: all
  become: yes
  
  vars:
    backup_dir: /var/backups/postgres
    db_name: your_database_name
    db_user: your_database_user
    db_password: your_database_password
  
  tasks:
    - name: Install required packages
      apt:
        name:
          - cron
          - postgresql
          - postgresql-client
        state: present

    - name: Create backup directory
      file:
        path: "{{ backup_dir }}"
        state: directory
        owner: postgres
        group: postgres
        mode: '0755'

    - name: Create a CRON job for PostgreSQL backup
      cron:
        name: "Backup PostgreSQL database every midnight"
        minute: "0"
        hour: "0"
        job: >
          /usr/bin/pg_dump -U {{ db_user }} -Fc {{ db_name }} > {{ backup_dir }}/{{ db_name }}_`date +\%Y-\%m-\%d_\%H-\%M-\%S`.dump
        state: present
        user: postgres

    - name: Set PostgreSQL user password
      postgresql_user:
        name: "{{ db_user }}"
        password: "{{ db_password }}"
      become_user: postgres
```

2. Explanation of the playbook:
   - The `hosts` parameter specifies the target hosts where the CRON job will be set up. You can replace `all` with a specific group or host name.
   - The `become` parameter is set to `yes` to run the tasks with sudo privileges.
   - The `vars` section defines variables for the backup directory, database name, database user, and password. Replace the values with your  database details.
   - The first task ensures that the required packages (`cron`, `postgresql`, and `postgresql-client`) are installed using the `apt` module.
   - The second task creates the backup directory specified in the `backup_dir` variable using the `file` module. It sets the ownership and permissions for the directory.
   - The third task creates the CRON job using the `cron` module:
     - `name` is a descriptive name for the CRON job.
     - `minute` and `hour` specify the schedule for the job. In this case, it will run every midnight (0 minute, 0 hour).
     - `job` contains the command to be executed by the CRON job. It uses `pg_dump` to create a compressed backup of the specified database and saves it in the backup directory with a timestamp in the filename.
     - `state` is set to `present` to ensure the CRON job is created.
     - `user` is set to `postgres` to run the CRON job as the PostgreSQL user.
   - The fourth task sets the password for the PostgreSQL user specified in the `db_user` variable using the `postgresql_user` module.

3. Save the playbook file.

4. Run the playbook using the following command:

```
ansible-playbook postgres_backup.yml
```

Make sure you have Ansible installed and configured to connect to the target host(s) where PostgreSQL is running.

5. After running the playbook, the CRON job will be set up on the specified host(s). It will run every midnight and create a compressed backup of the specified PostgreSQL database in the backup directory.

You can check the backup directory to verify that the backups are being created as expected.

You have now created a CRON job using Ansible

**Alternative**

To create a CRON job that performs a PostgreSQL database backup every midnight using an Ansible playbook, you need to ensure that the backup script is correctly set up and that your playbook manages the CRON job effectively. Below is a detailed guide on how to achieve this:

### Step 1: Create the Backup Script
Before setting up the CRON job, you should have a script that performs the PostgreSQL backup. Below is a simple example of a bash script that backs up a PostgreSQL database. Save this script on the server where the database resides, such as `/usr/local/bin/pg_backup.sh`.

```bash
#!/bin/bash
# PostgreSQL Database backup script

# Set these variables
PGUSER="dbuser"
PGPASSWORD="dbpassword"
PGHOST="localhost"
PGPORT="5432"
DATABASE="dbname"
BACKUP_DIR="/path/to/your/backup/directory"
DATE=$(date +"%Y%m%d%H%M")

# Perform the backup
pg_dump -U $PGUSER -h $PGHOST -p $PGPORT $DATABASE | gzip > "$BACKUP_DIR/db-$DATE.gz"

# Ensure permissions are set for security
chmod 600 "$BACKUP_DIR/db-$DATE.gz"
```

Make sure to replace `dbuser`, `dbpassword`, `localhost`, `5432`, `dbname`, and `/path/to/your/backup/directory` with your  PostgreSQL credentials and desired backup directory.

### Step 2: Make the Backup Script Executable
On the server, set the script to be executable:
```bash
chmod +x /usr/local/bin/pg_backup.sh
```

### Step 3: Create Ansible Playbook
Now, create an Ansible playbook that sets up a CRON job for this script. Below is an example of a playbook named `setup_pg_backup_cron.yml`:

```yaml
---
- name: Setup PostgreSQL Database Backup Cron Job
  hosts: all
  become: yes  # Run tasks as sudo

  tasks:
    - name: Ensure cron is installed (Ubuntu)
      ansible.builtin.apt:
        name: cron
        state: present

    - name: Setup daily database backup cron job
      ansible.builtin.cron:
        name: "Daily PostgreSQL Backup"
        job: "/usr/local/bin/pg_backup.sh > /dev/null 2>&1"
        minute: "0"
        hour: "0"
        user: root
        state: present
```

This playbook does the following:
- Ensures the `cron` package is installed on Ubuntu.
- Sets up a CRON job that runs at midnight every day (`minute: "0"`, `hour: "0"`), executing the backup script.

### Step 4: Run the Playbook
Execute the playbook using the following command:

```bash
ansible-playbook setup_pg_backup_cron.yml -i your_inventory_file
```

Replace `your_inventory_file` with the path to your inventory file or specify your host list.

This setup ensures your PostgreSQL database is backed up every midnight, and the backups are stored securely with the correct permissions. Make sure the server has enough disk space to store the backups and consider setting up a mechanism to manage old backups to avoid filling up the disk space.