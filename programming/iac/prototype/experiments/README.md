## Health Check

```
curl http://localhost:8080/healthz | jq .
```

## Goss Test Setup

- Review the Packer and Terraform template
- Manually run goss autoadd on the server.
- Copy the generated file on the server to tests/goss.yaml file in the project

## Tasks

- Update the steps for different stages: Base Image, Custom Image and Provisioning
- Remove hard-coded AWS Secrets id in javascript/keyDownload.js
- Update goss.yaml by running goss autoadd for all services (after the image creation by Packer stabilizes)
- Update the inventory_file with the public static IP of EC2 instance and the port number where sshd is running
