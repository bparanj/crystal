## Goss Testing Basics

To create a Goss test file that verifies the installation of the specified packages, you can use the `package` test type in Goss. Here's an example `goss.yaml` file that checks if each package is installed:

```yaml
package:
  build-essential:
    installed: true
  curl:
    installed: true
  git:
    installed: true
  libdb-dev:
    installed: true
  libffi-dev:
    installed: true
  libgdbm-dev:
    installed: true
  libgdbm6:
    installed: true
  libgmp-dev:
    installed: true
  libncurses5-dev:
    installed: true
  libreadline-dev:
    installed: true
  libssl-dev:
    installed: true
  libyaml-dev:
    installed: true
  locales:
    installed: true
  patch:
    installed: true
  pkg-config:
    installed: true
  rustc:
    installed: true
  uuid-dev:
    installed: true
  zlib1g-dev:
    installed: true
  tzdata:
    installed: true
  openssl:
    installed: true
  python3:
    installed: true
  openssh-client:
    installed: true
```

This `goss.yaml` file in the tests directory specifies that each listed package should be installed on the system. When you run `goss validate`, Goss will check the system to ensure that each package is indeed installed, reporting any discrepancies.

### How to Use the Goss Test File

1. **Place the `goss.yaml` file on your system**: Copy this file to the target system where you want to validate the package installations. You can do this manually, or automate the process using tools like Ansible, Packer, or a CI/CD pipeline.

2. **Run Goss to validate the system**:
   - Install Goss on the target system if it's not already installed.
   - Navigate to the directory containing the `goss.yaml` file and run:
     ```bash
     goss validate
     ```
   - Goss will output the results of the tests, indicating whether each package is installed as expected.

This approach allows you to systematically verify the setup of your systems, ensuring that all necessary packages are installed according to your specifications.

The location of the `goss.yaml` file within your project directory should be structured based on how you organize your Packer and Ansible configurations, as well as how you plan to execute Goss tests. A common approach is to place test files, including `goss.yaml`, in a directory dedicated to testing or validation scripts. This helps maintain a clean project structure and simplifies the process of specifying the path to the `goss.yaml` file in your automation scripts.

Given a project with both Packer and Ansible, a suggested project structure might look like this:

```
project-directory/
├── packer/
│   ├── packer-template.pkr.hcl
│   └── ...
├── ansible/
│   ├── playbooks/
│   │   ├── setup-packages.yml
│   │   └── ...
│   └── roles/
│       └── ...
└── tests/
    ├── goss.yaml
    └── ...
```

In this structure:

- The `packer/` directory contains your Packer templates and related files.
- The `ansible/` directory holds Ansible playbooks and roles.
- The `tests/` directory is dedicated to testing scripts and files, including your `goss.yaml`.

This setup allows you to easily reference the `goss.yaml` file from your Packer or Ansible scripts, knowing it's located in the `tests/` directory relative to the root of your project.

When integrating Goss with Packer, you might have a provisioner step in your Packer template to copy the `goss.yaml` file onto the image being built and then run Goss tests. The path to `goss.yaml` would be something like `"${path.root}/tests/goss.yaml"`, assuming `path.root` points to the root of your project directory.

If you are using Ansible to trigger Goss tests on a provisioned instance, you could use an Ansible task to copy `goss.yaml` from your local project's `tests/` directory to the target machine before running the Goss validation.

This structure is just a recommendation, and you should adjust it based on your project's specific needs and workflows.

## Create the Goss Playbook

In the playbooks folder, create goss.yaml:

```yml
---
- name: Install and Verify with Goss
  hosts: all
  become: true

  vars:
    goss_version: "v0.4.4"
    goss_install_path: "/usr/local/bin/goss"
    goss_test_directory: "/etc/goss"
    goss_file: "goss.yaml"

  tasks:
    - name: Install Goss
      get_url:
        url: "https://github.com/aelsabbahy/goss/releases/download/{{ goss_version }}/goss-linux-amd64"
        dest: "{{ goss_install_path }}"
        mode: "0755"

    - name: Ensure Goss test directory exists
      ansible.builtin.file:
        path: "{{ goss_test_directory }}"
        state: directory

    - name: Copy Goss test file to target
      ansible.builtin.copy:
        src: "../tests/{{ goss_file }}"
        dest: "{{ goss_test_directory }}/{{ goss_file }}"

    - name: Run Goss validation
      command: "{{ goss_install_path }} validate --format documentation {{ goss_file }}"
      args:
        chdir: "{{ goss_test_directory }}"
      register: test_result

    - name: List contents of Goss test directory
      command: ls -lah "{{ goss_test_directory }}"
      register: ls_output

    - name: Show contents of Goss test directory
      ansible.builtin.debug:
        var: ls_output.stdout_lines

    - name: Show Goss validation results
      ansible.builtin.debug:
        var: test_result.stdout_lines

    - name: Show Goss validation errors
      ansible.builtin.debug:
        var: test_result.stderr_lines
      when: test_result.rc != 0
```

VS Code error:

Incorrect type. Expected "Goss-file-schema".yaml-schema: Goss-file-schema

Fix:

Install Ansible VS code extension.

Yes, the revised Ansible playbook you've shared looks correct for the purpose of installing Goss, copying a Goss test file (`goss.yaml`) to a specific directory on the target system (`/etc/goss`), and then running Goss validation in that directory. The changes you've made, particularly using the `chdir` argument to change the working directory before running the Goss validation command, address the issue of Goss not finding the `goss.yaml` file due to incorrect working directory context.

Here's a summary of the key parts and their correctness:

- **Install Goss**: Downloads the Goss binary to the specified path and sets the executable permissions correctly.
- **Ensure Goss Test Directory Exists**: Creates the directory where the Goss tests will be stored, if it doesn't already exist.
- **Copy Goss Test File to Target**: Correctly copies the `goss.yaml` file from your project directory into the target directory on the remote system. Make sure the relative path `../tests/{{ goss_file }}` accurately reflects the location of `goss.yaml` relative to where the playbook is run.
- **Run Goss Validation**: Uses the `chdir` argument to switch to the directory containing `goss.yaml` before running the validation, ensuring Goss can find the test file. This is the correct approach to resolving the earlier issue.
- **List Contents of Goss Test Directory**: This debugging task will list the contents of the Goss test directory, helping verify that the `goss.yaml` file is in the expected location before validation.
- **Show Contents of Goss Test Directory**: Displays the output from listing the directory contents, which is useful for debugging.
- **Show Goss Validation Results and Errors**: These tasks will output the results of the Goss validation, including any errors if the validation fails (`when: test_result.rc != 0`), which is essential for troubleshooting failed validations.

Overall, your playbook is well-structured for the task of deploying Goss to a remote system, running validations, and providing useful debug information in case of issues. Ensure the paths used in the playbook accurately reflect your project's directory structure, and adjust as necessary based on where the playbook is executed from within your project.

## Modify Packer Template

Add this section:

```hcl
  provisioner "ansible" {
    playbook_file = "${path.root}/playbooks/goss.yml"
    user          = "ubuntu"
    // Ensure Ansible can use the dynamic SSH settings provided by Packer
    use_proxy = false
    ansible_env_vars = [
      "ANSIBLE_HOST_KEY_CHECKING=False"
    ]
  }
```

The entire Goss playbook will be:

```yml
packer {
required_plugins {
amazon = {
source  = "github.com/hashicorp/amazon"
version = "~> 1"
}
ansible = {
version = "~> 1"
source  = "github.com/hashicorp/ansible"
}
}
}

source "amazon-ebs" "ubuntu" {
communicator  = "ssh"
ami_name      = "packer-ubuntu-aws-{{timestamp}}"
instance_type = "t2.micro"
region        = "us-west-2"
source_ami_filter {
filters = {
name                = "ubuntu/images/*ubuntu-jammy-22.04-amd64-server-*"
root-device-type    = "ebs"
virtualization-type = "hvm"
}
most_recent = true
owners      = ["099720109477"]
}
ssh_username = "ubuntu"
tags = {
"Name"        = "UbuntuImage"
"Environment" = "Testing"
"OS_Version"  = "Ubuntu 22.04"
"Release"     = "Latest"
"Created-by"  = "Packer"
}
}

build {
sources = [
"source.amazon-ebs.ubuntu"
]

provisioner "ansible" {
playbook_file = "${path.root}/playbooks/packages.yml"
user          = "ubuntu"
use_proxy     = false
ansible_env_vars = [
"ANSIBLE_HOST_KEY_CHECKING=False"
]
}

provisioner "ansible" {
playbook_file = "${path.root}/playbooks/webserver.yml"
user          = "ubuntu"
// Ensure Ansible can use the dynamic SSH settings provided by Packer
use_proxy = false
ansible_env_vars = [
"ANSIBLE_HOST_KEY_CHECKING=False"
]
}

provisioner "ansible" {
playbook_file = "${path.root}/playbooks/goss.yml"
user          = "ubuntu"
// Ensure Ansible can use the dynamic SSH settings provided by Packer
use_proxy = false
ansible_env_vars = [
"ANSIBLE_HOST_KEY_CHECKING=False"
]
}

post-processor "manifest" {}

}
```
