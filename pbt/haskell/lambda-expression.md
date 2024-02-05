## Lambda Expression

The simplest lambda expression you can define in lambda calculus is the identity function. This function takes one argument and returns that argument unchanged. It is expressed as:

\[ \lambda x. x \]

Here, \( \lambda \) denotes the start of a lambda expression (indicating that what follows is a function definition), \( x \) is the parameter of the function, and the expression after the period (.) is the body of the function, which in this case is simply \( x \) itself. This means that whatever input you give to this function, it will return that input as the output without any modification. The identity function is a fundamental concept in lambda calculus, showcasing its ability to express functions abstractly.

## Bound Variable

In lambda calculus, a **bound variable** is a variable that is specified as the input (or parameter) of a lambda expression and is used within the body of that expression. It's called "bound" because its occurrence is linked, or bound, to the lambda operator \( \lambda \) that declares it, giving it a specific scope and meaning within the context of the lambda expression.

The defining characteristic of a bound variable is that its value is determined by the lambda expression's input. It does not have a value by itself outside of this context; instead, it takes on the value of whatever argument is passed to the lambda expression when the function is applied.

### Example

In the lambda expression \( \lambda x. x + 2 \), the variable \( x \) is bound. Here's why:

- \( \lambda \) introduces the function definition.
- \( x \) is declared right after \( \lambda \), making it the function's parameter.
- Within the expression \( x + 2 \), \( x \) is used to refer to any input value the function might be applied to.

In this context, \( x \) is bound because its use is directly linked to its declaration as part of the \( \lambda \) expression. It has a meaning within the function \( \lambda x. x + 2 \) (i.e., it represents the input to the function), but outside of this function, \( x \) would not have a defined value unless it is given one as part of an application of the function.

Bound variables contrast with **free variables**, which are not declared by any lambda in the expression and refer to values not provided by the lambda expression itself. In the expression \( \lambda x. x + y \), \( x \) is a bound variable (as it is declared by the lambda), while \( y \) is a free variable (assuming it is not declared elsewhere in a wider containing expression).
