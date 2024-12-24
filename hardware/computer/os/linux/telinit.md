## telinit

The `telinit` command in Linux is used to change the system's runlevel, which is a state that defines what system services are operating. It is closely linked to the `init` command, which is the first process started by the kernel and is responsible for initializing the system.

### Key Points:

1. **Runlevels**: 
   - **Runlevel 0**: Halt the system.
   - **Runlevel 1**: Single-user mode (maintenance mode).
   - **Runlevel 3**: Multi-user mode without a graphical interface.
   - **Runlevel 5**: Multi-user mode with a graphical interface.
   - **Runlevel 6**: Reboot the system.

2. **Usage**: 
   - To change the runlevel, you can use `telinit` followed by the desired runlevel number. For example, `telinit 3` would switch the system to runlevel 3.
   - It sends signals to the `init` process to perform the necessary actions to change the runlevel.

3. **Systemd**: 
   - In modern Linux distributions that use `systemd` instead of the traditional SysV init system, runlevels are replaced by targets. For example, `runlevel 3` is equivalent to `multi-user.target` in `systemd`.
