## Bisect

Used for finding regression bugs.

```
git bisect start
git bisect good <good-commit>
git bisect bad <bad-commit>
```

Repeat to find the first bad commit. 

Exit bisect session:

```
git bisect reset. 
```

## Example

```
git log --oneline
```

## Automating Bisect

```
git bisect run
```

## Blame

```
git blame <file-name>
```

Filter based on line numbers in the file:

```
git blame -L 67, 82 <file-name>
```

```
git show <commit-id>
```

## Search

```
git grep [options] pattern
```

```
git grep 'error'
```

```
git grep 'error' -- '*.js'
```

-n - Display line number

```
git grep '[0-9]*error'
```

```
git grep 'error' branch-name
```

```
git grep --format="%f:%1:%0" "error"
```

## Comparison with Unix Search

Here's a table that compares the differences between `git grep` and Unix `grep`:

| Feature/Aspect            | Unix `grep`                       | Git `grep`                                 |
|---------------------------|-----------------------------------|--------------------------------------------|
| **Context of Search**     | Filesystem; any text files        | Only Git repository; tracked files         |
| **Scope of Search**       | Any directory or file             | Files in the Git repository                |
| **Version Control**       | Independent of VCS                | Integrated with Git; searches across commits and branches |
| **Performance**           | Varies with file system           | Often faster within Git repos due to indexing and compression |
| **Special Features**      | General text pattern search       | Git-specific features like searching in staged files, specific commits |
| **Usage Flexibility**     | Can be used outside Git repos     | Limited to Git repositories                |
| **Integration**           | Not integrated with Git           | Seamless integration with Git features    |
| **Search in History**     | Not applicable                    | Can search across different versions and branches |
| **Handling of .gitignore**| Does not recognize `.gitignore`   | Respects `.gitignore` settings             |

This table outlines the primary differences, emphasizing the context-specific functionalities and integration aspects of each tool.
