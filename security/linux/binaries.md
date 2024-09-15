Binaries

In Linux, the term **binaries** refers to executable files that contain compiled code. These files are essential for running programs, scripts, and commands on the system. When you execute a command like `ls` to list directory contents or `cp` to copy files, you're ly running binaries that reside in directories such as `/bin`, `/usr/bin`, and `/sbin`¹².

Here's a quick breakdown:
- **/bin**: Contains essential command binaries needed for the system to function, like `ls`, `cp`, and `mv`.
- **/sbin**: Holds system binaries,  used by the root user for administrative tasks.
- **/usr/bin**: Stores user binaries, which are non-essential but  used commands and applications.
- **/usr/sbin**: Contains non-essential system binaries used by the root user.

Binaries allow the operating system to perform a wide range of tasks, from basic file manipulations to running complex applications¹³.

Programs are called "binaries" because they are compiled into binary code, which is the machine-readable format that computers understand. At the lowest level, computers operate using binary (base-2) number systems, which consist of only two digits: 0 and 1¹².

Here's a bit more detail:
- **Binary Code**: This is the fundamental language of computers, representing data and instructions using combinations of 0s and 1s. Each binary digit (bit) corresponds to an electrical state: on (1) or off (0)¹.
- **Compilation**: When source code (written in high-level programming languages like C or Python) is compiled, it is translated into binary code. This process converts human-readable instructions into a format that the computer's processor can execute directly².

So, the term "binaries" reflects the fact that these executable files are in a binary format, ready for the computer to run.

So the programs are already compiled and the executable program is in the binary format.

Yes. When a program is compiled, the source code (written in a high-level programming language) is translated into machine code, which is in binary format. This machine code is what the computer's processor can execute directly. The resulting file is called a binary or an executable.

For example, when you compile a C program using `gcc`, the output is a binary file that you can run on your system. Here's a simple illustration:

1. **Source Code**: Written in a high-level language (e.g., C).
   ```c
   #include <stdio.h>

   int main() {
       printf("Hello, World!\n");
       return 0;
   }
   ```

2. **Compilation**: Using a compiler like `gcc`.
   ```bash
   gcc -o hello hello.c
   ```

3. **Binary/Executable**: The output file (`hello`) is in binary format.
   ```bash
   ./hello
   ```

When you run `./hello`, the binary code is executed by the processor, and you see the output "Hello, World!" on your screen.

The binaries that are shipped with the any Linux distro distribution is already compiled in a format and stored in standard directories for the users to run them from command line.

Yes, that's correct! When you install a Linux distribution, it comes with a set of pre-compiled binaries that are ready to use. These binaries are stored in standard directories, making it easy for users to run them from the command line. Here are some of the common directories where these binaries are stored:

- **/bin**: Contains essential command binaries needed for the system to function, like `ls`, `cp`, and `mv`.
- **/sbin**: Holds system binaries,  used by the root user for administrative tasks.
- **/usr/bin**: Stores user binaries, which are non-essential but  used commands and applications.
- **/usr/sbin**: Contains non-essential system binaries used by the root user.
- **/usr/local/bin**: Used for binaries that are installed locally, often by the system administrator or user.

These directories are included in the system's PATH environment variable, so you can run the commands without needing to specify their full path.

Here's a table comparing and contrasting system binaries, user binaries, and other types of binaries found in a Linux distribution:

| **Type of Binary** | **Description** | **Location** | **Usage** | **Examples** |
|--------------------|-----------------|--------------|-----------|--------------|
| **System Binaries** | Essential binaries required for the system to function. Typically used for system-level tasks. | `/bin`, `/sbin` | Used by both the system and users for basic operations and administrative tasks. | `ls`, `cp`, `mv`, `init`, `shutdown` |
| **User Binaries** | Non-essential binaries used by users for various applications and commands. | `/usr/bin`, `/usr/sbin` | Used by users for everyday tasks and applications. | `firefox`, `gcc`, `nano`, `htop` |
| **Local Binaries** | Binaries installed locally, often by the system administrator or user. | `/usr/local/bin`, `/usr/local/sbin` | Used for custom or locally installed applications and scripts. | Custom scripts, locally compiled programs |
| **Temporary Binaries** | Binaries used temporarily, often during the boot process or for temporary tasks. | `/tmp`, `/var/tmp` | Used for temporary tasks and are usually cleaned up after use. | Temporary installation files, temporary scripts |
| **Library Binaries** | Shared libraries used by various programs to perform common tasks. | `/lib`, `/usr/lib`, `/lib64` | Used by programs to access shared functions and routines. | `libc.so`, `libm.so` |

This table highlights the different types of binaries, their locations, usage, and some examples. Each type of binary serves a specific purpose and is stored in standard directories to ensure the system operates smoothly.

Different kinds of binaries in Linux serve various purposes, ensuring the system operates efficiently, securely, and flexibly. Here's why having different types of binaries is important:

1. **Organization and Management**: Separating binaries into different categories helps keep the system organized. Essential system binaries are kept separate from user applications, making it easier to manage and maintain the system.

2. **Security**: By isolating system binaries from user binaries, you can apply different security policies and permissions. For example, system binaries in `/sbin` might require root access, while user binaries in `/usr/bin` can be executed by any user.

3. **Performance**: Different types of binaries can be optimized for their specific tasks. System binaries are often optimized for performance and stability, while user binaries might prioritize features and usability.

4. **Flexibility**: Having separate locations for different binaries allows for more flexible system configurations. For instance, you can easily add custom binaries to `/usr/local/bin` without interfering with the system's default binaries.

5. **Maintenance and Upgrades**: When binaries are categorized, it simplifies system maintenance and upgrades. You can update system binaries without affecting user applications, and vice versa.

6. **Compatibility**: Different binaries might be compiled for different architectures or purposes. Keeping them separate ensures that the right binaries are used for the right tasks, maintaining system compatibility.
