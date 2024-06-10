## The Production-Grade Infrastructure Checklist

| Task              | Description                                                                                                                               | Tools                          |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| Install           | Install the software binaries and all dependencies.                                                                                       | Bash, Ansible, Docker, Packer  |
| Configure         | Configure the software at runtime. Includes port settings, TLS certs, service discovery, leaders, followers, replication, etc.            | Chef, Ansible, Kubernetes      |
| Provision         | Provision the infrastructure. Includes servers, load balancers, network configuration, firewall settings, IAM permissions, etc.           | Terraform, CloudFormation      |
| Deploy            | Deploy the service on top of the infrastructure. Roll out updates with no downtime. Includes blue-green, rolling, and canary deployments. | ASG, Kubernetes, ECS           |
| High availability | Withstand outages of individual processes, servers, services, datacenters, and regions.                                                   | Multi-datacenter, multi-region |
| Scalability       | Scale up and down in response to load. Scale horizontally (more servers) and/or vertically (bigger servers).                              | Auto scaling, replication      |
| Performance       | Optimize CPU, memory, disk, network, and GPU usage. Includes query tuning, benchmarking, load testing, and profiling.                     | Dynatrace, Valgrind, VisualVM  |
| Networking        | Configure static and dynamic IPs, ports, service discovery, firewalls, DNS, SSH access, and VPN access.                                   | VPCs, firewalls, Route 53      |
| Security          | Encryption in transit (TLS) and on disk, authentication, authorization, secrets management, server hardening.                             | ACM, Let’s Encrypt, KMS, Vault |
| Metrics           | Availability metrics, business metrics, app metrics, server metrics, events, observability, tracing, and alerting.                        | CloudWatch, Datadog            |
| Logs              | Rotate logs on disk. Aggregate log data to a central location.                                                                            | Elastic Stack, Sumo Logic      |
| Data backup       | Make backups of DBs, caches, and other data on a scheduled basis. Replicate to separate region/account.                                   | AWS Backup, RDS snapshots      |
| Cost optimization | Pick proper Instance types, use spot and reserved Instances, use auto scaling, and clean up unused resources.                             | Auto scaling, Infracost        |
| Documentation     | Document your code, architecture, and practices. Create playbooks to respond to incidents.                                                | READMEs, wikis, Slack, IaC     |
| Tests             | Write automated tests for your infrastructure code. Run tests after every commit and nightly.                                             | Terratest, tflint, OPA, InSpec |
