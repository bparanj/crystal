In Haskell, an explicit type is when you directly specify the type of a variable, function, or expression using a type annotation. Haskell is a statically typed language, meaning that the type of every expression is known at compile time. While Haskell has a powerful type inference system that can often determine types without explicit annotations, specifying types explicitly can improve code readability, make errors easier to understand, and serve as documentation.

### Syntax for Explicit Types

Type annotations in Haskell are written using the `::` operator, followed by the type. Here's the general syntax:

```haskell
expression :: Type
```

### Examples

1. **Explicit Type for Variables**

   You can specify the type of a variable explicitly:

   ```haskell
   myNumber :: Int
   myNumber = 42
   ```

   Here, `myNumber` is explicitly annotated as an `Int`.

2. **Explicit Type for Functions**

   Functions can also have explicit type annotations, specifying the types of their arguments and return value:

   ```haskell
   add :: Int -> Int -> Int
   add x y = x + y
   ```

   This defines a function `add` that takes two `Int` arguments and returns an `Int`.

3. **Explicit Type in Expressions**

   Even within expressions, you can use type annotations to specify the expected type:

   ```haskell
   someInteger :: Integer
   someInteger = 12345678901234567890

   square :: Integer -> Integer
   square x = x * x

   bigNumber = square (someInteger :: Integer)
   ```

   Here, `someInteger` is explicitly typed as an `Integer` (which can hold very large numbers), and we define a function `square`. The type annotation in `square (someInteger :: Integer)` is redundant in this context but illustrates how you might specify types within expressions.

### Why Use Explicit Types?

- **Clarity**: They make the intended use of functions and variables clear, improving code readability.
- **Safety**: Explicit types can help the compiler catch type-related errors early, making your code more robust.
- **Documentation**: They serve as a form of documentation for anyone reading the code, making it easier to understand what each part of the program is supposed to do.
- **Type Inference Boundary**: In complex Haskell programs, explicitly stating types can help manage the type inference process, especially in cases where inference alone might lead to overly general or unexpected types.

While Haskell's type inference can often eliminate the need for explicit type declarations, judicious use of explicit types is considered good practice for the reasons mentioned above.
