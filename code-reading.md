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

Code may need fixing. If you think you have found a bug in a large system, you need strategies and tactics to let you read the code at increasing levels of detail until you have found the problem. The key concept in this case is to use tools. Use the debugger, the compiler's warnings or symbolic code output, a system call tracer, your database's Structured Query Language (SQL) logging facility, packet dump tools to locate a bug's location.





