Below are simple code examples in Haskell, illustrating each of the terms as expressions. Haskell is chosen for its clarity in demonstrating these concepts, especially given its expression-oriented nature.

### Literals

Numeric, string, and boolean literals:

```haskell
42          -- Numeric literal
"hello"     -- String literal
True        -- Boolean literal
```

### Constructions

Constructing a list (a complex data structure) using list literals and tuple construction:

```haskell
[1, 2, 3]          -- List construction
(4, "five")        -- Tuple construction
```

### Function Calls

Calling a standard library function and a user-defined function:

```haskell
abs (-5)            -- Standard library function call

double x = x * 2    -- User-defined function
double 4            -- Calling the user-defined function
```

### Conditional Expressions

Using `if-else` to choose between two values:

```haskell
if x > 0 then "positive" else "non-positive"
```

### Iterative Expressions

Haskell uses recursion instead of traditional iterative constructs for looping, illustrating with a function that sums a list:

```haskell
sumList :: [Int] -> Int
sumList [] = 0
sumList (x:xs) = x + sumList xs
```

### Constant and Variable Accesses

Accessing a constant and a variable (Note: Haskell uses `let` or top-level definitions for constants, and variable bindings are immutable):

```haskell
piValue :: Double            -- Constant access
piValue = 3.14159

let x = 10 in x              -- Variable access within a `let` expression
```

Each of these examples demonstrates the fundamental building blocks of expressions in Haskell, showcasing how literals, constructions, function calls, conditional expressions, and more, contribute to the language's ability to express complex computations and data manipulations in a concise and type-safe manner.
