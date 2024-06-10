## PEM File Experiment

Create a new folder for the experiment:

```
mkdir pemf
cd pemf
```

Create hosts file:

```
[local]
localhost
```

Create create_key_pair.yml:

```yaml
---
- hosts: local
  connection: local
  gather_facts: no
  tasks:
    - name: Create a new EC2 key
      ec2_key:
        name: ansible-ec2-key
        region: us-east-1
      register: ec2_key_result

    - name: Save private key
      copy:
        content: "{{ ec2_key_result.key.private_key }}"
        dest: "./rails-server.pem"
        mode: 0600
      when: ec2_key_result.changed
```

Run the playbook:

```bash
ansible-playbook -i hosts create_key_pair.yml
```

Verify the file:

```bash
head -n 5 rails-server.pem
```

Verify this key is in the AWS console.

Status: PUblished