

- Associate an Elastic IP address with an Amazon EC2 instance
- Allocate an Elastic IP address for Amazon EC2
- Create an Amazon EC2 security group
- Create a security key pair for Amazon EC2
- Create and run an Amazon EC2 instance
- Set inbound rules for an Amazon EC2 security group

https://rick-hightower.blogspot.com/2017/03/setting-up-ansible-ssh-to-configure-aws.html

Look at Claude answers for boto questions
Using the AWS docs for boto, add error handing and idemptotency to boto3 project

https://github.com/bparanj/learning-nuxt/blob/main/iac/docs/ansible/custom-ami.md
https://github.com/bparanj/learning-nuxt/blob/main/iac/docs/ansible/ec2.md
https://github.com/bparanj/learning-nuxt/blob/main/iac/docs/ansible/one-box.md

The playbooks:
	iac/prototype/experiments/ansible/experiments/ec2.yml
	iac/prototype/experiments/ansible/experiments/test.yml

have issues with SSH connection. See boto3 project for alternate way to accomplish the same task.