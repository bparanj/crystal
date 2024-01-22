## Effective Haskell

- Reliable
- Predictable
- Maitainable

Easily scaled horizontally.

- Immutability
- Free of side effects
- Type system

What is a Haskell language extension?

Haskell language extension add new features and you can enable specific language features.

Used for:

- Web apps
- Data pipelines
- Compilers
- Configuration management tools

- Power
- Flexibility
- Correctness

## First Program

Create Main.hs file. 

```haskell
module Main where
main = print "This is a great book"
```

Compile:

```
ghc Main
```

Run:

```
./Main
```

Compile and run:

```
runhaskell Main.hs
```

Experimenting during development:

```
$ ghci
GHCi, version 9.4.8: https://www.haskell.org/ghc/  :? for help
ghci> :load Main.hs
[1 of 2] Compiling Main             ( Main.hs, interpreted )
Ok, one module loaded.
ghci> main
"This is a great book"
```

## Concepts

- Anonymous Function
- Nest Anonymous Function
- Currying
- Fully Saturated
- Partially Applied
- Eta Reduction
- Eta Expansion
- Infix
- Partially Apply Operator
- Infix Function
- Flip Function
- Composing Function
- Function Application Operator
- Function Composition Operator
- Higher Order Function
- Fixity
- Pattern Matching
- Destructuring Lists

### Currying

Convert a function that takes multiple arguments into a series of single-argument functions.

### Fully Saturated

When a function is called with all of its arguments and can return a value that is not a function.

### Partially Applied

Call a function with only some of its arguments.

## Flip Function

Apply only the second argument of a function.





## Research

- How to infer types in Ruby program?

