To upload a key pair from your local machine to your AWS account using Ansible, you can use the `amazon.aws.ec2_key` module. This playbook requires the path to your PEM file on your local machine and assumes you have the necessary permissions in AWS to import key pairs.

```yaml
---
- name: Upload a key pair to AWS
  hosts: localhost
  gather_facts: false
  vars:
    local_pem_path: "/path/to/your/local/key.pem" # Update this path
    key_name: "MyImportedKeyPair" # Name for the key pair in AWS

  tasks:
    - name: Read local key file
      ansible.builtin.slurp:
        src: "{{ local_pem_path }}"
      register: pem_file

    - name: Convert key to base64
      ansible.builtin.set_fact:
        key_content: "{{ pem_file['content'] | b64decode }}"

    - name: Upload key pair to AWS
      amazon.aws.ec2_key:
        name: "{{ key_name }}"
        key_material: "{{ key_content }}"
        state: present
```

### Key Points:

- **`local_pem_path`**: Update this variable with the full path to your PEM file on your local machine.
- **`key_name`**: This is the name you want to assign to your key pair in AWS. Ensure it's unique within your AWS region.
- **Tasks Explained**:
  - **Read local key file**: This task reads the content of your PEM file.
  - **Convert key to base64**: Since the PEM file is slurped as a base64-encoded string, it's decoded back to its original string format.
  - **Upload key pair to AWS**: The key material (content of your PEM file) is uploaded to AWS under the provided `key_name`.

Before running this playbook, ensure you have:
- The `amazon.aws` collection installed (`ansible-galaxy collection install amazon.aws`).
- Your AWS credentials configured properly for Ansible to use.

Replace `/path/to/your/local/key.pem` with the  path to your PEM file and `MyImportedKeyPair` with your desired key pair name in AWS. This playbook will import your PEM file into AWS, making it available for use when launching EC2 instances.

## Remove Key Pair from Instance

When creating a custom image (AMI) in AWS that will be shared with or sold to customers, ensuring it does not contain sensitive information, specific configuration files, or personal SSH keys is crucial. To remove a file from an instance before creating a common AMI, you can use a script or manual commands as part of your instance preparation process. Here's a general approach:

1. **Access the Instance**: SSH into the instance using its public IP address and your SSH key.

2. **Remove the File**: Use the `rm` command to delete the specific file. For example, to remove a file named `sensitive-info.txt` located in the home directory, you would run:
   ```bash
   rm ~/sensitive-info.txt
   ```

3. **Clean Up**: Ensure no remnants of the file remain,  backups or shell history. For shell history, you can clear it by running:
   ```bash
   history -c && history -w
   ```

4. **Zero Out Free Space**: To make sure deleted files can't be easily recovered, you can zero out the free space on your disk. This step is optional but recommended for sensitive data. For a Linux instance, you can use the `dd` command on each mounted drive. For example, to zero out the main partition, you might use:
   ```bash
   sudo dd if=/dev/zero of=/bigfile bs=1M; sudo rm -f /bigfile
   ```

5. **Create the AMI**: After ensuring the file is securely deleted and the instance is in the desired state, create an AMI from the EC2 console or using AWS CLI:
   ```bash
   aws ec2 create-image --instance-id i-1234567890abcdef0 --name "My Custom AMI" --description "An AMI without sensitive data."
   ```

6. **Test the AMI**: Launch a new instance from your custom AMI and verify that the file has been removed and the instance behaves as expected.

By following these steps, you can prepare a clean, customer-ready AMI without unnecessary or sensitive files.
