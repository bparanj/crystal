In Haskell, the `Bool` type is a fundamental algebraic data type representing boolean values, which are either `True` or `False`. While the `Bool` type is predefined in Haskell, if you were to define it yourself as an educational exercise, it would look like this:

```haskell
data Bool = True | False
```

### Explanation:

- `data Bool` declares a new algebraic data type named `Bool`.
- `True | False` specifies that `Bool` has two value constructors: `True` and `False`. This means an instance of `Bool` can be either `True` or `False`, and nothing else. The vertical bar `|` is used to separate different constructors for the type, indicating a sum type, which means the type is a choice between several options (in this case, two).

This definition is an example of a simple sum type because it defines a type (`Bool`) that can have one of a fixed set of possible values (`True` or `False`). Each of these values is represented by a value constructor with the same name. Since `Bool` is so fundamental, it's built into the Haskell language and available by default, so you wouldn't normally need to define it yourself. However, understanding how such basic types could be defined helps grasp the concept of algebraic data types in Haskell.

## Negate Function

Using the `Bool` algebraic data type (ADT) and its constructors `True` and `False`, you can implement a `negate` function that takes a `Bool` value and returns its negation. In Haskell, this function would flip `True` to `False` and vice versa. Here's how you can implement it:

```haskell
negateBool :: Bool -> Bool
negateBool True = False
negateBool False = True
```

### Explanation:

- The function `negateBool` is defined with a type signature `Bool -> Bool`, indicating it takes a `Bool` value as input and returns a `Bool` value as output.
- The function uses pattern matching on its input:
  - If the input is `True`, it returns `False`.
  - If the input is `False`, it returns `True`.

This implementation leverages the power of pattern matching in Haskell, which allows for concise and readable definitions of functions that operate on ADTs.
