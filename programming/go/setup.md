Install the Go from its website.

To define the `GOPATH` on a Mac, follow these steps:

### 1. **Determine Where to Set `GOPATH`**
   - Usually, environment variables like `GOPATH` are set in a shell configuration file, such as `.bash_profile`, `.bashrc`, or `.zshrc`, depending on which shell you're using.

   To determine your current shell, run:
   ```bash
   echo $SHELL
   ```
   If you see `/bin/bash`, you're using Bash. If you see `/bin/zsh`, you're using Zsh (the default shell in macOS Catalina and later).

### 2. **Set `GOPATH` in the Correct File**

#### For Zsh (default shell in macOS Catalina and later):
1. Open the `.zshrc` file in a text editor:
   ```bash
   nano ~/.zshrc
   ```

2. Add the following lines to set `GOPATH`:
   ```bash
   export GOPATH=$HOME/go
   export PATH=$PATH:$GOPATH/bin
   ```

3. Save the file (in Nano, press `CTRL + O`, then `ENTER`, and then `CTRL + X` to exit).

4. Apply the changes by running:
   ```bash
   source ~/.zshrc
   ```

#### For Bash (default shell in older macOS versions):
1. Open the `.bash_profile` (or `.bashrc`):
   ```bash
   nano ~/.bash_profile
   ```

2. Add the following lines to set `GOPATH`:
   ```bash
   export GOPATH=$HOME/go
   export PATH=$PATH:$GOPATH/bin
   ```

3. Save the file (`CTRL + O`, then `ENTER`, `CTRL + X` to exit).

4. Apply the changes:
   ```bash
   source ~/.bash_profile
   ```

### 3. **Verify the `GOPATH`**

After setting `GOPATH`, verify that it's correctly set by running:
```bash
echo $GOPATH
```

This should output the directory you set, typically `$HOME/go`. The `GOPATH` is now defined, and Go will look for projects and packages in that directory.

Since you're using the `.bashrc` file and encountering the "command not found" error for `go`, it suggests that Go is either not installed correctly or its installation path is not included in your `PATH`. Here's how to resolve this:

### 1. **Install Go (if not installed)**
   - If Go is not yet installed, download and install it from the official Go website:
     - [Go Downloads](https://golang.org/dl/)
   - After installation, Go binaries should be placed in `/usr/local/go/bin` by default.

### 2. **Add Go to Your `PATH`**
   
   If Go is installed but not recognized, you need to add its installation path to your `PATH` environment variable in the `.bashrc` file.

1. Open the `.bashrc` file in a text editor:
   ```bash
   nano ~/.bashrc
   ```

2. Add the following lines to export the Go installation path and set the `GOPATH`:
   ```bash
   export PATH=$PATH:/usr/local/go/bin
   export GOPATH=$HOME/go
   export PATH=$PATH:$GOPATH/bin
   ```

3. Save the file by pressing `CTRL + O`, then `ENTER`, and `CTRL + X` to exit.

4. Apply the changes by running:
   ```bash
   source ~/.bashrc
   ```

### 3. **Verify Installation**
   After updating your `.bashrc`, verify that Go is properly installed by checking the Go version:
   ```bash
   go version
   ```

If Go is correctly installed and the `PATH` is updated, you should no longer see the "command not found" error.
