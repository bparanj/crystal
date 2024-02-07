Algebraic Data Types (ADTs) in Haskell are a way to define complex data structures that can hold multiple types of data. ADTs are called "algebraic" because they are composed using two basic operations: product and sum.

### Product Types

A product type combines multiple values into a single composite type, similar to fields in a record or elements in a tuple. The "product" aspect comes from the fact that the total number of possible values of the product type is the product (multiplication) of the number of possible values of its components.

**Example**: Defining a point in a 2D space with `x` and `y` coordinates can be represented as a product type:

```haskell
data Point = Point Int Int
```

Here, `Point` is a product type composed of two `Int` values. If `Int` can represent \(n\) different values, then `Point` can represent \(n \times n\) different values.

### Sum Types

A sum type allows a value to be one of several different types, acting as a tagged union of types. The "sum" aspect comes from the fact that the total number of possible values of the sum type is the sum (addition) of the number of possible values of its components.

**Example**: Defining a shape that can either be a circle with a radius or a rectangle with width and height can be represented as a sum type:

```haskell
data Shape = Circle Float | Rectangle Float Float
```

Here, `Shape` is a sum type that can either be a `Circle` with one `Float` value (the radius) or a `Rectangle` with two `Float` values (the width and height).

### Combining Product and Sum Types

ADTs in Haskell can combine product and sum types to create sophisticated data structures.

**Example**: Extending the `Shape` example to include a point for the position:

```haskell
data Shape = Circle Point Float
           | Rectangle Point Float Float
```

Now, `Shape` uses both product and sum aspects: it's a sum type because a `Shape` can be either a `Circle` or a `Rectangle`, and it's a product type because each variant (`Circle` or `Rectangle`) combines multiple values (`Point` with `Float` or `Point` with two `Float`s).

### Benefits of ADTs

1. **Type Safety**: Haskell's type system ensures that ADTs are used safely. For example, you cannot mistakenly use a `Circle` as a `Rectangle`.

2. **Pattern Matching**: Haskell allows for pattern matching on ADTs, enabling elegant ways to deconstruct and operate on ADT values based on their structure.

3. **Expressiveness**: ADTs allow for the concise and precise modeling of complex data structures and domain concepts, making code more readable and maintainable.

In summary, ADTs are a foundational concept in Haskell, offering a powerful and type-safe way to model data in programs. They leverage the strengths of Haskell's type system to enable expressive, concise, and correct code.

## Comparison

In Haskell, both `newtype` and algebraic data types (ADTs) are used to define custom data types, but they serve different purposes and have different constraints and characteristics. Here's a comparison of the two:

### Algebraic Data Types (ADTs)

ADTs are used to create complex data structures that can have multiple constructors (sum types) and multiple fields (product types). They are incredibly versatile and allow for the definition of rich data models.

- **Sum Types**: ADTs can represent types that can be one of many defined variants. For example, a data type representing shapes could be a circle or a rectangle.
- **Product Types**: ADTs can also represent types that bundle several values together, like a point with `x` and `y` coordinates.
- **Pattern Matching**: ADTs are conducive to pattern matching, allowing functions to deconstruct values easily.

**Example**:
```haskell
data Shape = Circle Float | Rectangle Float Float
```

### `newtype`

`newtype` is used for creating new types from existing ones, but it's restricted to having exactly one constructor with exactly one field. It's a way to create a distinct type at the type level without introducing runtime overhead, as it is represented the same way as the underlying type at runtime.

- **Performance**: `newtype` incurs no runtime overhead compared to the type it wraps, making it as efficient as using the original type directly.
- **Type Safety**: Despite the runtime representation being the same, types defined with `newtype` are distinct from their underlying type and from each other, enhancing type safety.
- **New Typeclass Instances**: It allows for the definition of new typeclass instances for the new type, enabling different behaviors for the same underlying data structure.

**Example**:
```haskell
newtype UserID = UserID Int
```

### Comparison

- **Purpose**:
  - **ADTs** are used to model data that can be one of several shapes (sum types) or to bundle multiple pieces of data into a single entity (product types).
  - **`newtype`** is used to create a new type with the same underlying representation as an existing type for purposes of type safety, readability, or defining new typeclass instances.

- **Flexibility**:
  - **ADTs** offer more flexibility in modeling complex data structures.
  - **`newtype`** is restricted to a single constructor with a single field but allows for a different set of typeclass instances.

- **Performance**:
  - **ADTs** may introduce a slight runtime overhead due to their structure.
  - **`newtype`** has no runtime overhead, as it is represented the same as its underlying type.

- **Use Cases**:
  - Use **ADTs** when you need to model data with multiple variants or bundle various data together.
  - Use **`newtype`** when you need to distinguish between different uses of the same underlying data type without introducing runtime overhead, or when you need to define specific typeclass instances.

In summary, `newtype` and ADTs serve different needs in Haskell programming: `newtype` for creating distinct types from existing ones with added type safety and no runtime cost, and ADTs for modeling more complex data structures with multiple forms or components.

## RGB - Example

Representing an RGB color value, which consists of three components (Red, Green, Blue), each typically ranging from 0 to 255, is best suited as an algebraic data type (ADT) rather than a `newtype`. This choice is due to the need to bundle three separate values together into a single entity, which aligns with the use case for product types within ADTs.

### Using an ADT for RGB

Here's how you can define an RGB color using an ADT in Haskell:

```haskell
data RGB = RGB Int Int Int
```

This definition creates a type `RGB` with a single constructor `RGB` that takes three `Int` values as arguments, representing the red, green, and blue components of the color, respectively.

### Why Not `newtype`?

The `newtype` keyword in Haskell is intended for creating new types from existing ones but is restricted to cases where there is exactly one constructor with exactly one field. Since an RGB value inherently consists of three distinct values, `newtype` is not suitable for this purpose.

### Example Usage

Here's how you might create an RGB value and define a function to manipulate or interpret RGB values:

```haskell
-- Creating an RGB color
myColor :: RGB
myColor = RGB 255 0 150

-- Function to calculate the brightness of an RGB color
brightness :: RGB -> Int
brightness (RGB r g b) = (r + g + b) `div` 3

-- Using the function
main :: IO ()
main = print $ brightness myColor  -- Example output: 135
```

### Benefits of Using an ADT for RGB

- **Clarity**: The `RGB` type clearly models the concept of an RGB color, making the code more readable and expressive.
- **Safety**: Functions that operate on `RGB` types are type-safe, preventing mix-ups between colors and other types or between the RGB components themselves.
- **Flexibility**: You can easily extend the `RGB` type with additional constructors or fields (e.g., adding an alpha component for transparency) or define methods for color manipulation and conversion.

In conclusion, using an ADT to represent RGB values in Haskell is a natural and effective choice, offering clear, type-safe, and flexible modeling for colors in your programs.
