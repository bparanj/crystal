## Normal Form

Explain normal form in lambda calculus

In lambda calculus, an expression is said to be in **normal form** if it cannot be reduced any further using the rules of the calculus, such as beta reduction or alpha conversion. This means there are no more possible applications of functions to their arguments within the expression that could simplify it further. The normal form represents a fully simplified state where the expression has reached its simplest, irreducible form.

### Key Points about Normal Form:

- **Irreducible:** An expression in normal form cannot undergo further simplification or reduction. It's in its final, simplest state according to the rules of lambda calculus.
- **Not Guaranteed:** Not all lambda expressions can be reduced to a normal form due to the possibility of infinite loops or unresolvable expressions. This situation is often encountered with expressions that define recursive operations without a base case.
- **Unique Normal Form:** If an expression has a normal form, it is unique. This means that regardless of the order in which reductions are applied (assuming the expression can be reduced to a normal form), the final, simplified expression will be the same.

### Example

Consider the following lambda expression:

\[ (\lambda x. \lambda y. y) (\lambda z. z) \]

Applying beta reduction, we can reduce this expression as follows:

1. The outermost lambda expression \( \lambda x. \lambda y. y \) is applied to \( \lambda z. z \).
2. According to beta reduction, we replace \( x \) with \( \lambda z. z \) in the body of the outer lambda. However, since \( x \) does not appear in the body \( \lambda y. y \), the application of \( \lambda z. z \) has no effect.
3. The expression simplifies to \( \lambda y. y \), which is the identity function.

The resulting expression \( \lambda y. y \) is in normal form because there are no further reductions that can be applied. It represents a simple function that takes an argument \( y \) and returns \( y \), and there's no simpler way to express this idea in lambda calculus.

Normal form is a crucial concept in understanding the computation performed by lambda expressions, indicating when an expression has been fully evaluated or simplified.

## Beta Normal Form

Explain beta normal form in lambda calculus

In lambda calculus, **beta normal form** refers to a lambda expression that has been reduced as much as possible through **beta reduction** and cannot be reduced any further. Beta reduction is the process of applying a function to its argument(s) by substituting the argument(s) for the bound variable(s) in the function's body.

An expression is in beta normal form if:

1. There are no more applications of functions to arguments that can be performed within the expression. This means you've applied all possible function (lambda expression) reductions.
2. Essentially, the expression has been simplified to the point where it consists only of lambda abstractions (function definitions) and variables, with no further function applications left to evaluate.

### Why "Beta" in Beta Normal Form?

The term "beta" comes from the beta reduction rule in lambda calculus, which is one of the primary ways expressions are simplified or evaluated. It directly involves the application of functions to their arguments. The "normal form" part indicates that the expression has been reduced to its simplest form under the beta reduction rules.

### Example of Beta Normal Form

Consider the following lambda expression:

\[ (\lambda x. \lambda y. x + y) 3 5 \]

This expression represents a function that adds two numbers, applied to the numbers 3 and 5.

1. **First Beta Reduction:** Apply 3 to \( x \), resulting in \( \lambda y. 3 + y \).
2. **Second Beta Reduction:** Apply 5 to \( y \), resulting in \( 3 + 5 \).
3. **Simplification:** Now, we simply compute the sum, which gives us 8.

The final result, 8, cannot be reduced any further within the context of lambda calculus (as arithmetic operations like addition are not directly part of lambda calculus but assumed to be externally defined or understood). Therefore, 8 is in beta normal form for this particular expression.

### Significance

Reaching beta normal form is significant because it means the computational process represented by the lambda expression has been fully carried out, and the expression is fully simplified. However, it's important to note that not all expressions will reach a beta normal form due to the possibility of infinite loops or expressions that can't be simplified due to their structure.

## Normal vs Beta

The terms "beta normal form" and "normal form" in the context of lambda calculus are closely related but can have nuanced differences based on the specific transformations considered in reducing lambda expressions.

### Beta Normal Form

An expression is in **beta normal form** if it cannot be further reduced using **beta reduction**. Beta reduction is the process of applying a function to its arguments, substituting the input expressions for their corresponding variables in the function body. When an expression is in beta normal form, it means there are no further function applications (no \( \lambda \) applications) that can be carried out; all have been resolved.

### Normal Form

The term **normal form** without qualification generally implies that the expression cannot be reduced or simplified any further using any of the reduction rules applicable in the context. In pure lambda calculus, this  means beta reduction, as it's the primary mechanism for simplification. However, in broader discussions or more complex systems that include additional forms of reductions (like alpha conversion for renaming variables or eta conversion for function simplification), an expression being in "normal form" might imply it's fully reduced in all applicable senses.

### Are They the Same?

- In the strict context of pure lambda calculus, where beta reduction is the primary (or only) form of simplification considered, "beta normal form" and "normal form" effectively mean the same thing: the expression cannot be simplified any further by applying functions to their arguments.
- In contexts or discussions where additional types of reductions or transformations are considered (beyond just beta reduction), the term "normal form" might imply a broader criterion for simplification,  other types of reductions.

In most practical discussions regarding lambda calculus, especially at an introductory level, the distinction is subtle, and the terms can be used interchangeably. The important concept to grasp is that an expression in normal form (or beta normal form) has been simplified as much as possible under the rules being considered.
