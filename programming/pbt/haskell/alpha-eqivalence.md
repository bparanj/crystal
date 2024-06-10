Alpha equivalence in lambda calculus is a concept that indicates two expressions are considered equivalent if they differ only by the names of their bound variables. In simpler terms, it means that you can change the names of the variables within a lambda expression without changing the expression's meaning or behavior, as long as you consistently replace every instance of the variable within the scope of its binding.

### Why "Alpha"?

The term "alpha" in "alpha equivalence" comes from the Greek letter α (alpha), which is often used in mathematics and computer science to denote the first in a series, variations, or versions. In the context of lambda calculus, "alpha" refers to the operation of renaming bound variables, which is a foundational operation before any other transformations (like beta reduction) are considered. The choice of the term "alpha" emphasizes the primary and initial nature of this renaming process in the equivalence and manipulation of lambda expressions.

### Example of Alpha Equivalence

Consider the two lambda expressions:
1. \( \lambda x. x + y \)
2. \( \lambda z. z + y \)

These two expressions are alpha equivalent because the second expression can be obtained from the first by renaming the bound variable \( x \) to \( z \). The presence of \( y \) in both expressions is not affected by this renaming because \( y \) is a free variable in this context, and its name does not change the equivalence of the expressions.

Alpha equivalence highlights an important aspect of lambda calculus and functional programming languages: the specific names of bound variables do not matter; what matters is how they are used within the expressions. This concept ensures flexibility in reasoning about and transforming lambda expressions without being tied to specific variable names.
