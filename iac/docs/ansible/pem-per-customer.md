This playbook creates a common base AMI for all customers without any PEM file associated with it. It starts with a base Ubuntu AMI, customizes it to fit your specific requirements, and creates a new AMI without associating any PEM file.

Here's what the playbook does:

1. Defines variables for the AWS region, EC2 instance details, and AMI creation.

2. Launches an EC2 instance using the specified base AMI ID, instance type, key name, subnet ID, security group, and other parameters.

3. Waits for the EC2 instance to be in the running state.

4. Customizes the EC2 instance by executing shell commands or Ansible tasks as needed. This step may include installing packages, configuring settings, or deploying applications.

5. Stops the EC2 instance and waits for it to be in the stopped state.

6. Creates a new AMI from the stopped EC2 instance using the `amazon.aws.ec2_ami` module. The AMI is tagged with a name and description indicating that it is a custom base AMI without any PEM file association.

7. Terminates the EC2 instance used for creating the AMI.

8. Registers the details of the created AMI in the `ami_info` variable.

9. Prints the ID of the created AMI using the `debug` module.

For each customer, you can create a separate playbook that starts with the common base AMI created by this playbook. The customer-specific playbook can then associate a unique PEM file and perform further customization specific to that customer.

Here's an example of a customer-specific playbook:

```yaml
---
- name: Create customer-specific AMI
  hosts: localhost
  gather_facts: false
  vars:
    aws_region: us-west-2
    base_ami_id: "{{ ami_info.image_id }}"  # Use the base AMI ID created in the previous playbook
    instance_type: t2.micro
    key_name: customer-key
    subnet_id: subnet-12345678
    security_group_id: sg-12345678
    customer_name: Customer1
    pem_file_path: /path/to/customer/pem/file.pem

  tasks:
    - name: Launch EC2 instance from base AMI
      amazon.aws.ec2_instance:
        image_id: "{{ base_ami_id }}"
        instance_type: "{{ instance_type }}"
        key_name: "{{ key_name }}"
        vpc_subnet_id: "{{ subnet_id }}"
        security_group: "{{ security_group_id }}"
        wait: yes
        region: "{{ aws_region }}"
      register: ec2_instance

    - name: Customize EC2 instance for the customer
      # Add customer-specific customization tasks here

    - name: Create AMI for the customer
      amazon.aws.ec2_ami:
        instance_id: "{{ ec2_instance.instance_id }}"
        name: "{{ customer_name }}-AMI-{{ timestamp }}"
        wait: yes
        region: "{{ aws_region }}"
      register: customer_ami_info

    - name: Terminate EC2 instance
      amazon.aws.ec2_instance:
        instance_ids: "{{ ec2_instance.instance_id }}"
        state: absent
        region: "{{ aws_region }}"

    - name: Print customer AMI ID
      debug:
        var: customer_ami_info.image_id
```

This customer-specific playbook does the following:

1. Uses the base AMI ID created in the previous playbook as the starting point.

2. Launches an EC2 instance from the base AMI with the customer-specific key pair and other parameters.

3. Performs customer-specific customization tasks on the EC2 instance.

4. Creates a new AMI from the customized EC2 instance, tagging it with the customer name.

5. Terminates the EC2 instance used for creating the customer-specific AMI.

6. Prints the ID of the customer-specific AMI.

By separating the common base AMI creation and customer-specific AMI creation into separate playbooks, you can maintain a consistent base image while allowing for customization and unique PEM file associations for each customer.

Replace the placeholder values (`{{ ami_info.image_id }}`, `{{ timestamp }}`, `/path/to/customer/pem/file.pem`) with the appropriate values in the customer-specific playbook.
