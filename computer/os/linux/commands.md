Create an exercise to practice:

Text File Records A text file record is a single file line that ends in a newline line-
feed, which is the ASCII character LF. You can see if your text file uses this end-of- line
character via the cat - E command. It will display every newline linefeed as a $. If your
text file records end in the ASCII character NUL, you can also use cut on them, but you
must use the - z option.


head - 2 /etc/passwd

cut -d ":" -f 1,7 /etc/passwd

cut -c 1- 5 /etc/passwd

grep daemon.*nologin /etc/passwd

grep root /etc/passwd

grep ^root /etc/passwd

grep - v nologin$ /etc/passwd

grep - E "^root|^dbus" /etc/passwd

egrep "(daemon|s).*nologin" /etc/passwd


$ cat alphabet.txt
Alpha
Tango
Bravo
Echo
Foxtrot

$ sort alphabet.txt
Alpha
Bravo
Echo
Foxtrot
Tango

cat counts.txt
105
8
37
42
54
$

sort counts.txt

sort -n counts.txt

printf "%s\n" "Hello World"