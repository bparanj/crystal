## Copilot

Using GitHub Copilot effectively in software development. Key points:

1. Utilize specific, concise prompts for better Copilot responses.
2. Understand the role of context in influencing Copilot's outputs.
3. Adopt an iterative approach to refine Copilot's suggestions.
4. Use Copilot for various coding tasks, including debugging and refactoring.
5. The developer's expertise is crucial in guiding and verifying Copilot's outputs.
6. Copilot is a tool that complements, not replaces, the developer's skills.

To use GitHub Copilot effectively:

1. Understand Copilot as a Tool: Recognize it's a tool for code completion, providing suggestions based on context.
2. Context Matters: The current file and open tabs in the IDE provide context to Copilot.
3. Adapt Workflow: Regularly use Copilot during coding for best results.
4. Effective Prompt Crafting: Be clear and specific in comments and code to guide Copilot.
5. Utilize Examples: Providing examples helps Copilot generate accurate suggestions.
6. Follow Best Practices: Describe goals at the file’s top, be flexible with suggestions, and keep relevant files open.
7. Naming Conventions and Good Code: Proper naming and following coding best practices help Copilot generate better code.
8. Go with the Flow: Be adaptable and open to Copilot’s probabilistic nature.

1. Provide a high level goal 

- How should I break down the problem so we can solve it together? 
- How would I approach pair programming with this person?

```javascript
/*
Create a basic markdown editor in Next.js with the following features:
- Use react hooks
- Create state for markdown with default text "type markdown here"
- A text area where users can write markdown 
- Show a live preview of the markdown text as I type
- Support for basic markdown syntax like headers, bold, italics 
- Use React markdown npm package 
- The markdown text and resulting HTML should be saved in the component's state and updated in real time 
*/
```

This level of detail helps you to create a more desired output, but the results may still be non-deterministic. 

2. Question must be simple and specific. Aim for a short output from Copilot.

Task Decomposition: Express the logic and steps needed to achieve the goal.

3. Provide examples

```javascript
// Map through an array of arrays of objects
// Example: Extract names from the data array
// Desired outcome: ['John', 'Jane', 'Bob']
```

Define the input and output requirements.

```javascript
# Implement the function calculate_average_grade in grades.py that takes a list of grades as input and returns the average grade as a floating-point number
```

## Use Cases

- Code suggestions
- Generate unit tests
- IaC development
- Code translation
- Dictionaries with lookup data
- Explain code
- Fix problems
- Document code

### Explain Command

Copilot /explain command can be used for syntactic level and semantic level explanation of the code.
