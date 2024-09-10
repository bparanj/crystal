


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