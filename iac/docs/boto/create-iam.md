what is teh boto3 code to create a IAM role with full EC2 access and {
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

policy? 

Here's the boto3 code to create an IAM role with full EC2 access and the specified Secrets Manager policy:

```python
import boto3
import json

iam = boto3.client('iam')

# Create the IAM role
role_name = 'EC2FullAccessRole'
assume_role_policy_document = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "ec2.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}

response = iam.create_role(
    RoleName=role_name,
    AssumeRolePolicyDocument=json.dumps(assume_role_policy_document)
)

role_arn = response['Role']['Arn']

# Attach the EC2FullAccess managed policy to the role
ec2_full_access_policy_arn = 'arn:aws:iam::aws:policy/AmazonEC2FullAccess'
iam.attach_role_policy(
    RoleName=role_name,
    PolicyArn=ec2_full_access_policy_arn
)

# Create the inline policy for Secrets Manager
secrets_manager_policy = {
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

iam.put_role_policy(
    RoleName=role_name,
    PolicyName='SecretsManagerPolicy',
    PolicyDocument=json.dumps(secrets_manager_policy)
)

print(f"IAM role '{role_name}' created with ARN: {role_arn}")
```

This code does the following:

1. We import the necessary modules: `boto3` for interacting with AWS services and `json` for handling JSON data.

2. We create an IAM client using `boto3.client('iam')`.

3. We define the IAM role name (`'EC2FullAccessRole'`) and the assume role policy document that allows EC2 to assume this role.

4. We create the IAM role using `iam.create_role()` with the specified role name and assume role policy document. We capture the role ARN from the response.

5. We attach the `AmazonEC2FullAccess` managed policy to the role using `iam.attach_role_policy()`. This policy grants full access to EC2 services.

6. We define the inline policy for Secrets Manager with the specified actions and resource.

7. We create the inline policy and attach it to the role using `iam.put_role_policy()`.

8. Finally, we print a message indicating that the IAM role has been created along with its ARN.

Make sure to have the necessary AWS credentials configured in your environment before running this code. The IAM user or role associated with the credentials should have the required permissions to create IAM roles and attach policies.

To create an IAM role with full EC2 access and attach a custom policy for specific Secrets Manager actions using `boto3`, you'll need to follow these steps:

1. **Create the IAM Role** with a trust policy that allows EC2 instances to assume this role.
2. **Create a Custom Policy** with the specified permissions for AWS Secrets Manager.
3. **Attach the AWS managed policy for full EC2 access** to the role.
4. **Attach your custom policy** to the role.

Here's how you can do it with `boto3`:

```python
import boto3
import json

# Initialize IAM client
iam = boto3.client('iam')

# Step 1: Create the IAM Role
role_name = "MyEC2FullAccessRole"
assume_role_policy = json.dumps({
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {"Service": "ec2.amazonaws.com"},
            "Action": "sts:AssumeRole"
        }
    ]
})
try:
    role = iam.create_role(
        RoleName=role_name,
        AssumeRolePolicyDocument=assume_role_policy,
        Description="Role with EC2 Full Access and specific Secrets Manager permissions",
    )
    print(f"Role created: {role['Role']['Arn']}")
except Exception as e:
    print(e)

# Step 2: Create the Custom Policy
policy_name = "MySecretsManagerAccessPolicy"
policy_document = json.dumps({
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
})
try:
    policy = iam.create_policy(
        PolicyName=policy_name,
        PolicyDocument=policy_document
    )
    custom_policy_arn = policy['Policy']['Arn']
    print(f"Custom policy created: {custom_policy_arn}")
except Exception as e:
    print(e)

# Step 3: Attach the AWS Managed Policy for Full EC2 Access
try:
    iam.attach_role_policy(
        RoleName=role_name,
        PolicyArn='arn:aws:iam::aws:policy/AmazonEC2FullAccess'
    )
    print("Attached AWS managed policy for EC2 full access to the role.")
except Exception as e:
    print(e)

# Step 4: Attach the Custom Policy to the Role
try:
    iam.attach_role_policy(
        RoleName=role_name,
        PolicyArn=custom_policy_arn
    )
    print("Attached custom Secrets Manager policy to the role.")
except Exception as e:
    print(e)
```

Note:
- Ensure you have the necessary permissions to create roles and policies in IAM.
- Replace `"MyEC2FullAccessRole"` and `"MySecretsManagerAccessPolicy"` with your desired role and policy names.
- The AWS managed policy `AmazonEC2FullAccess` provides full access to EC2. This and the custom policy for Secrets Manager are attached to the newly created role.
