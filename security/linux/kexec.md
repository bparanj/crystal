kexec

**kexec** is a system call that allows you to load and boot into another kernel from the currently running kernel without going through the BIOS or firmware initialization. This can reduce the time required for a reboot.

1. **Loading the Kernel**: You load the new kernel into memory using the command:
   ```bash
   kexec -l /path/to/kernel --append="command-line-options" --initrd=/path/to/initrd
   ```
   This prepares the new kernel to be booted.

2. **Executing the Kernel**: Once the kernel is loaded, you can boot into it using:
   ```bash
   kexec -e
   ```
   This command will immediately switch to the new kernel.
