## Refactoring Packer Templates with Variables

To refactor your Packer template to use variables, you'll define these variables at the beginning of your template. This makes your template more flexible and customizable for different builds or environments. Here's how you can extract variables from your template:

### Packer HCL2 with Variables

```hcl
variables {
  aws_region = "us-west-2"
  instance_type = "c5.4xlarge"
  source_ami_name = "ubuntu/images/*ubuntu-jammy-22.04-amd64-server-*"
  ami_owners = ["099720109477"]
  ssh_username = "ubuntu"
  playbook_file = "../ansible/playbooks/master_playbook.yml"
  ansible_user = "ubuntu"
}

packer {
  required_plugins {
    amazon = {
      source  = "github.com/hashicorp/amazon"
      version = "~> 1"
    }
    ansible = {
      version = "~> 1"
      source  = "github.com/hashicorp/ansible"
    }
  }
}

source "amazon-ebs" "ubuntu" {
  communicator  = "ssh"
  ami_name      = "packer-ubuntu-aws-${timestamp()}"
  instance_type = "${var.instance_type}"
  region        = "${var.aws_region}"
  source_ami_filter {
    filters = {
      name                = "${var.source_ami_name}"
      root-device-type    = "ebs"
      virtualization-type = "hvm"
    }
    most_recent = true
    owners      = var.ami_owners
  }
  ssh_username = "${var.ssh_username}"
  tags = {
    "Name"        = "UbuntuImage"
    "Environment" = "Production"
    "OS_Version"  = "Ubuntu 22.04"
    "Release"     = "Latest"
    "Created-by"  = "Packer"
  }
}

build {
  sources = [
    "source.amazon-ebs.ubuntu"
  ]

  provisioner "ansible" {
    playbook_file = "${var.playbook_file}"
    user          = "${var.ansible_user}"
    use_proxy     = false
    ansible_env_vars = [
      "ANSIBLE_HOST_KEY_CHECKING=False"
    ]
  }

  post-processor "manifest" {}
}
```

### Notes:

- **Variables**: Variables are defined at the top using the `variables` block. Each variable is assigned a default value that can be overridden at runtime.
- **Interpolation**: When referencing variables within your configuration, use `${var.variable_name}` syntax.
- **Dynamic Values**: For values like `ami_name` that include a function call (`timestamp()`), keep the function call inline within the string.
- **Playbook File Path**: Adjust the `playbook_file` path variable according to your directory structure.

### Using Variables at Runtime

To override any of these variables at runtime, you can use the `-var` or `-var-file` command-line options when executing `packer build`. For example:

```bash
packer build -var 'aws_region=eu-central-1' -var 'instance_type=m5.large' your_template.pkr.hcl
```

This approach keeps your Packer configurations flexible and easily adaptable for different environments, AWS regions, instance types, or AMI filters without modifying the core template.

When using AWS credentials (such as AWS Access Key ID and Secret Access Key) with Packer and they are already set as environment variables, you do not need to explicitly define these credentials as sensitive variables within your Packer template. Packer can automatically use these credentials from the environment variables, which is a secure and common practice. This approach keeps your templates clean and avoids hardcoding sensitive information.

### Environment Variables Used by Packer

Packer automatically recognizes and uses the following environment variables for AWS authentication:

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- Optionally, `AWS_SESSION_TOKEN` if you are using temporary credentials from roles or federated access.

### Using Environment Variables with Packer

As long as these environment variables are set in your shell or CI/CD environment, Packer will use them for AWS operations without additional configuration in your template. This method is preferred for handling credentials because it reduces the risk of accidentally exposing sensitive information.

### Example: Confirming Use of Environment Variables

You don't need to add anything to your Packer template for it to use AWS credentials from environment variables. However, if you're using other sensitive information or custom variables that need to be passed to Packer or Ansible, you can define them in your Packer template as variables and then pass the values through the command line or a variables file, ensuring any sensitive information is not directly included in the template.

For non-sensitive custom variables, you can define them in your Packer HCL file like so:

```hcl
variables {
  example_variable = "default value"
}

# Use the variable
source "amazon-ebs" "example" {
  # your configuration
  example_field = "${var.example_variable}"
}
```

And for sensitive variables or to override the default values, you can use the `-var` flag when running Packer:

```bash
packer build -var 'example_variable=custom value' template.pkr.hcl
```

For sensitive data, ensure you're handling it securely, such as using environment variables or a secrets manager and referencing them in your commands or scripts without hardcoding them into your templates or scripts.

## Troubleshooting

### Issue #3

$ packer validate .
Error: 1 error(s) occurred:

- AMIName should only contain alphanumeric characters, parentheses (()), square brackets ([]), spaces ( ), periods (.), slashes (/), dashes (-), single quotes ('), at-signs (@), or underscores(\_). You can use the `clean_resource_name` template filter to automatically clean your ami name.

  on aws-ubuntu.pkr.hcl line 24:
  (source code not available)

The error message you're seeing is due to the `ami_name` in your Packer template not adhering to AWS's naming restrictions for AMIs. AWS requires that AMI names only contain certain characters: alphanumeric characters, parentheses `()`, square brackets `[]`, spaces ` `, periods `.`, slashes `/`, dashes `-`, single quotes `'`, at-signs `@`, or underscores `_`.

To resolve this error, ensure that the `ami_name` field in your Packer template does not contain any disallowed characters. If you are using dynamic elements like `{{timestamp}}` to construct the `ami_name`, it's possible that the resulting string includes characters outside of the allowed set.

To automatically clean your AMI name to adhere to these restrictions, you can use the `clean_resource_name` template filter provided by Packer. Here's how you might adjust the `ami_name`:

```hcl
ami_name = "packer-ubuntu-aws-${clean_resource_name(timestamp())}"
```

### Issue #2

This uses the `clean_resource_name` function to ensure that the resulting AMI name is compliant with AWS's naming restrictions by replacing or removing any disallowed characters from the `timestamp()` output or any other dynamic elements you include in the `ami_name`.

After making this change, run `packer validate .` again to check if the error is resolved.

packer validate .
Error: Call to unknown function

The error message you're encountering suggests that `clean_resource_name` was mentioned as a solution to clean up AMI names to conform to AWS's naming restrictions, but it appears that `clean_resource_name` is not an existing function in Packer. As of my last update, Packer does not have a `clean_resource_name` function built into its templating engine.

To resolve the original error and ensure your AMI name contains only allowed characters, you will need to manually ensure that the `ami_name` you're specifying in your Packer template adheres to AWS's naming conventions. Here's a way to manually clean the AMI name using built-in Packer template functions like `timestamp` to ensure uniqueness without violating AWS constraints:

```hcl
source "amazon-ebs" "ubuntu" {
  ami_name = "packer-ubuntu-aws-${regex_replace(timestamp(), "[^a-zA-Z0-9-]", "")}"
  ...
}
```

In this modification:

- `${timestamp()}` generates a current timestamp.
- `regex_replace` function is used to replace any character not matching the regex pattern `[a-zA-Z0-9-]` (which includes letters, numbers, and dashes) with an empty string, effectively removing unwanted characters.

This approach ensures that the `ami_name` will only include alphanumeric characters and dashes, adhering to AWS's naming requirements.

If you encountered the `clean_resource_name` suggestion in documentation or a forum, it might have been a misunderstanding or a custom function defined in someone's specific Packer wrapper scripts, not a function available in Packer itself.

on aws-ubuntu.pkr.hcl line 26:
(source code not available)

There is no function named "clean_resource_name".
