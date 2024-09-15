## Output AWS Account ID

If you have multiple AWS accounts, it can lead to issues when Terraform creates the resources in a different AWS account. This behaviour occurred after installing AWS CLI. The CLI is useful for troubleshooting. However we must know which account we are using.

## AWS CLI

How to output the account that AWS CLI is using?

To output the AWS account ID that the AWS CLI is currently configured to use, you can run the following command:

```sh
aws sts get-caller-identity --query "Account" --output text
```

This command uses the AWS Security Token Service (STS) to retrieve details about the credentials used to call the AWS CLI,  the account ID. The `--query "Account"` parameter extracts just the account ID from the response, and `--output text` formats the output as plain text.

## Terraform

To output the AWS account ID that Terraform is using to create resources, you can use the `aws_caller_identity` data source provided by the AWS provider. This data source retrieves the caller's identity, which includes the AWS account ID among other details.

First, declare the data source in your Terraform configuration:

```hcl
data "aws_caller_identity" "current" {}
```

Then, you can output the AWS account ID like this:

```hcl
output "aws_account_id" {
  value = data.aws_caller_identity.current.account_id
}
```

Your complete example might look like this:

```hcl
provider "aws" {
  region = "us-west-2"
}

data "aws_caller_identity" "current" {}

output "aws_account_id" {
  value = data.aws_caller_identity.current.account_id
}

# The rest of your Terraform configuration...
```

After applying your Terraform configuration, the output will display the AWS account ID used by Terraform for creating the resources. This way, you can verify that Terraform is operating within the expected AWS account.

Yes, separating concerns by having an `outputs.tf` file for outputs and using the `data` blocks within your `main.tf` (or any other Terraform configuration file) is a good practice for organizing your Terraform code. This makes your infrastructure code more maintainable and easier to understand.

- **Outputs.tf**: This file  contains output variables that you want to display after Terraform applies your configurations. Outputs can be useful for extracting specific values from your resources, like IP addresses, DNS names, etc.

- **Main.tf**: This is often the primary entry file for Terraform configurations. It can include `resource`, `provider`, `variable`, and `data` blocks, among others. Using `data` blocks here allows you to fetch and use information about resources that are either managed outside of Terraform or created in other parts of your Terraform code.

Remember, while separating concerns into different files is a recommended practice, Terraform treats all `.tf` files in a directory as part of the same configuration during an apply or plan. So, how you organize these files is flexible and can be adapted to the needs and scale of your project.

## Terraform and AWS Credentials

Terraform picks up AWS credentials in several ways, and it uses the first method it finds in the following order:

1. **Environment Variables**: Terraform checks for `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`. Optionally, `AWS_SESSION_TOKEN` can also be used if you're leveraging AWS STS for temporary credentials.

2. **The AWS Credentials File**: By default, this file is located at `~/.aws/credentials` on Linux and macOS, or `%UserProfile%\.aws\credentials` on Windows. Terraform uses the `[default]` profile unless a different profile is specified with the `profile` attribute in the provider block or via the `AWS_PROFILE` environment variable.

3. **The AWS Shared Configuration File**: Similar to the credentials file, it's located at `~/.aws/config` on Linux and macOS, or `%UserProfile%\.aws\config` on Windows. This file may also contain credentials information, especially for named profiles that might include region settings alongside.

4. **ECS and EC2 Role**: If Terraform is running on an Amazon ECS task or an EC2 instance, it will use the IAM roles for tasks or the role attached to the EC2 instance profile, respectively.

5. **Explicit Provider Block Configuration**: You can directly specify credentials within the Terraform provider block, although this is not recommended due to the risk of committing sensitive information to source control.

For most scenarios, it's recommended to use environment variables or the AWS credentials file with named profiles to manage different access credentials. This way, you can switch between accounts and roles as necessary without modifying your Terraform configuration.
