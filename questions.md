What language is pwd, ls, cat and other commands in Linux implemented?
What are utilities in Linux?
What are builtin commands in Linux?
What is POSIX? What problem does it address?
What is tty in Linux?
What does a teletype look like?
What is a low-level service from the kernel? Why is it called low level?

grep "Search Term" articles/*

Keyboard is the standard input.
Terminal screen is the standard output.

Filter

Output of a program is used as the input to another program
All the data is passed as the data stream or as arguments in the command line.
Without any arguments, a program reads from the standard input and writes to the standard output.

Programs can be combined by using pipes. It can take output of the program on the left and feed it as input to the program on the right. Diagram.

What is job control in Linux?
What is command line editing in Linux?

grep loginname /etc/passwd

ypmatch loginname /etc/passwd

The last field shows the default shell.

tr command

tr '\015' < file.mac > file.unix

tr '\015' '\012'

chmod +x mac2unix

mac2unix < file.mac > file.unix

for x
do
  echo "Converting $x"
  tr \0105' '\012' < "$x" > "tmp.$x"
  mv "tmp.$x" "$x"
done

mac2unix file2 file2 file3 ...

- Loop
- Variable substitution

Internel commands are built into the shell. Ex: cd
External commands are programs stored in the file /bin. Ex: ls command is in /bin/ls

Internal commands are run in the same process as the shell.
External commands are run on a new subprocess that is created by shell using fork and exec.

For external commands:

- If the command has absolute pathname, execute it. Ex: /bin/ls
- Aliases or shell functions
- Look in the search path for an executable program with the given name

Search path is a list of directories that the shell should look through for a command that matches the typed command.
The search path is specified in shell setup file.

/opt
/usr/local/bin
/bin
/usr/bin
/etc
/usr/etc
/sbin
/usr/sbin

The search path is stored in an environment variable called PATH
The path is searched from left to right. Two commands with the same name -> First command will be executed.

Kernel

The kernel assigns memory to the running programs. Allocates time to the programs for the job to be done. It handles input/output operations.

Daemons

They perform tasks like handling email, network communictaions, sending data to a printer, keeping track of time, etc.

ps x

List all running processes

What is a virtual console in Linux?

ps aux

List all running programs

Kernel mediates the request for time, memory, disks etc.

fsck

File system check

sync
shutdown


