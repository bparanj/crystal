Here's an example of how to use the `amazon.aws.ec2_instance` module in Ansible to create an EC2 instance:

```yaml
---
- name: Create EC2 instance
  hosts: localhost
  gather_facts: false
  vars:
    aws_region: us-west-2
    instance_type: t2.micro
    ami_id: ami-0c55b159cbfafe1f0
    key_name: my-key-pair
    subnet_id: subnet-12345678
    security_group_id: sg-12345678
    instance_name: MyInstance

  tasks:
    - name: Launch EC2 instance
      amazon.aws.ec2_instance:
        name: "{{ instance_name }}"
        key_name: "{{ key_name }}"
        instance_type: "{{ instance_type }}"
        image_id: "{{ ami_id }}"
        wait: yes
        volumes:
          - device_name: /dev/sda1
            ebs:
              volume_size: 20
              delete_on_termination: true
        vpc_subnet_id: "{{ subnet_id }}"
        security_group: "{{ security_group_id }}"
        state: present
        region: "{{ aws_region }}"
        network:
          assign_public_ip: yes
        tags:
          Environment: Dev
          Application: MyApp
      register: ec2

    - name: Print EC2 instance details
      debug:
        var: ec2
```

This playbook does the following:

1. Defines variables for the AWS region, instance type, AMI ID, key pair name, subnet ID, security group ID, and instance name.

2. Uses the `amazon.aws.ec2_instance` module to launch an EC2 instance with the specified configuration.

3. Specifies the instance name, key pair, instance type, AMI ID, and other parameters.

4. Configures the root volume with a size of 20 GB and sets it to be deleted on instance termination.

5. Associates the instance with the specified subnet and security group.

6. Ensures the instance is in the "present" state and launches it in the specified AWS region.

7. Assigns a public IP to the instance.

8. Adds tags to the instance for environment and application.

9. Registers the output of the `ec2_instance` module in the `ec2` variable.

10. Prints the details of the created EC2 instance using the `debug` module.

To use this playbook:

1. Install the `amazon.aws` collection using `ansible-galaxy collection install amazon.aws`.

2. Replace the placeholder values (`aws_region`, `instance_type`, `ami_id`, `key_name`, `subnet_id`, `security_group_id`) with your specific AWS configuration.

3. Save the playbook with a `.yml` extension (e.g., `create_ec2_instance.yml`).

4. Run the playbook using the `ansible-playbook` command:

   ```
   ansible-playbook create_ec2_instance.yml
   ```

   Ansible will execute the playbook and create the EC2 instance with the specified configuration. The instance details will be printed in the output.

Make sure you have the necessary AWS credentials and permissions configured for Ansible to interact with your AWS account.
