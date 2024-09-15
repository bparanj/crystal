## Verifying Package Installation with Ansible

Run the shell script to verify the installation manually. This is for troubleshooting purposes and is a fallback mechanism.

Below is an Ansible playbook that installs the specified packages on Ubuntu 22.04. This playbook updates the package lists for the Ubuntu package manager, installs the required packages, and generates the locale `en_US.UTF-8`.

```yaml
---
- name: Install development tools and libraries on Ubuntu 22.04
  hosts: all
  become: yes
  tasks:
    - name: Update APT package manager
      ansible.builtin.apt:
        update_cache: yes

    - name: Install development packages
      ansible.builtin.apt:
        name:
          - autoconf
          - bison
          - build-essential
          - curl
          - git-core
          - libdb-dev
          - libffi-dev
          - libgdbm-dev
          - libgdbm6
          - libgmp-dev
          - libncurses5-dev
          - libreadline6-dev
          - libsqlite3-dev
          - libssl-dev
          - libyaml-dev
          - locales
          - patch
          - pkg-config
          - rustc
          - uuid-dev
          - zlib1g-dev
          - tzdata
        state: present

    - name: Generate locale en_US.UTF-8
      ansible.builtin.locale_gen:
        name: en_US.UTF-8
        state: present
```

### How to Use This Playbook:

1. **Save the Playbook**: Copy the above playbook into a file, for example, `setup_dev_env.yml`.

2. **Create an Inventory File**: If you haven't already, create an inventory file (e.g., `hosts.ini`) that lists the Ubuntu 22.04 servers where you want to install these packages. Here's an example of what the inventory file might look like:

   ```
   [ubuntu_servers]
   192.168.1.10 ansible_user=ubuntu ansible_ssh_private_key_file=/path/to/your/private/key
   192.168.1.11 ansible_user=ubuntu ansible_ssh_private_key_file=/path/to/your/private/key
   ```

   Replace the IP addresses with those of your servers, and adjust the `ansible_user` and `ansible_ssh_private_key_file` as necessary.

3. **Run the Playbook**: Use the following command to run the playbook:

   ```bash
   ansible-playbook -i hosts.ini setup_dev_env.yml
   ```

This command will execute the playbook, updating the package list, installing the required packages, and generating the locale on all the servers listed in your inventory file under `[ubuntu_servers]`. Ensure you have Ansible installed on your local machine and that you can access the target servers over SSH.

To create an Ansible playbook that installs the specified packages on Ubuntu 22.04 and is intended to be run by Packer, you can follow the structure below. This playbook includes tasks for updating the package list, installing the necessary packages, and generating the locale as specified:

```yaml
---
- name: Install required packages on Ubuntu 22.04
  hosts: all
  become: true
  tasks:
    - name: Update apt repository and system packages
      ansible.builtin.apt:
        update_cache: yes
        cache_valid_time: 3600 # Cache valid for 1 hour to avoid unnecessary updates

    - name: Install development tools and libraries
      ansible.builtin.apt:
        name:
          - autoconf
          - bison
          - build-essential
          - curl
          - git-core
          - libdb-dev
          - libffi-dev
          - libgdbm-dev
          - libgdbm6
          - libgmp-dev
          - libncurses5-dev
          - libreadline6-dev
          - libsqlite3-dev
          - libssl-dev
          - libyaml-dev
          - locales
          - patch
          - pkg-config
          - rustc
          - uuid-dev
          - zlib1g-dev
          - tzdata
        state: present

    - name: Ensure locale is generated
      ansible.builtin.locale_gen:
        name: en_US.UTF-8
        state: present

    - name: Update locale
      ansible.builtin.command: update-locale LANG=en_US.UTF-8
      when: ansible_facts['env']['LANG'] is not defined or ansible_facts['env']['LANG'] != 'en_US.UTF-8'
```

To integrate this playbook with Packer, ensure you have the Ansible provisioner configured in your Packer template. Here's an example snippet on how to include the Ansible provisioner in your Packer HCL configuration:

```hcl
provisioner "ansible" {
  playbook_file = "path/to/your_playbook.yml"
}
```

Replace `path/to/your_playbook.yml` with the  path to the Ansible playbook you've created. This setup assumes Packer and Ansible are correctly installed and configured to work together, and that you have SSH access configured for the target Ubuntu 22.04 instance that Packer creates.

Running this setup will execute the Ansible playbook as part of the Packer build process, installing the required packages and configuring the locale on your Ubuntu 22.04 image.

## Gemini

Here's the Ansible playbook to install the listed packages on Ubuntu 22.04 along with an explanation:

```yaml
---
- name: Install packages on Ubuntu 22.04
  hosts: all  # Replace 'all' with your target host group if needed
  become: true  # Required for package management

  tasks:
    - name: Update apt cache
      apt:
         update_cache: yes

    - name: Install required packages
      apt:
        name: "{{ packages }}"
        state: present

  vars:
    packages:
      - autoconf
      - bison
      - build-essential
      - curl
      - git-core
      - libdb-dev
      - libffi-dev
      - libgdbm-dev
      - libgdbm6
      - libgmp-dev
      - libncurses5-dev
      - libreadline6-dev
      - libsqlite3-dev
      - libssl-dev
      - libyaml-dev
      - locales
      - patch
      - pkg-config
      - rustc
      - uuid-dev
      - zlib1g-dev
      - tzdata

    - name: Generate en_US.UTF-8 locale
      locale_gen:
        name: en_US.UTF-8
        state: present

```

**Explanation:**

- **hosts:** If you want to target a specific group of servers, replace the 'all' with your host group definition from your Ansible inventory.
- **become: true:** Since package management tasks require root privileges, we use `become` to execute them with elevated rights.
- **Tasks:**
  - **Update apt cache:** Ensures the package manager has the latest package lists before proceeding.
  - **Install required packages:** Uses the `apt` module, providing a list of packages. The `state: present` guarantees they are installed.
  - **Generate en_US.UTF-8 locale:** Handles locale generation for proper language support.
- **vars:** Defines the `packages` list in a convenient block to improve playbook readability.

**How to Use:**

1. **Save as YAML:** Save this code as a playbook file, for example, `install_packages.yml`.
2. **Ansible Inventory:** Ensure your Ansible inventory has the correct target hosts defined.
3. **Run the Playbook:** Execute using `ansible-playbook install_packages.yml`

**Feel free to modify the `hosts` section if you have a specific setup in mind. Let me know if you'd like help customizing this playbook for different scenarios or adding error handling!**

## Manual Verification

```
git --version
dpkg -l | grep curl
dpkg -l | grep autoconf
dpkg -l | grep build-essential
```

Here are a few common and effective methods to verify if a package is installed on your Ubuntu system from the terminal:

**1. Using `dpkg` (Direct Package Management)**

- **Command:** `dpkg -l | grep <package_name>`
- **Example:** `dpkg -l | grep curl`
- **Output:**
  - If installed, you'll see detailed package information.
  - If not installed, no output is returned.

**2. Using `apt-cache` (Package Cache Query)**

- **Command:** `apt-cache policy <package_name>`
- **Example:** `apt-cache policy git-core`
- **Output:**
  - If installed, shows version, repository, etc.
  - If not, it states that the package cannot be found.

**3. Using `apt list` (List All Packages)**:

- **Command:** `apt list --installed | grep <package_name>`
- **Example:** `apt list --installed | grep build-essential`
- **Output**: A single line listing the package if found.

**4. Checking for the Executable:**

- **Command:** `which <package_executable>`
  (replace `<package_executable>` with the main command provided by the package
  e.g., `which git`)
- **Output:**
  - If installed, this shows the path to the executable.
  - If not installed, there's no output

**Choosing the Right Method**

- **Quick Check:** `dpkg -l` or `apt-cache policy` are fastest for "is it there or not?"
- **Version Info:** `apt-cache policy` provides detailed version and installation source information.
- **Thorough Search:** `apt list --installed` lists everything and is good if you're unsure of the exact package name.
- **Beyond Packages:** `which` is helpful if you know the primary command a package provides.

**Let me know if you want to dive deeper into any of these methods or have specific scenarios for package verification you'd like to discuss!**

### Script

Here's a shell script that checks the installation of a list of packages, along with explanations:

```bash
#!/bin/bash

# Check if a list of packages is provided
if [[ $# -eq 0 ]]; then
    echo "Error: Please provide a list of packages to check."
    exit 1
fi

# Store the list of packages to check
packages_to_check=("$@")

# Iterate over the packages and check if they are installed
for package in "${packages_to_check[@]}"; do
    if dpkg-query -W -f='${Status}' "$package" 2>/dev/null | grep -q "ok installed"; then
        echo "$package is installed"
    else
        echo "$package is not installed"
    fi
done
```

**How to Use**

1. **Save as a script:** Save the code as `check_packages.sh`.
2. **Make executable:** `chmod +x check_packages.sh`
3. **Run the script:**
   ```bash
   ./check_packages.sh curl git-core build-essential
   ```

**Explanation**

- **Argument Check:** Ensures the user has provided at least one package name as input.
- **Packages Array:** Stores the provided package names from the command-line arguments.
- **`dpkg-query`:** Queries the package management system reliably.
  - `-W` shows information about a specific package
  - `-f='${Status}'` outputs only the installation status
  - `2>/dev/null` redirects errors to avoid false negatives
  - `grep -q "ok installed"` checks for the 'installed' status.
- **Success/Failure Output:** Provides clear messages about each package's state.

**Improvements**

- **Error Handling:** Return a non-zero exit code if any package check fails, aiding in scripting for automation tasks.
- **Customization:** Accept a filename containing the package list instead of only using command-line arguments.

**Let's Enhance It**

Would you like me to demonstrate how to:

- Include robust error handling for automation?
- Modify the script to read the package list from a file?
- Adapt it for other package managers (e.g., `yum` on RPM-based distros)?

Just ask!

```
$ chmod 744 ./check.sh
$ ./check.sh curl git-core build-essential
curl is installed
git-core is not installed
build-essential is installed
```

```
$ ./check.sh curl git build-essential libdb-dev rustc tzdata
curl is installed
git is installed
build-essential is installed
libdb-dev is installed
rustc is installed
tzdata is installed
```

## Read from File and Verify Installation

```bash
#!/bin/bash

# Color codes
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # Reset to normal

# Check if a filename is provided
if [[ $# -eq 0 ]]; then
    echo "Error: Please provide the filename containing the package list."
    exit 1
fi

# Read the package list file
package_file="$1"

# Ensure the file exists and is readable
if [[ ! -r "$package_file" ]]; then
    echo "Error: Cannot read package list file: $package_file"
    exit 1
fi

# Iterate over packages in the file
while read -r package; do
  if dpkg-query -W -f='${Status}' "$package" 2>/dev/null | grep -q "ok installed"; then
    echo -e "${GREEN}$package is installed${NC}"
  else
    echo -e "${RED}$package is not installed${NC}"
  fi
done < "$package_file"
```

**Changes Made**

1. **Input Argument:** The script now expects a filename as the first argument.
2. **File Readability Check:** Added a check to ensure the provided file exists and is readable by the user running the script.
3. **`while read` Loop:** A `while` loop processes the file line by line. The `< "$package_file"` part redirects the file content as input to the loop.

**How to Use**

1. **Package List File (`packages.txt`)**

   ```
   curl
   git-core
   build-essential
   ```

2. **Run Script**
   ```bash
   ./check_packages.sh packages.txt
   ```

**Improvements**

- **Error Handling:** Consider what the script should do if a single package within the file fails the check. Should it continue, or stop with an overall error code?

**Flexibility**

- **Filename Customization:** You could easily make the filename a second command-line argument if you don't want to hardcode it within the script.

Here's how to create a `packages.txt` file suitable for the script we developed earlier, given your input YAML structure:

**Simply Extract Package Names**

Since your YAML only indicates that the packages should be present, the `packages.txt` file can be a simple list of the package names. Here's the process:

1. **Copy and Paste:** Copy the YAML content you provided.
2. **Cleanup (Manually, or with a Tool):**
   - **Manual:** Remove all lines except those that start with a package name followed by a colon (`:`). Delete the `installed: true` parts.
   - **Tools:** You could use text editors with regular expressions or command-line tools like `awk` or `sed` to automate this removal.

**Resulting `packages.txt`**

```
build-essential
curl
git
libdb-dev
libffi-dev
libgdbm-dev
libgdbm6
libgmp-dev
libncurses5-dev
libreadline-dev
libssl-dev
libyaml-dev
locales
patch
pkg-config
rustc
uuid-dev
zlib1g-dev
tzdata
openssl
python3
openssh-client
```

**Let's Automate It!**

If you often have to transform YAML data like this, here's a quick Python snippet (assuming your YAML is in 'input.yaml'):

```python
import yaml

with open('input.yaml', 'r') as f:
    data = yaml.safe_load(f)

packages = data['package'].keys()

with open('packages.txt', 'w') as f:
    for pkg in packages:
        f.write(pkg + '\n')
```

**Important Note:** If your original YAML sometimes needs to express more than just package presence (e.g., versions), then the `packages.txt` generation would need additional logic.

Let me know if you'd like to explore more sophisticated transformations of the input data!
