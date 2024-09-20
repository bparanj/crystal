In Linux, a signal is a form of inter-process communication used to notify a process that a specific event has occurred. Signals can be sent by the operating system, hardware, or other processes to indicate various conditions or to control the behavior of processes.

- **Types of Signals**: There are standard signals (like `SIGINT`, `SIGTERM`, `SIGKILL`) and real-time signals. Standard signals are predefined and have specific meanings, while real-time signals are user-defined and can carry additional data¹².
- **Signal Handling**: Each signal has a default action, such as terminating the process, ignoring the signal, or stopping the process. Processes can change the default action by defining custom signal handlers.
- **Common Signals**:
  - `SIGINT` (Interrupt): Sent when the user types Ctrl+C. It usually terminates the process.
  - `SIGTERM` (Terminate): Requests a process to terminate gracefully.
  - `SIGKILL` (Kill): Forces a process to terminate immediately. This signal cannot be caught or ignored.
  - `SIGTRAP`: Used for debugging purposes, such as setting breakpoints³.

- **Sending Signals**: Signals can be sent using commands like `kill`, `pkill`, or `killall`, or programmatically using functions like `raise()` or `kill()`.
