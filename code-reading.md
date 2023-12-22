## Code Analysis

When reading code ask yourself:

- Why is this written this way?
- What in the author's background would lead him to this choice?

This mode is reviewing code for problems. You are looking for patterns and clues. Use incongruities you find to double check your understanding.

- Do you see any bugs or dubious coding practices?

Fixing bug in a big codebase:

- How do you start?
- How can you assess the impact of a change you are thinking of making?
- What methods do you use to identify or understand what you are observing?

You're asking about the process or techniques used to recognize or interpret code.

## Action Items

- Document useful grep and find commands used to read code.
- Write code to help you read code.

## Code Comprehension

- Read
- Comment
- Experiment
- Learn

Go beyond just reading code by actively engaging with it through commenting, experimenting and learn about the code. Gain insights on how to structure and program big systems.

## Analysing Code

- Programming Constructs
- Data Types
- Data Structures
- Control Flow
- Project Organization
- Coding Standards
- Style and Documentation Conventions
- Architecture

## Making Changes

- Read
- Understand
- Modify

## Goal of the Book

- Be able to read and understand big codebase.
- Appreciate important software development concepts.
- Know how to explore large bodies of code.
- Be able to read and understand many important programming languages, both advanced and basic.
- Appreciate the intricacies of real software projects.

## Code Reading Guidelines

Ability to recognize bad code is a valuable skill. Bad code has:

- An inconsistent coding style
- A gratuitously complicated or unreadable structure 
- Obvious logical errors or omissions
- Overuse of nonportable constructs
- Lack of maintenance

Read code selectively and with a goal in your mind. Are you trying to learn new patterns, a coding style, a way to satisfy some requirements?

Notice the nonfunctional requirements that gives rise to a specific implementation style.

### Step 1

Start with small programs. Build the programs you study and run them. This will provide you with immediate feedback on the way the code is supposed to work and a sense of achievement.

### Step 2

Actively change the code to test your understanding. Begin with small changes and gradually increase their scope. Your active involvement with real code can quickly teach you the basics of the new environment.

Read related books, documentation, or manual pages, or attend training courses; the two methods of learning complement each other.

Another way to actively read existing code is to improve it. Think about how you can improve it. This can involve using a better design or algorithm, documenting some code parts, or adding functionality. Document your understanding of the code in improved documentation.

## Code as Exemplar

Sometimes, when trying to understand how a particular feature in software works, you can find explanations in textbooks or articles. But often, the best way to learn “how it's done” is by reading the actual code. This approach is not only useful for understanding the functionality but also essential for developing software that needs to be compatible with that existing code.

Be flexible. Use a number of different strategies to understand how the code works. Start with any documentation. Use the system to get a feel for its external interfaces. Understand what you are looking for:

- A system call
- An algorithm
- Code sequence
- An architecture

Devise a strategy that will uncover the target.

- Trace through the instruction execution sequence. Run the program and place a breakpoint in a strategic location.
- Textually search through the code to find specific code or data elements.
- Use tools to locate the code.

Once you locate the desired code, study it, ignoring irrelevant elements.

If you find it difficult to understand the code in its original context, copy it into a temporary file and remove all irrelevant parts. The formal name of this procedure is slicing.

## Maintenance

Code may need fixing. If you have found a bug in a large system, you need strategies and tactics to let you read the code at increasing levels of detail until you have found the problem. Use tools such as the debugger, the compiler's warnings or symbolic code output, a system call tracer, your database's Structured Query Language (SQL) logging facility, packet dump tools to locate a bug's location.

Examine the code from the problem manifestation to the source of the problem. Follow only the related paths. Use debugger's stack trace, single stepps and breakpoints to narrow down the search.

Add print statements in strategic locations of the execution path. For OS interfaces, system call tracing is useful.

## Evolution

80% of the time is spent in:

- Add new functionality
- Modify existing feature
- Adapt it to new environments and requirements
- Refactor it to enchance nonfunctional qualities

In these cases, be selective and narrow the focus to the sections of the code that are relevant to the current problem.

When looking at a large codebase, choose which parts to focus on. Instead of trying to understand every detail of the entire codebase, it's more effective to target specific sections that are most relevant to what you need to know or solve. 

In most cases, you have to understand a very small percentage of the overall system's implementation. Selectively understand and change one or two files. The strategy for dealing with parts of a large system:

- Locate the sections of code that interest you
- Understand the specific parts in isolation
- Infer the code excerpt's relationship with the rest of the code

When adding a new functionality to a system:

Find the implementation of a similar feature to use as a template for the feature to be implemented.

When modifying an existing feature:

First locate the underlying code.

To go from a feature's functional specification to the code implementation:

- Follow the string messages
- Search the code using keywords

Once you have located the feature, study its implementation by following relevant code sections. Design the new feature or addition, locate its impact area - the rest of the code that will interact with your new code. In most cases, these are the only code parts you will need to thoroughly understand.

Page 53: Using compiler to locate the relevant code that will be impacted.

Note:

"Follow the string messages" typically means to trace or track the flow of text messages or strings within a program or system. This can involve understanding how these strings are created, modified, and used throughout the application, often for the purpose of debugging, localizing, or comprehensively understanding the system's operations. It's about paying attention to how textual data is handled and processed.

"Code parts" generally refers to various segments or components of a programming code. This can include functions, classes, modules, or any distinct sections within a larger codebase. Each part usually serves a specific purpose or function within the program. 

THINK:

Can we use failing test as a way to minimize code-reading efforts to find the impact of change?

When looking for code to reuse in a specific problem you are facing, first isolate the code that will solve your problem. A keyword-based search through the system's code will in most cases guide you to the implementation. If the code you want to reuse is intractable, difficult to understand and isolate, look at larger granularity packages or different code.

Another reuse activity involves proactively examining code to mine reusable nuggets. Here your best bet is to look for code that is already reused, probably within the system you are examining.

### Nonfunctional Issues

- Does the code fit with your organization's development standards and style guides? 
- Is there an opportunity to refactor? 
- Can a part be coded more readably or more efficiently? 
- Can some elements reuse an existing library or component?

Examine the file and directory structure, the build and configuration process, the user interface and the system's documentation.

## Commands

find /mydir -name '*.ruby' -print | xargs grep 'find_by'

## Top 10 Languages

The most commonly used programming languages in open source projects:

1. **JavaScript**: Widely used for web development.
2. **Python**: Known for its simplicity and versatility.
3. **Java**: Popular in enterprise environments and Android app development.
4. **C**: Used in system programming and embedded systems.
5. **C++**: Known for performance-critical applications.
6. **Ruby**: Favored for its elegant syntax, often used in web development.
7. **PHP**: Commonly used for server-side web development.
8. **C#**: Used in a variety of applications, including game development.
9. **TypeScript**: A superset of JavaScript, adding static types.
10. **Go**: Known for its simplicity and efficiency in system and network programming.

These languages are popular due to their robust communities, comprehensive libraries, and versatility in various types of projects. 

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

## Functions

- What are the control flow statements available in Ruby?
- Where is the main code body?
- Identify the major parts of a program. It could be variables and functions.

To understand what a function (or method) is doing you can employ one of the following strategies.

- Guess, based on the function name.
- Read the comment at the beginning of the function. 
- Examine how the function is used.
- Read the code in the function body.
- Consult external program documentation.

When you read code:

- What are the naming conventions for the variables and functions?

Test your initial guess by running appropriate test cases.

This form of gradual understanding is common when reading code; understanding one part of the code can make others fall into place. Based on this form of gradual understanding you can employ a strategy for understanding difficult code similar to the one often used to combine the pieces of a jigsaw puzzle: start with the easy parts.

## Exercises

Examine the visibility of functions and variables in programs in your environment. Can it be improved?

Determine the role of a function. Try to minimize the time spent on each function. Order the strategies by their success rate.

## Loops, Conditions and Blocks

Read the documentation of the library you use. It will enhance your code reading and writing skills.

## Exercises

Discover how the editor can identify matching braces and parentheses.

Examine all control structures that do not use braces and mark the statements that will get executed.

This instruction means to carefully review the sections of code where control structures (like `if`, `for`, `while` statements) are used without curly braces `{}`. You should identify and highlight which specific lines or commands will be executed as part of these control structures. This is important because in many programming languages, if braces are not used, only the immediately following statement is considered part of the control structure. Identifying these statements ensures clarity in understanding the code's flow and logic.

Verify that the indentation of a function matches the control flow.

The mandatory use of braces in Perl's control structures contributes to consistent and clear code formatting. This requirement ensures that the scope of each control structure is visually distinct and easy to identify, reducing ambiguity about which statements are controlled by structures like `if`, `while`, or `for`. This can enhance readability, making it easier for programmers to understand and maintain the code, especially in complex or nested structures. Consistency in code structure is often valued for its contribution to overall code clarity and maintainability.

## Switch Statements

When examining code, look out for common errors in switch-case and other control structures.

Examine the handling of unexpected values in switch statements in the programs you read. Propose changes to detect errors. Discuss how these changes will affect the robustness of programs in a production environment.

Is there a tool or a compiler option in your environment for detecting missing break statements in switch code? Use it, and examine the results on some sample programs.

## Loops

The pattern for reading code emerges slowly. Code reading involves many alternative strategies: bottom- up and top-down examination, the use of heuristics, and review of comments and external documentation should all be tried as the problem dictates.

```
for (i = 0; i < len; i++) {
```

Loops of this type appear very frequently in programs; learn to read them as "execute the body of code len times."

Mark sections of code and label the purpose. For example:

- Parse
- Convert
- Error handling
- Verify ascending order
- Break out of loop
- Verify valid X

## Exercises

- What are the different uses of for statement?
- Which is more readable for or while?
- Is there style guideline when while loops should be used instead of for loops?
- Where will the execution be transfered when break and continue is hit?

## Character and Boolean Expressions

Dissect a complex expressions into smaller expressions. We can understand the meaning of an expression by applying it on sample data. Create a table containing the values of all variables and expression parts as each expression part is evaluated. After the loop terminates we can see a picture emerging.

De Morgan's rules provide you a quick and easy way to disentangle a complicated logical expression. Concepts:

- Conjunction
- Disjunction
- Short-circuit evaluation 

## Exercises

Find, simplify, and reason about five nontrivial Boolean expressions in the source code base. Do not spend time on understanding what the expression elements mean; concentrate on the conditions that will make the expression become true or false. Where possible, identify and use the properties of short-circuit evaluation.

Locate and reason about five nontrivial integer or character expressions in the source code base. Try to minimize the amount of code you need to comprehend in order to reason about each expression.




















