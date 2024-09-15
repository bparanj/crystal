## Checklist

### Issues

- Is the title of the bug report precise and short?
- Ensure each issue contains a precise description on how to reproduce the problem with a short, self-contained, correct example.
- Triage issues and schedule your work based on the priority and severity of each issue.

### Taking Notes

- Document progress by documenting the steps for investigating and fixing the bug  dead ends. Write down the comands used to log or trace the program.

### Interface

- Carefully examine a method's preconditions and postconditions.

### Error Messages

- Perform a web search regarding error messages by enclosing them in double quotes.

## Guidelines

### Understanding the Interface

Look for open-source software that uses a particular function, and examine how the parameters passed to it are initialized and how its return value is interpreted.

### Search for Error Messages

If the problem is manifesting itself through an error message, start by locating the message’s text within the program’s source code. Your friend here is `fgrep -r`.

### Top Down or Bottom Up

Work bottom up in the case of failures that have a clearly identifiable cause, such as crashes, freezes, and error messages.

Work top down in the case of failures that are difficult to pin down, such as performance, security, and reliability.

## Questions

- How do they track plan releases?
- How is the work items prioritized?
- Where is common issues and solutions documented?
- How is the release notes generated?
- How to learn from the defects in the issue tracking system?
- Is there a code specific search engine?
