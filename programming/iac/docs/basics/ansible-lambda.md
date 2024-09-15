No, you don't need to install Ansible on the Lambda runtime system to run Ansible playbooks. Instead, you can package Ansible and its dependencies within the Lambda function itself.

Here's an approach you can follow to run Ansible playbooks from an AWS Lambda function:

1. Create a new directory for your Lambda function and navigate to it.

2. Create a virtual environment for your Lambda function:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install Ansible and any other required dependencies in the virtual environment:
   ```
   pip install ansible boto3
   ```

4. Create a `requirements.txt` file with the installed dependencies:
   ```
   pip freeze > requirements.txt
   ```

5. Write your Lambda function code to run the Ansible playbook. Here's an example:
   ```python
   import os
   import boto3
   from ansible.playbook import PlaybookExecutor
   from ansible.inventory.manager import InventoryManager
   from ansible.vars.manager import VariableManager
   from ansible.executor.playbook_executor import PlaybookExecutor
   
   def lambda_handler(event, context):
       # Set up Ansible inventory
       inventory = InventoryManager(loader=None, sources=['localhost'])
       
       # Set up Ansible variables
       variable_manager = VariableManager(loader=None, inventory=inventory)
       
       # Set up Ansible playbook
       playbook_path = 'path/to/your/playbook.yml'
       
       # Set up Ansible executor
       executor = PlaybookExecutor(
           playbooks=[playbook_path],
           inventory=inventory,
           variable_manager=variable_manager,
           loader=None,
           passwords=None
       )
       
       # Execute the Ansible playbook
       result = executor.run()
       
       return result
   ```

6. Bundle the Lambda function code, Ansible playbook, and dependencies into a deployment package:
   ```
   zip -r lambda_function.zip lambda_function.py playbook.yml requirements.txt venv/lib/python3.8/site-packages/
   ```

7. Create an IAM role for the Lambda function with the necessary permissions to access the required AWS resources (e.g., EC2 instances).

8. Create a new Lambda function and upload the `lambda_function.zip` deployment package.

9. Set the appropriate handler for the Lambda function (e.g., `lambda_function.lambda_handler`).

10. Configure the Lambda function's environment variables, timeout, and other settings as needed.

By packaging Ansible and its dependencies within the Lambda function deployment package, you can run Ansible playbooks directly from the Lambda function without the need to install Ansible on the Lambda runtime system.

Keep in mind that running Ansible playbooks from a Lambda function has some limitations and considerations, such as the Lambda execution time limit, the size of the deployment package, and the need to manage Ansible inventory and variables within the Lambda function.

Additionally, make sure to grant the necessary permissions to the Lambda function's IAM role to access the target instances or resources on which the Ansible playbook will be executed.

Here's an updated example of how you can include the Ansible playbooks from your ansible/playbooks folder in the Lambda function deployment package using the AWS CDK with Python:

```python
from aws_cdk import (
    aws_lambda as lambda_,
    aws_iam as iam,
    core,
)
import os

class AnsibleLambdaStack(core.Stack):
    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        # Create an IAM role for the Lambda function
        lambda_role = iam.Role(
            self,
            "AnsibleLambdaRole",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
        )
        
        # Grant necessary permissions to the Lambda role
        lambda_role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name("AmazonEC2FullAccess")
        )
        
        # Create a Lambda function
        ansible_lambda = lambda_.Function(
            self,
            "AnsibleLambda",
            code=lambda_.Code.from_asset("lambda"),
            handler="lambda_function.lambda_handler",
            runtime=lambda_.Runtime.PYTHON_3_8,
            role=lambda_role,
            timeout=core.Duration.seconds(900),  # Adjust timeout as needed
        )
        
        # Include Ansible playbooks in the Lambda function deployment package
        playbooks_dir = os.path.abspath("ansible/playbooks")
        for root, dirs, files in os.walk(playbooks_dir):
            for file in files:
                if file.endswith(".yml") or file.endswith(".yaml"):
                    playbook_path = os.path.join(root, file)
                    ansible_lambda.add_to_asset_hash(playbook_path)

app = core.App()
AnsibleLambdaStack(app, "AnsibleLambdaStack")
app.synth()
```

In this example:

1. We create an IAM role for the Lambda function using `iam.Role` and grant necessary permissions using `add_managed_policy` (adjust the permissions based on your requirements).

2. We create a Lambda function using `lambda_.Function` and specify the code asset, handler, runtime, IAM role, and timeout.

3. To include the Ansible playbooks in the Lambda function deployment package, we use the `os` module to walk through the ansible/playbooks folder and its subdirectories.

4. For each YAML file (with .yml or .yaml extension) found in the ansible/playbooks folder, we add it to the asset hash of the Lambda function using `ansible_lambda.add_to_asset_hash(playbook_path)`. This ensures that the playbooks are included in the deployment package.

5. The Lambda function code and dependencies should be placed in a directory named lambda in the same directory as the CDK stack file.

When you run `cdk deploy`, the AWS CDK will package the Lambda function code, dependencies, and the Ansible playbooks into a deployment package and create the Lambda function with the specified configuration.

Inside your Lambda function code (lambda_function.py), you can reference the playbooks using their relative paths within the deployment package. For example:

```python
def lambda_handler(event, context):
    # ...
    playbook_path = 'playbook.yml'  # Relative path to the playbook within the deployment package
    # ...
```

Make sure to adjust the paths and names according to your specific folder structure and playbook file names.

By  the Ansible playbooks in the Lambda function deployment package using `add_to_asset_hash`, you ensure that the playbooks are available to the Lambda function at runtime, allowing you to execute them as needed.
