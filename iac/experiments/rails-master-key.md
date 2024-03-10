## Handling the Rails Master Key Securely in a Deployment Pipeline Using Terraform and Ansible

For now, store it in the environment variable.

Postpone the following:

Handling the Rails master key securely in a deployment pipeline using Terraform and Ansible is crucial for maintaining the confidentiality and integrity of your application's secrets. The Rails master key is used to decrypt credentials and other secrets for your application, making its secure management essential. Here's a strategy to manage the Rails master key securely:

### 1. Storing the Master Key Securely

#### Terraform:

Use Terraform to create and manage infrastructure resources securely. While Terraform itself isn't typically used to directly handle application secrets, it can be used to set up infrastructure where secrets can be securely stored (e.g., AWS Secrets Manager, Azure Key Vault).

- **Create a Secrets Manager resource**: Use Terraform to provision a secure storage solution like AWS Secrets Manager or Azure Key Vault.
- **Store the Master Key**: After creating the secrets manager resource, manually add the Rails master key to the secrets manager. Ensure that access to this secret is tightly controlled.

Example Terraform configuration for creating an AWS Secrets Manager secret (the secret value should be inserted manually through the AWS console or CLI after creation):

```hcl
resource "aws_secretsmanager_secret" "rails_master_key" {
  name        = "rails_master_key"
  description = "Holds the Rails master key for the application"
}

# Note: The actual secret value (the master key itself) should be added securely,
# either through the AWS Management Console or using the AWS CLI.
```

#### Ansible:

Ansible can be used to configure your application servers and securely fetch the Rails master key during the deployment process.

- **Fetch the Master Key**: Use an Ansible task to retrieve the Rails master key from the secrets manager during deployment.
- **Template Configuration**: Use the Ansible `template` module or `copy` module to create the `master.key` file on your server with the fetched key as its content, ensuring it's properly secured.

Example Ansible task to fetch the Rails master key from AWS Secrets Manager and create the `master.key` file:

```yaml
- name: Retrieve Rails master key from AWS Secrets Manager
  community.aws.aws_secret:
    name: "rails_master_key"
    region: us-east-1
  register: rails_master_key

- name: Ensure config/credentials directory exists
  ansible.builtin.file:
    path: "/path/to/your/app/config/credentials"
    state: directory
    mode: "0700"

- name: Create master.key file with the retrieved key
  ansible.builtin.copy:
    dest: "/path/to/your/app/config/credentials/master.key"
    content: "{{ rails_master_key.secret }}"
    mode: "0600"
```

### 2. Best Practices

- **Access Control**: Ensure that only necessary personnel and systems have access to the master key. Use IAM roles and policies to restrict access.
- **Audit Logs**: Enable audit logging for access to the secrets manager to monitor for unauthorized access attempts.
- **Encryption in Transit and At Rest**: Ensure that the secrets manager and your deployment process support encryption in transit (e.g., using HTTPS) and at rest.
- **Environment Specific Keys**: If you have multiple environments (e.g., staging, production), consider using separate master keys for each and storing them securely in the secrets manager.

By combining Terraform's infrastructure management capabilities with Ansible's application configuration tools, you can securely manage your Rails master key and other sensitive information, minimizing the risk of exposure.

To ensure that the Rails master key is stored in the customer's AWS account and securely retrieved during deployment with Ansible, you'll need to adjust the setup to interact with the customer's AWS environment. This involves configuring access permissions, potentially using a customer-provided IAM role, and making sure your Ansible playbook is set up to use the correct AWS credentials and region for accessing the AWS Secrets Manager in the customer's account. Here are the changes and considerations:

### 1. Configure AWS Credentials

Ensure that your deployment environment (where Ansible runs) has the necessary AWS credentials to access the customer's AWS Secrets Manager. This can be achieved through several methods:

- **Assuming an IAM Role**: If the customer provides an IAM role with permissions to access the secret, you can configure your environment to assume this role. This is the most secure method, as it does not require the customer to share AWS access keys.

- **AWS Access Keys**: If assuming an IAM role is not feasible, the customer may provide AWS access keys with limited permissions to access the necessary resources. Store these credentials securely in your environment and ensure they are used by Ansible when making AWS API calls.

### 2. Modify the Ansible Playbook

Adjust the Ansible playbook to specify the correct region and, if necessary, the credentials to use when fetching the Rails master key from the AWS Secrets Manager in the customer's account.

If assuming an IAM role, you might need to add steps to your playbook or your CI/CD pipeline to handle the role assumption process before accessing the secret.

Here's an adjusted example that includes a placeholder for setting AWS credentials (if not assuming a role automatically via your environment's IAM role or EC2 role):

```yaml
- name: Setup AWS credentials
  ansible.builtin.set_fact:
    aws_access_key: "{{ customer_aws_access_key }}"
    aws_secret_key: "{{ customer_aws_secret_key }}"
    aws_region: "us-east-1" # Example region, adjust as necessary

- name: Retrieve Rails master key from AWS Secrets Manager in the customer's account
  community.aws.aws_secret:
    name: "rails_master_key"
    region: "{{ aws_region }}"
    aws_access_key: "{{ aws_access_key }}"
    aws_secret_key: "{{ aws_secret_key }}"
  register: rails_master_key

- name: Ensure config/credentials directory exists
  ansible.builtin.file:
    path: "/path/to/your/app/config/credentials"
    state: directory
    mode: "0700"

- name: Create master.key file with the retrieved key
  ansible.builtin.copy:
    dest: "/path/to/your/app/config/credentials/master.key"
    content: "{{ rails_master_key.secret }}"
    mode: "0600"
```

### 3. Security Considerations

- **Least Privilege**: Ensure the IAM role or user has the least privilege necessary, with permissions restricted to only getting the required secret.
- **Secure Credential Management**: If using AWS access keys, ensure they are handled securely and not hard-coded in your playbook. Consider using Ansible Vault to encrypt sensitive variables or CI/CD pipeline secrets management features.
- **Audit and Monitoring**: Recommend to the customer that they enable monitoring and auditing (e.g., AWS CloudTrail) for access to their AWS Secrets Manager to detect unauthorized access attempts.

By carefully managing access permissions and adjusting your deployment process, you can securely access the Rails master key stored in the customer's AWS account, maintaining the security and integrity of the deployment process.

Yes, you can use Ansible Vault instead of AWS Secrets Manager to handle the Rails master key, especially if you prefer to keep the deployment process within Ansible and avoid dependencies on cloud-specific services. Ansible Vault is a feature of Ansible that allows you to keep sensitive data such as passwords or keys in encrypted files, rather than as plaintext in your playbooks or roles.

Here's how you can modify your approach to use Ansible Vault for managing the Rails master key:

### Storing the Master Key with Ansible Vault

1. **Create an Encrypted File with Ansible Vault**:

   - Use `ansible-vault` to create a new encrypted file. This file will contain the Rails master key. You can specify a name for the file, such as `master_key.yml`, and inside the file, you can structure it as a YAML file containing the key.
   - Command to create an encrypted file:
     ```bash
     ansible-vault create master_key.yml
     ```
   - Inside `master_key.yml`, structure it like this:
     ```yaml
     rails_master_key: your_master_key_here
     ```

2. **Accessing the Master Key in Your Ansible Playbook**:

   - When your playbook runs, you can include the encrypted file and use the variable it defines. To include the encrypted file, use the `include_vars` module with the `ansible-vault` tag.
   - Example task to include the encrypted vars:
     ```yaml
     - name: Include the Rails master key
       include_vars:
         file: master_key.yml
         name: master_key
     ```
   - This makes the master key available as a variable (`master_key.rails_master_key`) within your Ansible playbook.

3. **Using the Master Key in Your Deployment**:
   - Use the `copy` module to create the `master.key` file on your server with the content of the `rails_master_key` variable.
   - Example task to create the `master.key` file:
     ```yaml
     - name: Create master.key file with the Rails master key
       ansible.builtin.copy:
         dest: "/path/to/your/app/config/credentials/master.key"
         content: "{{ master_key.rails_master_key }}"
         mode: "0600"
     ```

### Running Your Playbook with Ansible Vault

- When you run your Ansible playbook, you'll need to provide the password for the Ansible Vault encrypted file. You can do this in several ways, such as:
  - Using the `--ask-vault-pass` option, which prompts you to enter the vault password when you run the playbook.
  - Using a password file with the `--vault-password-file` option if you have the vault password stored in a file.

Example command with `--ask-vault-pass`:

```bash
ansible-playbook your_playbook.yml --ask-vault-pass
```

### Considerations

- **Security**: Ensure that the vault password is stored securely and is only accessible to authorized users. The security of your master key depends on the security of the vault password.
- **Version Control**: While it's safe to store the encrypted `master_key.yml` in version control, never store the vault password in version control.
- **Environment Specific Keys**: If you're managing multiple environments (e.g., production, staging), you can create separate encrypted files for each environment's master key or manage them all within a single file with environment-specific variables.

Using Ansible Vault offers a straightforward and integrated way to manage sensitive information such as the Rails master key without relying on external services, making it a suitable approach for scenarios where using cloud-based secrets managers is not preferred or possible.

Yes, Ansible Vault can be used for storing a customer's Rails app master key securely. This method is particularly useful if you manage or deploy Rails applications on behalf of customers and need a secure way to handle sensitive information like the Rails master key. Using Ansible Vault allows you to encrypt the master key file and then use it within your Ansible playbooks without exposing the key in plain text.

Here’s how to adapt the process specifically for handling a customer's Rails app master key:

### 1. Creating an Encrypted Master Key File with Ansible Vault

First, you need to create an encrypted file that will store the Rails master key. You can do this for each customer's Rails application to ensure separation and security of each key:

```bash
ansible-vault create customer_name_master_key.yml
```

Inside this file, you can structure it as follows, replacing `actual_master_key` with the customer's Rails master key:

```yaml
rails_master_key: actual_master_key
```

### 2. Using the Master Key in Deployment

When deploying the customer's Rails application, include the encrypted master key file in your Ansible playbook to set up the `config/credentials/master.key` file on the server:

```yaml
- name: Include the customer's Rails master key
  include_vars:
    file: customer_name_master_key.yml
    name: master_key

- name: Create master.key file on the server
  ansible.builtin.copy:
    dest: "/path/to/customer/app/config/credentials/master.key"
    content: "{{ master_key.rails_master_key }}"
    mode: "0600"
```

### 3. Running Ansible Playbook

When running your Ansible playbook, you'll need to provide the Ansible Vault password. This can be done interactively via `--ask-vault-pass` or automatically via `--vault-password-file` if you're automating deployments:

```bash
ansible-playbook playbook.yml --ask-vault-pass
```

or

```bash
ansible-playbook playbook.yml --vault-password-file /path/to/vault_password_file
```

### Best Practices

- **Secure Vault Password**: The security of the encrypted master key depends on the security of the Ansible Vault password. Ensure this password is stored securely and only accessible to authorized personnel.
- **Separate Vaults**: Use separate vault files for different customers to isolate their sensitive information effectively.
- **Permission Management**: Make sure the `config/credentials/master.key` file has strict file permissions (`0600`) to prevent unauthorized access.
- **Version Control**: It's safe to store the encrypted vault files (`*.yml`) in version control, but never store the vault password in version control.

Using Ansible Vault to manage customer's Rails master keys provides a secure and manageable approach to handling sensitive information across different environments or customer applications. It integrates seamlessly into deployment workflows, ensuring that sensitive keys are encrypted and only accessible to authorized deployment processes and personnel.

Yes, you can use HashiCorp's Vault to store the Ansible Vault password securely. HashiCorp Vault is a tool for secrets management, providing secure access to tokens, passwords, certificates, API keys, and other secrets in modern computing. Integrating HashiCorp Vault with Ansible allows you to enhance the security of your deployment process by securely fetching the Ansible Vault password from HashiCorp Vault at runtime, instead of storing it in a file or entering it manually.

### How to Integrate HashiCorp Vault with Ansible

To use HashiCorp's Vault secrets to store and retrieve the Ansible Vault password, follow these general steps:

#### 1. Store the Ansible Vault Password in HashiCorp Vault

- First, ensure you have HashiCorp Vault installed and properly configured.
- Store your Ansible Vault password in HashiCorp Vault by using the Vault CLI or API. For example:
  ```shell
  vault kv put secret/ansible_vault password='your_ansible_vault_password'
  ```

#### 2. Configure Ansible to Use HashiCorp Vault

- Ansible does not directly integrate with HashiCorp Vault for retrieving the vault password. However, you can use a script or a tool that fetches the password from HashiCorp Vault and then use that password with Ansible.

#### 3. Write a Script to Fetch the Ansible Vault Password

- Write a script in your preferred scripting language (e.g., Bash, Python) that uses HashiCorp Vault's CLI or API to fetch the Ansible Vault password. Here’s a simple example in Bash:
  ```bash
  #!/bin/bash
  vault kv get -field=password secret/ansible_vault
  ```
- Ensure the script has execute permissions and is secure.

#### 4. Use the Script with Ansible Playbook Command

- Use the script to dynamically provide the Ansible Vault password when running your Ansible playbooks. You can use the `--vault-password-file` option in the `ansible-playbook` command to specify your script:
  ```shell
  ansible-playbook playbook.yml --vault-password-file /path/to/your/script.sh
  ```

### Security Considerations

- **Access Control**: Ensure that access to HashiCorp Vault is securely managed and that only authorized users or systems can fetch the Ansible Vault password.
- **Script Security**: The script used to fetch the password should be stored securely and have restricted access to prevent unauthorized use.
- **Audit Logging**: Enable audit logging in HashiCorp Vault to keep a record of who accesses the Ansible Vault password and when.

By using HashiCorp Vault to store the Ansible Vault password, you benefit from a centralized and secure management system for your secrets, reducing the risk associated with storing sensitive information in less secure locations. This approach leverages the strengths of both HashiCorp Vault for secrets management and Ansible for automation, providing a robust solution for managing sensitive data in your infrastructure.

Integrating HashiCorp Vault with GitHub Actions in your CI/CD pipeline allows you to securely fetch secrets, such as the Ansible Vault password, during the CI/CD process. This setup ensures that sensitive information like secrets, tokens, or passwords are securely managed and dynamically accessed during the build or deployment processes.

### Overview

The general approach involves:

1. **Setting up HashiCorp Vault**: Ensure your HashiCorp Vault is properly set up and contains the secrets you want to access, such as the Ansible Vault password.
2. **Configuring GitHub Actions**: Use GitHub Actions to interact with HashiCorp Vault to retrieve the necessary secrets and use them in your CI/CD tasks.

### Steps to Integrate HashiCorp Vault with GitHub Actions

#### 1. Configure HashiCorp Vault Access

Ensure you have a policy and token (or use AppRole, AWS IAM, etc.) in Vault that grants access to the secrets needed by your GitHub Actions workflow. This token or method will be used to authenticate from GitHub Actions to HashiCorp Vault.

#### 2. Store Vault Access in GitHub Secrets

Store your Vault access credentials (like the Vault address, token, or other auth methods) as GitHub Secrets in your repository settings. This ensures they are available to GitHub Actions while keeping them secure.

- Go to your GitHub repository > Settings > Secrets and add your Vault credentials, e.g., `VAULT_ADDR`, `VAULT_TOKEN`.

#### 3. Create a GitHub Action Workflow

In your repository, create a `.github/workflows` directory if it doesn't already exist. Inside, create a YAML file for your workflow (e.g., `ci-cd-pipeline.yml`). In this workflow file, you'll define the steps to install Vault CLI, authenticate to Vault, retrieve the Ansible Vault password, and then use it in your deployment steps.

#### Example Workflow

```yaml
name: CI/CD Pipeline with Vault

on: [push]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      # Step to install Vault CLI
      - name: Install Vault
        run: |
          wget https://releases.hashicorp.com/vault/1.8.4/vault_1.8.4_linux_amd64.zip
          unzip vault_1.8.4_linux_amd64.zip
          sudo mv vault /usr/local/bin/

      # Step to authenticate and retrieve the Ansible Vault password
      - name: Retrieve Ansible Vault Password
        env:
          VAULT_ADDR: ${{ secrets.VAULT_ADDR }}
          VAULT_TOKEN: ${{ secrets.VAULT_TOKEN }}
        run: |
          vault login $VAULT_TOKEN
          vault kv get -field=password secret/ansible_vault > ansible_vault_password.txt

      # Use the Ansible Vault password in your deployment
      - name: Deploy with Ansible
        run: ansible-playbook playbook.yml --vault-password-file ansible_vault_password.txt
```

### Security Considerations

- **Minimal Permissions**: Ensure the Vault policy used by GitHub Actions has the minimal necessary permissions to access only the required secrets.
- **Token Security**: Use dynamic secrets or short-lived tokens when possible. Consider authentication methods like AppRole with GitHub Actions for more secure interactions.
- **Audit Logging**: Ensure Vault's audit log is enabled to track access and usage of secrets by GitHub Actions.

This setup leverages GitHub Actions to dynamically retrieve secrets from HashiCorp Vault, allowing for a secure and automated CI/CD process. By using Vault, you minimize the exposure of sensitive information and adhere to best practices for secrets management in automated workflows.
