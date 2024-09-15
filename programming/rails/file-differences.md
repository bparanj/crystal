## Location File Differences

### Exercise 1

Propose a simple way to calculate a “measure of similarity” metric for two different files. Apply this metric to files in the source collection that share the same file name and create a list of files that could benefit from a structured approach toward code reuse.

To calculate a "measure of similarity" between two files, a simple approach is to use the `diff` command to count the number of differing lines, and then normalize this count by the total number of lines in the larger file. This can provide a rough similarity percentage.

Here's a step-by-step guide to calculate the similarity and identify files that could benefit from structured code reuse:

1. **Calculate Line Differences**:
   Use the `diff` command with the `-U0` flag (unified format with no context lines) to get the number of differing lines:
   ```bash
   diff -U0 file1.c file2.c | grep -c '^\+'
   ```

2. **Get Total Lines**:
   Use `wc -l` to get the total number of lines in each file and take the maximum as the base for normalization:
   ```bash
   total_lines=$(wc -l < file1.c)
   ```

3. **Calculate Similarity Metric**:
   The similarity metric can be calculated by subtracting the differing line count from the total line count and then dividing by the total line count. Multiply by 100 to get a percentage:
   ```bash
   similarity=$(echo "(1 - (differing_lines / total_lines)) * 100" | bc -l)
   ```

4. **Create a Script**:
   Write a script that loops through the files in the source collection, applies the metric to files with the same name, and outputs a sorted list based on the similarity metric.

Here is a bash script that implements this approach:

```bash
#!/bin/bash

SOURCE_DIR="./src"
OUTPUT_FILE="./similarity_report.txt"

# Empty the output file
> $OUTPUT_FILE

# Iterate over each file in the source directory
for file in $SOURCE_DIR/*; do
  filename=$(basename -- "$file")
  
  # Find other files with the same name in the directory tree
  find $SOURCE_DIR -type f -name "$filename" ! -path "$file" | while read -r match; do
    # Calculate differing lines
    differing_lines=$(diff -U0 "$file" "$match" | grep -c '^\+')
    
    # Get the total number of lines from the larger file
    total_lines=$(wc -l < "$file")
    match_lines=$(wc -l < "$match")
    if (( match_lines > total_lines )); then
      total_lines=$match_lines
    fi
    
    # Calculate similarity percentage
    similarity=$(echo "scale=2; (1 - ($differing_lines / $total_lines)) * 100" | bc)
    
    # Output to the file
    echo "$filename: $similarity% similar between $file and $match" >> $OUTPUT_FILE
  done
done

# Sort the output file by similarity percentage in descending order
sort -rn -k2 -t: $OUTPUT_FILE -o $OUTPUT_FILE

# Display the report
cat $OUTPUT_FILE
```

Before running the script, ensure that `bc` (an arbitrary precision calculator language) is installed on your system as it's used to perform the floating-point calculation.

**Note**: This method is very rudimentary and does not account for  code structure or logic. More sophisticated methods, such as token-based comparison or abstract syntax tree (AST) analysis, can give a more accurate measure of code similarity and should be considered for more complex analysis. Tools like Simian (Similarity Analyzer) or PMD's Copy/Paste Detector (CPD) can also be used to detect duplicate code.

### Exercise 2

A number of tools support the organized control of file revisions. If you are using such a tool, examine how you can display the differences between different file versions. Is there a way to display the differing lines in context?

Most version control systems (VCS) like Git provide built-in commands to display differences between file versions. These tools can show the changes in context, giving you insight into what has been added, removed, or altered.

Here's how you can examine differences between file versions and display differing lines in context using Git:

1. **Display Differences Between Revisions**:
   The `git diff` command compares files between commits, branches, working directory, etc. To display differences between two commits, you can use:
   ```bash
   git diff commit1 commit2 -- path/to/file
   ```

2. **Show Changes in Context**:
   By default, `git diff` shows a few lines of context around the changes. You can adjust the number of context lines shown with the `-U` option:
   ```bash
   git diff -U5 commit1 commit2 -- path/to/file
   ```
   The above command shows 5 lines of context around the changes.

3. **Side-by-Side Comparison**:
   For a side-by-side view of the changes, you can use the `--word-diff` flag or external diff tools that support side-by-side display.

4. **Compare Working Directory with Latest Commit**:
   To compare the working directory with the latest commit:
   ```bash
   git diff HEAD -- path/to/file
   ```

5. **View the History of a Single File**:
   You can use `git log` to see the commit history of a file and then use `git diff` to compare specific versions:
   ```bash
   git log -- path/to/file
   git diff <commit-hash-1> <commit-hash-2> -- path/to/file
   ```

6. **Graphical Tools**:
   Git also integrates with graphical diff tools through `git difftool`, which can provide a more user-friendly interface to view changes.

For systems other than Git, similar functionality exists:

- **SVN**: Use `svn diff -r revision1:revision2 path/to/file` to see differences between revisions.
- **Mercurial (hg)**: Use `hg diff -r revision1 -r revision2 path/to/file`.
- **Perforce (p4)**: Use `p4 diff2 file#revision1 file#revision2` to compare two revisions of a file.

These commands and tools allow developers to understand the evolution of a file over time, track down when a particular change was made, and ensure that changes are well-understood and documented.

### Roll Your Own Tool

Sometimes none of the tools at your disposal will handle a mundane and obviously automatable code-reading task. Create your own code-reading tools. The Unix shell with its tools such as sed, awk, sort, uniq and diff can be incrementally combined to obtain the required functionality. 

Modern interpreted programming languages such as Perl, Python, Ruby, and Visual Basic are particularly suited for creating customized code-reading tools. 

Perl, Python, and Ruby have strong support for strings, regular expressions, and associative arrays, simplifying many code-parsing tasks that can be achieved at a lexical level.

Consider one particular example, the location of code lines with an indentation that does not match that of the surrounding code. Such code can be misleading at best and is often an indication of an important program bug.

Implement an indentation verification tool.

The rules we follow when building tools can be summarized as follows.

- Exploit the capabilities of modern rapid-prototyping languages.
- Start with a simple design, gradually improving it as needed.
- Use heuristics that exploit the lexical structure of the code.
- Tolerate some output noise or silence (extraneous or missing output), but remember to take into consideration this noise or silence when using the tool.
- Use other tools to preprocess your input or postprocess your output.

### Exercise 1

Identify code-reading tasks that can benefit by use of a custom-built tool. Briefly describe how each such tool could be built. Implement one of the tools you described.

Code-reading tasks can greatly benefit from custom-built tools that automate and simplify the process. Here are a few tasks and ideas for custom tools:

1. **Code Search and Navigation**:
   - **Tool**: A tool that indexes all code and allows for quick searching and navigation to function definitions, variable declarations, and usage across a large codebase.
   - **Build**: Use text indexing libraries like Apache Lucene or Elasticsearch to create an indexed search system. Integrate with code editors or IDEs via plugins for in-editor navigation.

2. **Dependency Visualization**:
   - **Tool**: A tool that generates visual representations of the dependencies between different parts of the code, such as classes, modules, or services.
   - **Build**: Parse code to extract dependency information and use graph visualization libraries like Graphviz or D3.js to create interactive diagrams.

3. **Code Complexity Analysis**:
   - **Tool**: A static analysis tool that measures code complexity, such as cyclomatic complexity, and highlights areas that may need refactoring.
   - **Build**: Develop a static analysis tool that parses the source code, calculates complexity metrics, and provides a report. Tools like ANTLR can be used to parse different programming languages.

4. **Code Annotation and Documentation Generation**:
   - **Tool**: A tool that extracts comments and annotations from code and generates documentation.
   - **Build**: Use regular expressions or a parser to process code files, extract comments, and then use a documentation generation engine like Sphinx or Doxygen to create human-readable documents.

5. **Code Style Linting and Formatting**:
   - **Tool**: A linter that checks for code style violations according to a predefined style guide and can automatically format code.
   - **Build**: Use existing linter frameworks such as ESLint for JavaScript or RuboCop for Ruby to define custom rules and formatting guidelines.

6. **Automated Code Review**:
   - **Tool**: A tool that automatically reviews code submissions for common errors, potential bugs, and style issues before they're reviewed by a human.
   - **Build**: Integrate static analysis tools, custom linting rules, and maybe even machine learning models to assess code quality and provide feedback.

7. **Code Change Impact Analysis**:
   - **Tool**: A tool that analyzes the potential impact of code changes on the rest of the system.
   - **Build**: Create a tool that uses static analysis and perhaps dynamic analysis to trace through function calls and data flow, reporting potential areas affected by changes.

8. **Duplicate Code Detection**:
   - **Tool**: A tool that identifies duplicate or very similar code segments that could be refactored into shared functions or modules.
   - **Build**: Implement a tool using algorithms like token-based or text-based comparison to find and report duplicate code segments.

9. **Codebase Health Metrics**:
   - **Tool**: A dashboard that provides metrics on codebase health, such as test coverage, bug trends, and code churn.
   - **Build**: Aggregate data from version control systems, build systems, and test frameworks. Display the data in a web dashboard using technologies like Flask or React.

These tools would be built using a combination of programming languages and technologies best suited for the task, like Python for scripting, JavaScript for web interfaces, and existing libraries and frameworks for analysis and visualization. They would be integrated into the development workflow to assist developers in maintaining code quality and understanding the codebase.

### Exercise 2

A pretty-printer typesets source code in a way that makes it easy to read (see Section 10.7). Typically, different fonts or font styles are used for comments, variables, and reserved words. Implement a simple pretty- printer for the language of your choice based on lexical heuristics. To typeset the output you can use Postscript or drive another program: under Unix you can output LaTeX or troff commands.

### Exercise 3

Write a tool that indexes source code files to simplify their browsing. The index entries can be function definitions and declarations. You can present the index as an alphabetically sorted list or an HTML page with hypertext links.
