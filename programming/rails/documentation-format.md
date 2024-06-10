## Documentation Format

Familiarize yourself with the overall structure of the documentation and conventions. 

- Is it organized around packages or classes?

Use commands to find invocations of any getopt.

(
find . -name '*.ruby' -print | xargs grep getopt
find. -name '*.1' -print | xargs egrep '^\.(Op|Fl)'
) | sort -u

We used the above command to find discrepancies between the documentation and implementation of Unix tools.

## Exercises

What command is needed to find discrepancies between the documentation and implementation?