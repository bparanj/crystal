1. Create a IAM role with permissions for EC2, S3 and Secrets manager. Refer [IAM Role](./experiments/iam-role.md)

2. Setup A Record and CNAME Record for clickplan.net and www.clickplan.net. Refer [Domain IP Mapping](./experiments/domain-ip-mapping.md)

- A Record: (./screenshots/a-record.png)
- CNAME Record: (./screenshots/cname-record.png)

3. Setup SSL Certificate for clickplan.net and www.clickplan.net. Refer [Caddy SSL Setup](./experiments/caddy-ssl-setup.md)

4. Provision the EC2 instance with the IAM role in CI/CD pipleline. Refer [Provision EC2 Instance](./provisioner/provisioning-step.md) [Automate after 10 early adopters are onboarded]

5. Download the PEM file for the EC2 instance. Refer [Download PEM File](./experiments/pem-file-dwonloader.md)

## Deployment

1. Run the Rails deploy playbook from the root folder of the Rails project:

```
ansible-playbook -i inventory.ini deploy.yml --extra-vars "rails_master_key=501f054eecfdeab14e455aecd0b73e9e"
```

2. Run Rails playbook to setup Puma service. Refer [Puma](./deployer/puma.md)

```
ansible-playbook -i inventory.ini puma.yml
```

- [Postgresql Database](./deployers/database-permission.md)

## Pending

- Step 1: S3 access for database backups. Revise the [IAM role](./provisioner/iam-user.md) to include S3 access. Refer [hourly backups to S3 bucket](./experiments/hourly-db-backups.md). [Day 2 operations. Postpone to after 10 early adopters are onboarded]

```
FATAL:  Peer authentication failed for user \"deploy\"
```

```
cat /etc/postgresql/16/main/pg_hba.conf
```
