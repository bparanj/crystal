## Code Searching

### grep

The following sequence displays the file and the line containing the definition for the function strregerror in the source code of sed.

```
$ grep ′^strregerror′ *.c 
misc.c:strregerror(errcode, preg)
```

To find both the definition and all uses, we can use the name of the function as the regular expression.

```
$ grep strregerror *.c
compile.c: err(COMPILE, "RE error: %s", strregerror(eval, *repp)); misc.c:strregerror(errcode, preg)
process.c: err(FATAL, "RE error: %s", strregerror(eval, defpreg));
```

If you are not sure what you are looking for and where to start searching, you can use grep to search through the code with a keyword that the word will be mentioned in a comment or be part of an identifier. To ensure that capitalization and the word's ending and derivatives do not overly restrict your search space, search using the word's stem, omitting its initial character. In the following example we are looking for code associated with the compilation process.

```
$ grep ompil *.c
[...]
compile.c: p = compile–re(p, &a->u.r);
main.c: * Linked list pointer to compilation units and pointer to main.c: compile();
main.c: * Add a compilation unit to the linked list
```

You can also use grep to search through the output of other tools. For example, in a project with numerous source files you can use grep to search the file list for a file that might interest you.

```
$ ls | grep undo v–undo.c
```

Sometimes you do not want to read the code that contains a regular expression but are interested only in the files that contain it. The -l option of grep will display (once) the name of every file that contains the given regular expression.

```
$ grep -l xmalloc *.c *.h compile.c
main.c
misc.c
extern.h
```

ou can then use this output to automatically perform a specific task on all those files. Typical tasks might be editing each file to further scrutinize it or locking each file under a revision control system. In Unix-type shells you can accomplish this by enclosing the output of grep in backticks.

```
emacs `grep -l xmalloc *.c`
```

The most useful editing command is the substitution command (s), which is specified as follows.

```
s/regular expression/replacement/flags
```

The command will locate text matching the regular expression and replace it with the replacement text. In the replacement text you can use the special expression $n to indicate the nth parenthesized part of the regular expression (for example, $1 will match the first parenthesized part of the regular expression). The flags are single- character modifiers that change the command behavior. The most useful flag is g, which makes the substitution change all nonoverlapping occurences of the regular expression and not just the first one, as is the default behavior.

Page 490 to 501

## Exercises

Often programmers identify code parts that need further attention by using a special marker such as XXX or FIXME. Search for, count, and examine such instances in the source code tree.

The system call declarations in this book's Unix source distribution are generated from a single file. See page 779. Locate the definition of the first 20 system calls in the source tree. Automate this task as much as possible.

The task of locating underline-separated identifiers involved hand-editing the output list to remove identifiers that are part of the system libraries (for example, size–t). Propose a way to automate this task, taking into account that the identifiers used by system libraries are all declared in include files that you can process.

To automate the task of filtering out underline-separated identifiers that are part of system libraries, we can create a script that processes both the source code and the system include files. The script would:

1. **Extract Identifiers**:
   - Parse the source code to extract all underline-separated identifiers.

2. **Identify System Identifiers**:
   - Parse the system include files to create a list of identifiers declared in these files.

3. **Filter Out System Identifiers**:
   - Compare the list of extracted identifiers with the list of system identifiers.
   - Remove any matches from the extracted identifiers list.

Here’s a high-level description of the steps the script would follow:

1. **List System Identifiers**:
   - Use a tool like `grep` or `ctags` on the system include directory to list all identifiers.
   - Store these identifiers in a set or hash table for fast lookup.

2. **List Project Identifiers**:
   - Use the same tool on the project source files to list all identifiers.
   - For each identifier, use a regular expression to check if it is underline-separated (e.g., `grep '_[a-zA-Z0-9]*_'`).

3. **Filter Identifiers**:
   - For each underline-separated identifier from the project, check if it exists in the system identifiers set.
   - If it does, skip it; otherwise, include it in the final list.

4. **Output**:
   - Save the filtered list of identifiers to a file or display them as output.

By processing the identifiers in this manner, you can effectively automate the exclusion of system library identifiers from your list. This approach assumes you have a Unix-like environment with tools like `grep` or a programming language like Python or Ruby that can be used to run regular expressions and perform file I/O operations.

For more advanced filtering, you might consider lexical analysis tools or libraries that can parse C/C++ code and provide more accurate extraction of identifiers.

Write a shell script or a batch file that uses grep, regular expressions, and other tools to list coding standard violations in a set of source files. Document the violations caught and the type of spurious noise that can be expected.

Below is a basic shell script that uses `grep` to list potential coding standard violations in a set of C source files. This example checks for a few common C coding standards, such as the use of tabs instead of spaces, lines ending with whitespace, and functions exceeding a certain length in lines.

```bash
#!/bin/bash

# Define the directory containing the source files
SOURCE_DIR="./src"

# Define the maximum allowed function length
MAX_FUNC_LENGTH=50

# Function to check for the use of tabs
check_tabs() {
  echo "Checking for tabs instead of spaces..."
  grep -Pn "\t" $SOURCE_DIR/*.c
}

# Function to check for trailing whitespace
check_trailing_whitespace() {
  echo "Checking for trailing whitespace..."
  grep -Pn "[ \t]+$" $SOURCE_DIR/*.c
}

# Function to check for functions that exceed the maximum length
check_func_length() {
  echo "Checking for functions exceeding $MAX_FUNC_LENGTH lines..."
  awk '/\{/{c=0;func=$0}/\}/{if(c>'"$MAX_FUNC_LENGTH"'){print func, "exceeds max length:", c+1}}{c++}' $SOURCE_DIR/*.c
}

# Run the checks
check_tabs
check_trailing_whitespace
check_func_length

# Document potential noise
echo "Potential spurious noise:"
echo "- Legitimate use of tabs for alignment within comments or strings."
echo "- Trailing whitespace may appear in comments or multi-line macros."
echo "- Long functions might be correctly using nested blocks or have embedded documentation."
```

To use this script:

1. Save the code to a file, for example, `check_code_standards.sh`.
2. Give it execute permissions with `chmod +x check_code_standards.sh`.
3. Run the script in the terminal with `./check_code_standards.sh`.

This script should be run from a directory that has access to the `src` directory containing the source files. Adjust the `SOURCE_DIR` variable as needed to point to the  source files location.

**Violations Caught**:
- Use of tabs instead of spaces (coding standards may require spaces for indentation).
- Lines ending with whitespace (often considered untidy or unnecessary).
- Functions that exceed a certain length, which can be a sign of functions doing too much and may need refactoring.

**Spurious Noise**:
- **Tabs**: If tabs are used within comments for alignment or in string literals, these would be reported as violations but might be acceptable per the project's standards.
- **Trailing Whitespace**: Whitespace at the end of lines could be part of multi-line macro definitions or in comments for formatting, which might not be  violations.
- **Function Length**: The script does not differentiate between code and comments or recognize nested blocks, so it may report long functions that are ly well-structured or contain embedded documentation.

This script is quite basic and serves as a starting point. In practice, more sophisticated tools and linters, such as `clang-tidy`, `cpplint`, or static analysis tools, should be used for comprehensive coding standard checks, as they can provide more context-sensitive analysis and reduce noise.


