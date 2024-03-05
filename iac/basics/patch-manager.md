To use AWS Patch Manager with Ansible and Packer, you can follow these steps:

1. Set up AWS Systems Manager:
   - Ensure that your EC2 instances are managed by AWS Systems Manager.
   - Install the SSM Agent on your instances if it's not already installed.

2. Create an IAM role for Systems Manager:
   - Create an IAM role with the necessary permissions for Systems Manager.
   - Attach the `AmazonSSMManagedInstanceCore` managed policy to the role.

3. Configure Patch Manager:
   - In the AWS Systems Manager console, go to "Patch Manager".
   - Create a patch baseline that defines the patch policies and rules.
   - Specify the operating system, patch classifications, and approval rules.

4. Use Ansible to configure instances:
   - Create an Ansible playbook to configure your instances.
   - Install the necessary packages and dependencies.
   - Configure the SSM Agent to register the instances with Systems Manager.

5. Create a Packer template:
   - Define a Packer template to create an AMI with the desired configurations.
   - Use the Ansible provisioner in Packer to run your Ansible playbook.
   - Specify the IAM role with Systems Manager permissions in the Packer template.

6. Build the AMI with Packer:
   - Run the Packer build command to create the AMI.
   - Packer will launch an EC2 instance, run the Ansible playbook, and create an AMI from the configured instance.

7. Use the AMI to launch instances:
   - Launch EC2 instances using the AMI created by Packer.
   - The instances will have the necessary configurations and will be registered with Systems Manager.

8. Run patch scans and install patches:
   - Use AWS Systems Manager Run Command or Maintenance Windows to run patch scans on the instances.
   - The patch scans will identify missing or outdated patches based on the defined patch baseline.
   - Install the required patches using the appropriate patch installation commands.

Here's a simple example of an Ansible playbook that installs the SSM Agent:

```yaml
- name: Install SSM Agent
  hosts: all
  become: yes

  tasks:
    - name: Install SSM Agent
      yum:
        name: https://s3.amazonaws.com/ec2-downloads-windows/SSMAgent/latest/linux_amd64/amazon-ssm-agent.rpm
        state: present
```

And here's a basic Packer template that uses the Ansible provisioner:

```json
{
  "builders": [{
    "type": "amazon-ebs",
    "region": "us-west-2",
    "source_ami": "ami-0c55b159cbfafe1f0",
    "instance_type": "t2.micro",
    "ssh_username": "ec2-user",
    "iam_instance_profile": "SSMInstanceProfile",
    "ami_name": "packer-example-{{timestamp}}"
  }],

  "provisioners": [{
    "type": "ansible",
    "playbook_file": "playbook.yml"
  }]
}
```

Make sure to replace the `source_ami`, `iam_instance_profile`, and other relevant configurations with your own values.

By combining AWS Patch Manager, Ansible, and Packer, you can automate the process of creating pre-configured AMIs and managing patches on your EC2 instances.

No, if Patch Manager runs and applies patches to your server, it is not considered immutable infrastructure in the strict sense.

Immutable infrastructure is an approach where once an infrastructure component, such as a server, is deployed, it is never modified or updated in place. Instead, if changes or updates are required, a new version of the component is created and deployed to replace the existing one. The old component is then decommissioned or terminated.

The key principle of immutable infrastructure is that the components are treated as disposable and are not modified after they are deployed. This approach provides several benefits, such as:

1. Consistency: By deploying new versions of components instead of modifying existing ones, you ensure that all instances of the component are identical and have a consistent state.

2. Reproducibility: Immutable infrastructure allows for easy reproduction of the exact same environment since the components are defined and deployed using automated and version-controlled processes.

3. Simplified rollbacks: If issues arise with a new version of a component, you can quickly roll back to the previous version by deploying the older, known-good version.

4. Reduced configuration drift: Since components are not modified after deployment, there is less risk of configuration drift over time, where manual changes or ad-hoc modifications can lead to inconsistencies.

When Patch Manager runs and applies patches to your server, it modifies the existing server in place. This means that the server's state is changed after it was initially deployed, which goes against the principles of immutable infrastructure.

However, it's important to note that patching and updating servers is still a critical aspect of maintaining the security and stability of your infrastructure. In an immutable infrastructure setup, you would typically incorporate the patching process into your deployment pipeline. Instead of applying patches directly to running servers, you would create new server images or templates that include the latest patches and updates. These updated images would then be used to deploy new instances, replacing the old ones. IAC tool you use here is important. If it is image based like Packer then you would consider it immutable.

So, while running Patch Manager on your servers doesn't align with the strict definition of immutable infrastructure, it is still a necessary practice for maintaining a secure and up-to-date environment. You can adopt a hybrid approach where you apply patches to running servers periodically but also incorporate patching into your immutable infrastructure workflow by creating updated server images and deploying new instances based on those images.
