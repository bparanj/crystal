In lambda calculus, when we talk about how function application associates, we're basically talking about the order in which functions are applied when there's more than one function in a row. Saying that function application associates from the left means if you have a series of functions lined up, you start applying them from the left side, one after the other, moving towards the right.

Let's use a simple, non-math example to understand this. Imagine you have a line of people waiting to go through a series of funhouse doors. Each door is like a function that changes their outfit in some way. The rule that function application associates from the left is like saying, "You go through the doors from left to right, changing your outfit at each door in that order."

For example, if the first door puts on a hat, the second door gives you a pair of sunglasses, and the third door hands you a balloon, you first get the hat, then the sunglasses (over the hat), and finally, you get the balloon. You don't jump around; you go in order from the first door to the last, adding to your outfit step by step.

In the language of lambda calculus, if you have an expression like \(f g h x\), you first apply \(x\) to \(h\), then apply the result of \(h x\) to \(g\), and finally, apply the result of \(g (h x)\) to \(f\). You work your way from the left, applying each "function" (in our example, each door's outfit change) in turn, until you've gone through all the functions.

So, when we say function application associates from the left in lambda calculus, we're just describing the order in which things happen when you have a bunch of functions waiting to do their job on some input, much like going through those funhouse doors in order from left to right.
