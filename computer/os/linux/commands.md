


head - 2 /etc/passwd

cut -d ":" -f 1,7 /etc/passwd

cut -c 1- 5 /etc/passwd

grep daemon.*nologin /etc/passwd

grep root /etc/passwd

grep ^root /etc/passwd

grep - v nologin$ /etc/passwd

grep - E "^root|^dbus" /etc/passwd

egrep "(daemon|s).*nologin" /etc/passwd


printf "%s\n" "Hello World"

wc random.txt

wc -L /etc/nsswitch.conf

Every object is a file in Linux. The output device is also an object. A text file is an object. File object is identified by a file descriptor. It is an integer that classifies a process's open files. The file descriptor of an output device is 1. This is the standard output and the abbreviation STDOUT is used.

The default output of standard output is the current terminal. The current terminal is represented by the /dev/tty file.

echo 'Write to the standard output'

Redirection Operator

grep nologin$ /etc/passwd

grep nologin$ /etc/passwd > nologinaccts.txt

less nologinaccts.txt

echo 'Today is Monday' > date.txt

wc -l /etc/passwd >> date.txt

cat date.txt

The file descriptor for standard error is 2. The abbreviation is STDERR. It is sent to the terminal by default. The terminal is represented by /dev/tty.

Redirection operator to send STDERR to a file is 2> operator. 

2>> is append operator.

Find files in /etc directory that contain the hosts: directive.

grep -d skip hosts: /etc/*

grep -d skip hosts: /etc/* 2> err.txt

cat err.txt

&> redirection operator will send the standard error and standard output to the same file.

Ignore error messages by redirecting STDERR to the /dev/null file.

grep -d skip hosts: /etc/* 2> /dev/null

/dev/null is called the black hole.

