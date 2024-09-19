### What is an Environment Variable in Linux?

An environment variable in Linux is a dynamic value that can affect the way running processes will behave on a computer. These variables are used by the operating system and applications to store configuration settings and other information necessary for the system's operation.

### Characteristics of Environment Variables:

1. **Dynamic Values**:
   - Environment variables can change, and their values can be different for different processes and users.

2. **System and User Scope**:
   - Some environment variables are system-wide (set for all users), while others are specific to a particular user session.

3. **Inheritance**:
   - Environment variables are inherited by child processes. When a process is started, it inherits a copy of its parent process’s environment.

### Common Environment Variables:

- **`PATH`**: Specifies the directories in which the shell looks for executable files.
- **`HOME`**: Indicates the home directory of the current user.
- **`USER`**: Contains the name of the current user.
- **`SHELL`**: Specifies the path of the current user’s shell.
- **`LANG`**: Defines the language, encoding, and locale settings.
- **`PWD`**: Represents the current working directory.

### Why is it Named Environment Variable?

The term "environment variable" is used because these variables define the environment in which a process runs. They set the context or environment for the software and scripts executed within the system, influencing how they behave and interact with the system and user.

### Usage of Environment Variables:

1. **Setting Environment Variables**:
   - You can set an environment variable in a shell session using the `export` command:
     ```bash
     export VARIABLE_NAME=value
     ```

2. **Accessing Environment Variables**:
   - Accessing the value of an environment variable can be done using the `$` symbol:
     ```bash
     echo $VARIABLE_NAME
     ```

3. **Listing Environment Variables**:
   - To list all environment variables, you can use the `printenv` or `env` command:
     ```bash
     printenv
     env
     ```

4. **Persistent Environment Variables**:
   - To make an environment variable persistent across sessions, you can add it to the shell’s configuration file, such as `~/.bashrc`, `~/.bash_profile`, or `/etc/environment`.

### Practical Example:

- Setting a custom `PATH` environment variable:
  ```bash
  export PATH=$PATH:/usr/local/myapp/bin
  ```
  This command appends `/usr/local/myapp/bin` to the existing `PATH` variable, allowing executables in that directory to be found by the shell.

Environment variables are a fundamental aspect of configuring and managing the Linux operating environment, enabling both system-wide and user-specific settings that shape the behavior of processes and applications.
