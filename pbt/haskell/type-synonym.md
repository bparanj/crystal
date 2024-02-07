In Haskell, a type synonym is a feature that allows you to create a new name (alias) for an existing type. Type synonyms are used for making code more readable and understandable by giving more descriptive names to types, especially when dealing with complex types. However, it's important to note that type synonyms are purely aliases and do not create new types; they are interchangeable with the original types they refer to.

### Defining Type Synonyms

You define a type synonym using the `type` keyword followed by the new name you want to give to an existing type, an equals sign `=`, and then the existing type. The syntax looks like this:

```haskell
type NewTypeName = ExistingType
```

### Example

Consider a program that deals with users where each user is represented as a tuple of a name (String) and an age (Int). Instead of using `(String, Int)` throughout your code, you can define a type synonym to make the code more readable:

```haskell
type UserName = String
type UserAge = Int
type User = (UserName, UserAge)
```

Now, you can use the `User` type synonym in function type declarations, making your code clearer:

```haskell
getUserInfo :: User -> String
getUserInfo (name, age) = name ++ " is " ++ show age ++ " years old."
```

### Benefits of Using Type Synonyms

1. **Readability**: Type synonyms can make type signatures and declarations more readable and meaningful, especially for complex types.
2. **Ease of Maintenance**: If you need to change the underlying type, you only need to update the type synonym definition instead of updating every usage throughout the code.
3. **Documentation**: They can serve as documentation, indicating the intended use of a type or the kind of data it represents.

### Limitations

While type synonyms improve code readability, they don't enforce new type constraints or create distinct types. For example, if `UserId` and `ProductId` are both type synonyms for `Int`, the compiler won't prevent you from mistakenly using a `UserId` where a `ProductId` is expected, since they are both just `Int` underneath.

```haskell
type UserId = Int
type ProductId = Int

-- Both UserId and ProductId are interchangeable with Int, and with each other.
```

For situations where you want to enforce distinct types that are not interchangeable, Haskell offers "newtype" declarations, which create new types from existing ones with minimal runtime overhead.

In summary, type synonyms in Haskell provide a way to use more descriptive names for types, enhancing code readability and maintainability, without altering the underlying type system's behavior.

```haskell
midpoint :: (Double, Double) -> (Double, Double) -> (Double, Double)
```

can be simplified by using type synonym:

```haskell
type Point = (Double, Double)
midpoint :: Point -> Point -> Point
midpoint (x1, y1) (x2, y2) =
  ((x1+x2) / 2, (y1 + y2) / 2)
```
