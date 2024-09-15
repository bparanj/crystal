## Introduction

I have multiple AWS accounts for experimentation purposes. This makes it easy to manually cleanup the resources after I am done with them. This keeps the AWS bills low. I also don't have worry about accidentally deleting things from the wrong account.

Sometimes, I run into issues when I am checking the AWS console for the resources I created using Packer. The Packer build succeeds but the resources are not visible in the AWS console. Because I was looking at the wrong AWS account. I had to login to the AWS account that Packer was using to build the image.

## Packer Credentials

Packer does not display the AWS credentials it uses for operations like connecting to EC2 instances due to security reasons. Exposing credentials in logs or console output can pose a significant security risk. However, understanding which credentials Packer is using can be important for troubleshooting and ensuring your builds use the correct AWS account and permissions.

Here are a few methods to verify which AWS credentials Packer is using:

### 1. **Environment Variables**

Packer uses the AWS SDK for Go, which looks for credentials in a specific order,  environment variables such as `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`. You can check which credentials are set in your environment by running the following commands in your terminal (not recommended in shared or public environments due to security concerns):

```bash
echo $AWS_ACCESS_KEY_ID
echo $AWS_SECRET_ACCESS_KEY
```

This method displays the values directly, which can confirm what Packer might be using if it's relying on environment variables.

### 2. **CLI Debug Mode**

Running Packer in debug mode may indirectly hint at which credentials or profiles it's using based on the actions it takes. Use the `-debug` flag to run Packer in debug mode:

```bash
packer build -debug your-template.pkr.hcl
```

### 3. **AWS CLI or SDKs**

If you're unsure which credentials Packer is using and you have multiple profiles configured, you can use the AWS CLI or SDKs to list the current user. This method requires that the same credentials or profile Packer is presumed to be using are also set for the AWS CLI:

```bash
aws sts get-caller-identity
```

This command returns the AWS account number, user ID, and ARN associated with the current credentials, helping you identify which credentials are active.

### 4. **AWS Configuration and Credentials Files**

Packer can use the AWS credentials file (`~/.aws/credentials`) and the configuration file (`~/.aws/config`) when environment variables are not set. Review these files to see the configured profiles and credentials. Packer will use the `[default]` profile unless otherwise specified by the `profile` key in your Packer template:

```hcl
source "amazon-ebs" "example" {
  ...
  profile = "your-profile-name"
}
```

### 5. **Explicit Packer Template Configuration**

Check your Packer template for a specified `profile` attribute within your builder configuration. If present, Packer uses this profile from your AWS credentials/configuration files:

```hcl
source "amazon-ebs" "example" {
  profile = "example-profile"
  ...
}
```

This explicitly tells you which profile Packer is attempting to use, and you can cross-reference this with your AWS credentials and config files.

### Security Note:

Be cautious with AWS credentials; never echo or log them in an unsecured manner. Always use IAM roles and policies to adhere to the principle of least privilege, ensuring that the credentials Packer uses have only the permissions necessary to perform the required actions.
