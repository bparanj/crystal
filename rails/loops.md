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

## Loops and Integer Expressions

Comment on the readability and the code effiency of two alternatives.

What type of argument can cause a function to fail? Under what circumstances could such an argument be given? Propose a simple fix.