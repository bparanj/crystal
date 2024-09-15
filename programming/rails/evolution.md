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

Refer page 53 of Code Reading Open Source Perspective: Using compiler to locate the relevant code that will be impacted. Note:

"Follow the string messages"  means to trace or track the flow of text messages or strings within a program or system. This can involve understanding how these strings are created, modified, and used throughout the application, often for the purpose of debugging, localizing, or comprehensively understanding the system's operations. It's about paying attention to how textual data is handled and processed.

"Code parts" generally refers to various segments or components of a programming code. This can include functions, classes, modules, or any distinct sections within a larger codebase. Each part usually serves a specific purpose or function within the program. 

THINK:

Can we use failing test as a way to minimize code-reading efforts to find the impact of change?

When looking for code to reuse in a specific problem you are facing, first isolate the code that will solve your problem. A keyword-based search through the system's code will in most cases guide you to the implementation. If the code you want to reuse is intractable, difficult to understand and isolate, look at larger granularity packages or different code.

Another reuse activity involves proactively examining code to mine reusable nuggets. Here your best bet is to look for code that is already reused, probably within the system you are examining.

