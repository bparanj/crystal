## Tools

- AWS CLI
- Python 3
- IDE
- Boto3
- Create IAM user and download the credentials as CSV file.


python3 --version
Python 3.12.1

$ pip --version
pip 24.0 from /opt/homebrew/lib/python3.11/site-packages/pip (python 3.11)
$ which python3
/usr/local/bin/python3
How to uninstall python 3.11 and install pip for python 3.12 which is installed in /usr/local/bin

 pip3.12 --version
pip 24.0 from /opt/homebrew/lib/python3.12/site-packages/pip (python 3.12)

$ aws --version
aws-cli/2.15.28 Python/3.11.8 Darwin/23.1.0 exe/x86_64 prompt/off

$ aws configure
AWS Access Key ID [****************NJU7]: AKIAsomething
AWS Secret Access Key [****************gdRJ]: sDWdsomething
Default region name [None]: us-east-1
Default output format [json]: 
$ cat ~/.aws/credentials 
[default]
aws_access_key_id = AKIAsomething
aws_secret_access_key = sDWdsomething
[cdk]
aws_access_key_id = AKIAsomething
aws_secret_access_key = 2ECsomething

Delete CDK, because it not being used anymore.

To ensure AWS CLI is properly configured with your credentials, run:

```sh
aws sts get-caller-identity
```

This command returns details about the credentials you're currently using,  the AWS account ID, user or role name, and user or role ID. If your credentials are not set correctly, this command will produce an error indicating that AWS was unable to authenticate the request.

$ pip3.12 install boto3
error: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try brew install
    xyz, where xyz is the package you are trying to
    install.
    
    If you wish to install a non-brew-packaged Python package,
    create a virtual environment using python3 -m venv path/to/venv.
    Then use path/to/venv/bin/python and path/to/venv/bin/pip.
    
    If you wish to install a non-brew packaged Python application,
    it may be easiest to use pipx install xyz, which will manage a
    virtual environment for you. Make sure you have pipx installed.

note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification

To install `boto3` without affecting the system-managed Python environment, use a virtual environment:

1. Create a virtual environment:
   ```sh
   python3.12 -m venv myenv
   ```
2. Activate the virtual environment:
   - On macOS/Linux:
     ```sh
     source myenv/bin/activate
     ```
   - On Windows (cmd.exe):
     ```cmd
     myenv\Scripts\activate.bat
     ```
3. Install `boto3` within the activated virtual environment:
   ```sh
   pip install boto3
   ```

(myenv) $ pip show boto3   
Name: boto3
Version: 1.34.68
Summary: The AWS SDK for Python
Home-page: https://github.com/boto/boto3
Author: Amazon Web Services
Author-email: 
License: Apache License 2.0
Location: /Users/bparanj/work/nuxt/myenv/lib/python3.12/site-packages
Requires: botocore, jmespath, s3transfer
Required-by: 


(myenv) $ cat ~/.aws/config
[default]
output = json
region = us-east-1
[profile cdk]
region = us-east-1
output = json

You can delete the cdk. It is not used anymore.

 cat ~/.aws/credentials 
[default]
aws_access_key_id = AKIAblahblahblah
aws_secret_access_key = sDWdblahblahblah


To manage different versions of Python and their associated packages, it's highly recommended to use a version management system like `pyenv`. This approach allows you to switch between Python versions without affecting the system-installed Python and manage your Python environments more cleanly. Here’s how you can uninstall Python 3.11, install Python 3.12, and ensure `pip` is associated with Python 3.12.

### Step 1: Uninstall Python 3.11

If you installed Python 3.11 manually and it's not being managed by a version manager like `pyenv`, you can uninstall it by removing its directory. However, if it was installed via a package manager (like `brew` on macOS), you should use the same package manager to uninstall it. Assuming you're on a macOS and used Homebrew:

```sh
brew uninstall python@3.11
```

### Step 2: Install `pyenv`

If you haven’t already installed `pyenv`, you can do so. It will help you manage different Python versions easily. On macOS, you can install it with Homebrew:

```sh
brew install pyenv
```

### Step 3: Install Python 3.12 Using `pyenv`

With `pyenv` installed, you can now install Python 3.12:

```sh
pyenv install 3.12.0
```

Make sure you’ve installed the exact version you need. You can use `pyenv install --list` to see all available versions.

### Step 4: Set Python 3.12 as Global Python Version

After installing Python 3.12, set it as the global version on your system:

```sh
pyenv global 3.12.0
```

### Step 5: Verify the Installation

Check that the correct version of Python is being used:

```sh
python --version
# Should output Python 3.12.0
```

### Step 6: Ensure `pip` is Associated with Python 3.12

When you install Python using `pyenv`, `pip` comes installed with it. Verify that `pip` is pointing to the correct Python version:

```sh
pip --version
# Ensure it shows Python 3.12 in the path
```

### Step 7: Fixing the PATH (If Necessary)

Ensure your shell's PATH variable is correctly configured to use the `pyenv` managed Python and pip versions. Add `pyenv` to your shell's configuration file (e.g., `.bashrc`, `.zshrc`):

```sh
echo 'eval "$(pyenv init --path)"' >> ~/.zshrc
```

Replace `.zshrc` with your shell’s configuration file, like `.bashrc` for Bash. Then, restart your terminal or source your configuration file:

```sh
source ~/.zshrc
```

### Note:

- The uninstallation steps may vary if Python was installed using a different method or if you are on a different operating system.
- Using `pyenv` is just a recommendation. If you prefer another version management system or approach, the key steps remain similar: uninstall the old version, install the new version, and ensure the environment is correctly set up.

This process should switch your active Python version to 3.12, along with the corresponding `pip` version.

$ brew uninstall python@3.11
Error: Refusing to uninstall /opt/homebrew/Cellar/python@3.11/3.11.8
because it is required by awscli, which is currently installed.
You can override this and force removal with:
  brew uninstall --ignore-dependencies python@3.11

