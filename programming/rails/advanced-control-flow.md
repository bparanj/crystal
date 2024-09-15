## Advanced Control Flow

How to locate recursive function in Rails code base?

Locating recursive functions in a Rails codebase involves a few steps, particularly if you're dealing with a large and complex codebase. Here are some strategies:

1. **Code Search**:
   - Use code search tools like `grep`, `ag` (The Silver Searcher), or `ripgrep` to search through the code.
   - You can run a command in the root of the Rails project to search for common patterns used in recursive functions. For example: `grep -r "def " * | grep "self"`

2. **IDE Features**:
   - Many Integrated Development Environments (IDEs) and code editors like Visual Studio Code, RubyMine, or Atom have powerful search functionalities.
   - Use the search feature to look for keywords like `def` along with the name of the function being called within the same function, which is a sign of recursion.

3. **Understanding Code Logic**:
   - Familiarize yourself with the parts of the application where recursion might be  used, such as tree-like data structures, algorithm implementations, or complex data processing.
   - Manually review these areas to identify recursive patterns.

4. **Documentation and Naming Conventions**:
   - Check the project's documentation for any mention of recursive methods.
   - Look for function names that might suggest recursion, like `traverse`, `search`, `calculate`, etc.

5. **Ask the Team**:
   - If you're working in a team, ask other developers if they are aware of recursive methods in the codebase.

Recursive functions calls itself within its body, possibly with different arguments. They are often used for tasks that involve repetitive processing of data, like traversing hierarchical structures or performing iterative calculations until a condition is met.

Construct a simple tool to locate recursive function definitions. Run it on the source code and reason about the workings of three different recursive functions.

Locate a Ruby function calling sequence that signals errors through exceptions, and rewrite it so that it does not rely on them by modifying the function return values. Compare the readability of the two approaches.

- How can I create a drawing of exception propagation tree for Rails codebase?

Creating a drawing of an exception propagation tree for a Rails codebase involves mapping out how exceptions are raised, handled, and propagated through different layers and components of the application. Here's a step-by-step approach to create this drawing:

1. **Understand the Codebase**:
   - Familiarize yourself with the key components of your Rails application,  models, controllers, views, and any middleware.
   - Identify where exceptions are likely to be raised (e.g., database operations, external API calls).

2. **Trace Exception Flow**:
   - Manually trace or use debugging tools to follow the flow of an exception from the point where it is raised to where it is caught or propagated.
   - Note how different parts of the application (controllers, models, services, etc.) handle exceptions.

3. **Identify Common Exceptions**:
   - List common exceptions in Rails, such as `ActiveRecord::RecordNotFound`, `ActiveRecord::RecordInvalid`, and custom exceptions defined in the application.

4. **Use a Diagramming Tool**:
   - Choose a diagramming tool like Lucidchart, Draw.io, or even Microsoft Visio for drawing the tree.
   - Start with the points where exceptions are raised and draw branches showing how they propagate through the application layers.

5. **Represent Exception Handlers**:
   - Include exception handlers such as `rescue_from` in controllers or global exception handlers in `ApplicationController` or middleware.
   - Show how different handlers manage or transform exceptions.

6. **Review and Refine**:
   - Iteratively review the diagram to ensure it accurately represents the exception flow.
   - Consider getting feedback from team members to refine the diagram.

7. **Document and Share**:
   - Once complete, document what each part of the tree represents.
   - Share the diagram with your team as a reference for understanding exception handling in your Rails application.

This diagram can be an invaluable resource for both new and existing team members to understand how the application deals with runtime exceptions, aiding in debugging and enhancing error handling strategies.

Look for code that checks return value to indicate failure. Sketch how parts of the code can be rewritten in Ruby using exceptions.
