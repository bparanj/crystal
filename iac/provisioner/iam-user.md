## IAM User with EC2 Full Access and Secrets Manager Access

To create an IAM role with policies granting EC2 full access and specific access to AWS Secrets Manager via Terraform, follow these steps. This setup will allow you to programmatically provision these roles for customers upon signup.

### Step 1: Define the IAM Role and Policies in Terraform

Create a Terraform configuration file, e.g., `iam_role.tf`, and define an IAM role along with two policy attachments: one for EC2 full access and another for AWS Secrets Manager access.

```hcl
resource "aws_iam_role" "customer_role" {
  name = "customer_ec2_secrets_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "ec2.amazonaws.com"
        }
      },
    ]
  })
}

resource "aws_iam_policy" "secrets_policy" {
  name   = "customer_secrets_policy"
  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "secretsmanager:CreateSecret",
        "secretsmanager:DescribeSecret",
        "secretsmanager:GetSecretValue",
        "secretsmanager:ListSecretVersionIds",
        "secretsmanager:ListSecrets",
        "secretsmanager:GetResourcePolicy",
        "secretsmanager:DeleteSecret",
        "secretsmanager:PutSecretValue"
      ],
      "Resource": "*"
    }
  ]
}
EOF
}

resource "aws_iam_role_policy_attachment" "ec2_full_access" {
  role       = aws_iam_role.customer_role.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonEC2FullAccess"
}

resource "aws_iam_role_policy_attachment" "secrets_access" {
  role       = aws_iam_role.customer_role.name
  policy_arn = aws_iam_policy.secrets_policy.arn
}
```

### Step 2: Initialize and Apply Your Terraform Configuration

1. **Initialize Terraform** (if you haven't already done so for your project):

```bash
terraform init
```

2. **Apply the Configuration**:

```bash
terraform apply
```

Confirm the action when prompted by Terraform. This will create the IAM role with EC2 full access and the specified Secrets Manager access.

### Additional Notes

- **Customization**: You might want to customize the role and policy names or include additional policies based on your specific requirements.
- **Resource Tagging**: Consider adding tags to your resources for better management and cost tracking, especially if creating these resources for multiple customers.
- **Security Best Practices**: Always follow the principle of least privilege. If your use case does not require full EC2 access or if you can limit Secrets Manager actions to specific resources, adjust the policies accordingly.
- **IAM Role Trust Relationship**: The `assume_role_policy` in the `aws_iam_role` resource allows EC2 service to assume this role. Adjust this policy if the role will be assumed by other services or entities.

This setup provides a foundation for provisioning IAM roles with specific permissions as part of your customer onboarding process using Terraform.
