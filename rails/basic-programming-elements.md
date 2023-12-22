## Basic Programming Elements

"Code reading is in many cases a bottom-up activity" means that the process often starts by looking at specific details, like individual lines or blocks of code, and then gradually understanding the larger structure or system. Instead of starting with an overall picture (top-down), it begins with the smaller components to build an understanding of the entire codebase.

- What are the basic code elements that comprise the programs?
- How to read and reason about the basic code element?

Dissect a simple program to demonstrate the type of reasoning needed for code reading. 

- How to identify common traps and pitfalls that we should watch for when reading code?
- What idioms can be useful for understanding the meaning of the code?
- How to examine the functions, control structures and expressions that make up a program?
- What are the common control constructs of Ruby?
- How to reason about a program's flow of control at an abstract level and extract semantic meaning out of its code elements?

Elements of a program:

- Header files - use library functions

- What are the header files needed for each function?
- Run the code through the compiler looking for warning messages.
- Where does the program begin its execution? This is a good starting point for examining a program.

As you read the program, note down:

- Comments
- Library headers
- Function declaration
- Program starting location
- Arguments to the program

Using uninitialized variables is a common cause of problems. When inspecting code, always check that all program control paths will correctly initialize variables before these are used. Some compilers may detect some of these errors, but you should not rely on it.

- How to identify all the program control paths?

As you read the code, note down the reasons why something can fail.

- Is there a chance for the program to fail silently? 
- Can we lose output without any warning?

## Exercises

Experiment to find out how Ruby deals with uninitialized variables. Outline your results and propose an inspection procedure for locating uninitialized variables.

Look for code that does not verify the result of library calls. Propose practical fixes.

Sometimes executing a program can be a more expedient way to understand an aspect of its functionality than reading its source code. Devise a testing procedure or framework to examine how programs behave on write errors on their standard output. Try it on a number of character-based Ruby programs (such as the command-line version of your interpreter) and report your results.

Identify the require statements needed for using ActiveRecord library outside of Rails.
