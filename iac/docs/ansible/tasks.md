

- Allocate an Elastic IP address for Amazon EC2 (same as this:)
- [Associate an Elastic IP address with an Amazon EC2 instance](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/python/example_code/ec2/elastic_ip.py)


- Create an Amazon EC2 security group
- [Create a security key pair for Amazon EC2](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/python/example_code/ec2/key_pair.py)

- [Create security group](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/python/example_code/ec2/security_group.py)
- Create and run an Amazon EC2 instance
- Set inbound rules for an Amazon EC2 security group
- Using the AWS docs for boto, add error handing and idemptotency to boto3 project

- [Complete Scenario](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/python/example_code/ec2/scenario_get_started_instances.py)

https://rick-hightower.blogspot.com/2017/03/setting-up-ansible-ssh-to-configure-aws.html

Look at Claude answers for boto questions

https://github.com/bparanj/learning-nuxt/blob/main/iac/docs/ansible/custom-ami.md
https://github.com/bparanj/learning-nuxt/blob/main/iac/docs/ansible/ec2.md
https://github.com/bparanj/learning-nuxt/blob/main/iac/docs/ansible/one-box.md


Packer Template to Boto3 Tasks

- Review docs/boto/customize-ami.md

- Run the master playbook:

```
playbook_file   = "../ansible/playbooks/master_playbook.yml"
```

- Copy and include all the playbooks in the playbooks directory.

- Establish SSH connection from Ansible control node to EC2 instance. [Done]

- Identify the AMI with unique name. Review ami-name.md
	
- Extract the latest Ubuntu 22.04 AMI name from the AWS EC2 AMI search using Ansible. [Done]

- Review docs/boto/public-ami.md

- Review docs/boto/tag-ami.md

- Review and extract action items from Boto3 equivalent of post-processor in Packer /docs/boto/post-processor.md

Note:

The playbooks:
	iac/prototype/experiments/ansible/experiments/ec2.yml
	iac/prototype/experiments/ansible/experiments/test.yml

have issues with SSH connection. See boto3 project for alternate way to accomplish the same task. These playbooks are no longer required.
