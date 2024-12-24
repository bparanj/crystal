## Service vs Process

Terms "service" and "process" are related. They refer to different concepts in the context of operating systems like Linux:

### **Process**
- **Definition**: A process is an instance of a running program. It includes the program code and its current activity.
- **Characteristics**: Processes have their own memory space and system resources. They can be in various states such as running, waiting, or terminated.
- **Examples**: When you open a text editor or a web browser, each instance is a separate process.

### **Service**
- **Definition**: A service is a type of process that runs in the background and performs specific functions, often without direct user interaction.
- **Characteristics**: Services are typically started at boot time and run continuously to provide system functionalities like networking, logging, or scheduling tasks.
- **Examples**: Common services include `sshd` (for SSH access), `httpd` (web server), and `cron` (task scheduler).

While all services are processes, not all processes are services. Services are specialized processes designed to run in the background and provide ongoing system functions.
