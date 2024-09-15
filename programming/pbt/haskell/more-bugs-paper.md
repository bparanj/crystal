## Find More Bugs with QuickCheck

Random testing, while popular and effective, often repeatedly finds the same likely bugs, diminishing the benefits of extended test sessions on buggy software.

We introduce a new automated method that refines random test case generation to bypass known bugs, focusing efforts on discovering new ones.

The core issue is that bugs vary greatly in their likelihood of appearing in tests; thus, running enough tests to catch rare bugs often results in repeatedly finding common ones.

Bug slippage refers to the phenomenon where bugs are not detected during the testing phase and consequently make their way into the final release of a software product. This can happen for several reasons,  insufficient test coverage, testing environments that do not accurately replicate user environments, time constraints leading to rushed testing phases, or simply the inherent complexity of the software that makes some bugs very difficult to detect. Bug slippage can affect user satisfaction, software reliability, and the overall perception of quality, highlighting the importance of comprehensive and effective testing strategies in software development.

Test-case reduction, such as delta-debugging, often used with random testing to create simpler failing tests, can worsen the issue by turning rare bug tests into ones that trigger more common bugs, a phenomenon known as bug slippage.

Our approach is to generalize each bug as it is found, to a ‘bug pattern’, and then adapt test case generation so that test cases matching an existing bug pattern are never generated again, neither randomly nor during shrinking.

A fully automatic method to avoid provoking already known bugs at test case generation time, and to avoid bug slippage when failed tests are minimized.

Experimental results showing that this method can, in some cases, reduce the number of tests needed to find a set of bugs quite dramatically, and even find new bugs in well-studied software.

How can we avoid finding the same bug over and over again?

Our idea is to take a failing test case and automatically generalize it to a whole class of suspicious test cases, which we call a bug. We continue to test the system, but ignoring any test cases matching that bug.

More precisely, our algorithm maintains a set of bugs, which is initially empty. We test the system, ignoring any test cases matching any of the bugs. If we find a failing test case, we generalize it, add the resulting bug to the bug set, and repeat. Eventually, the bugs will cover all possible failing test cases, and we will not be able to provoke a failure.

Note that we overgeneralize failing test cases. This is because our goal is not necessarily to find all bugs in the software under test—we want to find more bugs than using random testing, but not so many that the user is overwhelmed.

The remaining problem is: how do we generalize failing test cases into bugs? In the remainder of this section we will describe our approach. It is fully automatic, though the user can tune it for better results. It is syntactic, so that we can avoid existing bugs during test case generation, which is vital if we want to make effective use of the time available for testing. We have implemented it in QuickCheck.

## Take one: subsequence checking

A very simple approach is as follows: take the failing test case, look at the names of the functions it calls and ignore their arguments. This gives us a sequence of function names S, which we take as the bug.
Given a test case, we can compute the sequence T of its function names too; the bug then matches the test case if S is a subsequence of T.

Let's illustrate this approach with a simple example involving a hypothetical software application that processes user data.

### Failing Test Case

Imagine we have a failing test case that uncovers a bug in the software. The test case executes the following sequence of function calls:

1. `login(user)`
2. `fetchData(userID)`
3. `processData(data)`
4. `logout(user)`

Ignoring the arguments, we derive the sequence of function names, **S**, representing the bug:

**S** = `login`, `fetchData`, `processData`, `logout`

### New Test Case

Now, consider we're evaluating a new test case designed to test a different aspect of the software. This test case might have the following sequence of function calls:

1. `login(user)`
2. `fetchData(userID)`
3. `updateSettings(user, settings)`
4. `processData(data)`
5. `logout(user)`

From this, we compute the sequence of function names, **T**:

**T** = `login`, `fetchData`, `updateSettings`, `processData`, `logout`

### Checking for Bug Match

To determine if the bug identified by sequence **S** matches the new test case, we check if **S** is a subsequence of **T**. In this example:

- **S** = `login`, `fetchData`, `processData`, `logout`
- **T** = `login`, `fetchData`, `updateSettings`, `processData`, `logout`

**S** is indeed a subsequence of **T** because we can find `login`, `fetchData`, `processData`, `logout` in that order within **T**, even though **T** includes an extra function call (`updateSettings`).

### Conclusion

This method simplifies bug matching by focusing on the sequence of function calls, disregarding the specifics of the arguments. It's a straightforward way to see if a new test case might encounter a previously identified bug based on the functions it uses, helping in test case analysis and prioritization.

The term "subsume" refers to the act of  or incorporating something within a larger or more comprehensive category or under a general rule. In other words, it means to absorb something into a more general set or category, making it a part of a larger whole. For example, in the context of classification, if you say that mammals subsume humans, you mean that humans are categorized under the broader class of mammals. In programming and logic, the concept can apply to how specific cases are covered or included under more general rules or classes.

We have presented MoreBugs, an extension to QuickCheck that, once a bug is discovered, avoids generating more test cases that are likely to provoke the same bug. The goals are to reduce debugging time, by presenting each bug only once, and to improve testing effectiveness by concentrating test effort on areas not yet known to be buggy

Make this as concise as possible without losing the meaning:
