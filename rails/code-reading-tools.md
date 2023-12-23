## Code Reading Tools

- Identify the declaration of a particular entity to determine the type of a function, variable, method, template, or interface.
- Locate where a particular entity is defined, for example, find the body of a function or class.
- Go through the places where an entity is used.
- List deviations from coding standards.
- Discover code structures that might help you understand a given fragment.
- Find comments explaining a particular feature.
- Check for common errors.
- View the code structure.
- Understand how the code interacts with its environment.

- What tools can automate these tasks?
- How to reverse engineer a system's architecture?
- How can we automatically create project documentation from specially formatted source code?

We start with tools that operate on source code at a lexical level (process characters without parsing the program structure). Continue with tools based on code parsing and compilation. Finish with an overview of tools that depend on the code execution.

### Regular Expressions

The tools that operate on source code at a lexical level are powerful and often underestimated. They can be used on any programming language or platform, operate without a need to preprocess or compile files, handle a wide variety of tasks, execute swiftly, and handle arbitrary amounts of program text. Using such tools, you can efficiently search for patterns in a large code file or across many files. These tools are by their nature imprecise; however, their use can save you time and yield results that might escape casual manual browsing.

The power and flexibility of many lexical tools come from the use of regular expressions. You can think of a regular expression as a recipe for matching character strings. A regular expression is composed from a sequence of characters. Most characters match only with themselves, but some characters, called meta-characters, have special meaning. You create regular expressions by using a combination of regular characters and meta-characters to specify a recipe for matching the exact code items you may be looking for.

Page 483: Table 10.1 Common Regular Expression Building Blocks

and Table 10.2

Page 483 to 486.

### Exercises

Learn the regular expression syntax provided by the editor you are using. Experiment with any additional features it provides. Try to express the additional features using only the meta-characters we have described. Comment on the relative merits of a rich regular expression syntax versus the cost of learning it.

Write regular expressions to locate integers, floating-point numbers, and a given word within a character string. Where would you use such expressions?

Write regular expressions to locate violations from the style guide used in the source code you are reading.