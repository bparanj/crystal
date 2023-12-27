## Richard's Book Notes

1. **Context**: Start by noticing problems around you and think about what could make life easier for others. This way, you can help your community.
2. **Opportunity**: When you find a problem, try to understand why it happens and think of many ways to solve it. Keep the ideas flowing without judging them too soon.
3. **Implementation**: Choose a solution that fits the problem's size. For example, a simple phone call might be enough to fix a small issue like a pothole.
4. **Loop**: If your solution doesn't work, don't give up. Go back, understand why it failed, find new ways to approach the problem, and try again. Adjust your focus as needed, whether it's looking closely at details or taking a broader view.

- Spend time on taking actions that will build your context of a project. You will be able to identify contribution opportunities.
- Work on a task even if someone else has claimed it.
- Focus on actions you can take today. It does not have to be perfect. Take small steps.
- Rejected contribution should be used as learning opportunities.
- Contribute without getting attached to the outcome.

## Find Opportunity to Contribute

- Seek out contributions opportunities deliberately.

### Step 1

Find problems through observation. Learn about a project and how people use it to accomplish their goals.

### Step 2

Brainstrom ways to solve the problem. Pick the most likely option to be merged.

### Step 3

Implement. Write the code, file the issue or make the change.

Identify any obstacles to resolving the problem. Repeat these steps until the problem is fixed. Focus on the code or the problem as needed. Read the code that is relevant to the problem. Build the context. Identify possible change locations for implementing the fix. Write a draft pull request.

Implement quickly and ask for feedback. Iterate and learn. If the PR is not accepted, create a library. Reflect on why the first contribution did not work, identify new ways to solve the problem. Implement.

## The Right Perspective

- View problems with libraries as opportunities to contribute.
- Take notes while working. Jot down painful things.
- Review the notes to see what could be improved.

## Project Familiarity

- Why are some pull requests accepted and others not? 
- How do maintainers like to do work? 
- How can you help effectively? 

Read the Contributing, Readme, Issues, Code of conduct, Governance. For Rails RUNNING_UNIT_TESTS.doc.

For Rails open source contribution:

- What versions are supported?
- What are the style guidelines and where to find it?
- Where does discussion happen?

The Ruby on Rails project maintains specific style guidelines to ensure consistency and quality in its codebase. These guidelines cover various aspects such as code formatting, naming conventions, and best practices for writing clear and maintainable code.

To find the Ruby on Rails style guidelines, you can visit the official Rails GitHub repository. In the repository, look for a CONTRIBUTING.md file or similar documentation, which often includes contribution guidelines and coding standards. Additionally, the Rails community might adhere to broader Ruby style guides, like the Ruby Style Guide by Bozhidar Batsov, which can also be found on GitHub.

- What types of word choices do maintainers choose when they talk to contributors?
- Do maintainers frequently ask similar questions?
- What preferences towards the contributions do maintainers hold?
- Are there some informal rules that are driving standard communication?

When Rails maintainers communicate with contributors, their word choices tend to be:

1. **Encouraging**: They often use positive and encouraging language to foster a welcoming environment for contributors.
2. **Constructive**: Feedback on contributions is usually constructive, focusing on how to improve the contribution rather than just pointing out flaws.
3. **Clear and Direct**: Maintainers typically use clear and direct language to ensure that their instructions or feedback are easily understood.
4. **Respectful and Polite**: Professionalism and respect are key, especially in open source communities, to maintain a healthy collaborative environment.
5. **Inclusive**: Language that promotes inclusivity and diversity is often preferred to ensure all contributors feel valued.

These communication styles help in building a positive and productive open-source community.

Discussions in the Ruby on Rails community typically happen in several key places:

1. **GitHub**: The Rails GitHub repository is a primary platform for discussion, especially regarding bug reports, feature requests, and pull requests.
2. **Rails Forums**: The official Rails forums are a place for broader discussions about the framework.
3. **Mailing Lists**: Rails has mailing lists for various topics, including core development and usage questions.
4. **Stack Overflow**: Many Rails developers use Stack Overflow for asking and answering questions.
5. **IRC Channels and Slack**: Real-time discussions often occur on IRC channels and in the Rails Slack community.

These platforms facilitate conversations ranging from development queries to contributing to the Rails codebase. 

## Acceptance

- Is the change small?
- Is the change provably correct? (Fixing a regression, updating contradictory docs)
- Is the change similar to something previously merged? (Housekeeping)
- Is there public and visible support for a change?
- Are you avoiding additional unnecessary changes? (Say no to mixing features and refactoring)

## Common Tasks

- Is the test suite passing?
- Do dependency versions need to be updated?
- Are there flappy tests that need to be hardened?
- Is the test suite free of deprecation outputs?
- Are the primary interfaces documented with examples?
- Are the primary code paths tested?
- Are linters or other auxiliary tools running without warning?

- Fix sporadic and unpredictable test failures.
- Add new language runtime versions. Check for missing version in CI config and add it.
- Fix tests that pass only on rerun.
- Add documentation for primary interfaces.
- Use code coverage tools (rcov, simplecov) to add missing tests.

To clean up deprecations in a Rails codebase:

1. **Identify Deprecations**: Check logs for deprecation warnings while running your application or tests. Rails typically logs a warning when deprecated features are used.

2. **Understand the Changes**: Refer to the Rails release notes or documentation to understand the recommended replacements for deprecated features.

3. **Update Your Code**: Replace deprecated methods, classes, or configurations with their updated counterparts as per the Rails guidelines.

4. **Run Tests**: After making changes, run your test suite to ensure that your updates haven’t broken existing functionality.

5. **Seek Community Guidance**: If you're unsure about how to update certain deprecations, consult the Rails community through forums, Stack Overflow, or mailing lists for advice.

6. **Repeat**: As Rails continues to evolve, keep an eye on new deprecations in future releases and repeat the process.

## Making Changes

- Make the change and link to a similar change.
- Avoid mixing feature and refactoring.

- What do projects and maintainers want? 
- What problems do they have that keep them up at night? 
- What do they hate doing? 
- What would they love to see in their codebase? 

Rails maintainers, like those of many open-source projects, might frequently ask similar questions, but these are usually related to specific issues or contributions. Common questions could be about the rationale behind a code change, requests for clarification, or suggestions for improvements. They often seek to understand the context and impact of contributions to ensure they align with the project's goals and standards. This process helps maintain the quality and consistency of the Rails codebase.

Patterns in merged PRs for Rails core often include:

1. **Quality Code**: Adherence to coding standards and high-quality code are key.
2. **Well-Tested**: PRs usually include thorough tests for new features or bug fixes.
3. **Documentation**: Good PRs often update or add necessary documentation.
4. **Community Agreement**: Changes typically align with the broader Rails community's needs and opinions.
5. **Issue Relevance**: PRs often address open issues or widely acknowledged enhancements.
6. **Maintainer Approval**: Core team reviews and agrees with the changes.

Successful PRs in such projects usually follow these patterns, demonstrating attention to detail and community standards.

## Open Issues

New issues are less than a month. Old issues are over a month. 

### New Issue with No Comments

- Read it and any insightful comments

### Old Issue with No Comments

- Is it describing a challengine problem?
- Is it clear?

### Old Issue with Comments

- Why is the issue stalled?
- Is it because a decision could not be made?
- Did someone stop responding?
- It was fixed but is not closed?

Ask if it can be closed.

## Categorize Issues

- Does it have sufficient details?
- Do you need more details?
- Do you need to separate critical from non-critical components?

Take notes on key details.

## Issue Types

### Bugs

- Regressions
- Unexpected behavior

### Feature Requests

- Modification
- Addition

## Reproducing Bugs

1. Missing expected vs actual result

Explain to the poster the importance of reproducing an issue and that the behavior they are describing is unclear.

2. No code provided
3. No instructions provided

Comment back on the issue that you appreciate the report, but you have no way to see the behavior for yourself, and that you need a reproduction.

Useful instructions: https://www.codetriage.com/example_app

4. Missing steps in the test case to reproduce the bug

Reproducing steps must be in code form. 

5. Provides link to a repository for reproducing the bug

Time box to 5 to 10 minutes to reproduce the bug. Comment on the issue with steps to reproduce the problem. If the bug was not reproduced, share the steps and ask if any steps is missing.

6. Provides link to a repo with instructions on reproducting the bug
7. Provides link to a repo with instructions on using containerization tool

Report back whether you were able to reproduce the issue.

## Checklist for Reproduction Steps

- Software versions are the same.
- OS version
- Everything is checked into git (did not forget the files in .gitignore)
- Ask them to run their reproducing in a new, fresh directory
- Get the reporter to fail in the same way as it is on your machine

If it passes for one person and fails for another, look for the differences in the environment to narrow down the cause.

## Debugging

### Confirm

Confirm it is still broken. See if the main branch has the problem. Run the test case against the latest commit and see if it still a problem.

If it is fixed, comment on the issue. It can be closed.

### Link 

If you notice similar issues, link them to the related issues.

- There is extra context for anyone who ultimately ends up working on the issue.
- Developers across different issues can share information such as debugging steps.
- Anyone who lands on one of the bugs via a search will have access to the whole conversation.
- Duplicate issues can be closed so that developers can focus effort in one location.
- Once a fix has been committed and confirmed, it is easy to go through and close all related issues.

Search existing issues with a few keywords. Searching for related issues should be the first step for anyone submitting an issue.

### Isolate Failing Behavior

- When did it start failing?

Use bisect to find failing commit that introduced the bug.

### Report your Findings

Explain the commit that caused the issue. Find the PR related to that commit. Read the PR and commit message. 

- Why was the change made? 
- Are there any tests modified or added? 
- What was the intent of the change?

Read any linked PRs.







