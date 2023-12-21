## Needed Git Skills

- Squashing and rebasing commits
- Keep your fork updated (fetching upstream)
- Resolving merge conflicts
- Git Bisect : https://m.youtube.com/watch?v=7zoD6NZy6vY&t=3596s

## Running Tests

```
bundle install
bundle exec rake test
```

ActionPack Module

```
cd actionpack
bundle exec rake test
```

Run tests for specific Ruby test file:

```
cd actionpack
bundle exec ruby -I test/test/abastract/translation_test.rb
```

Run tests for a specific database adapter:

```
cd activerecord
bundle exec rake test:mysql2
```

Running one specific test file for MySQL adapter:

```
bundle exec rake test:mysql2 TEST=test/cases/connection_adapters/connection_handler_test.rb
```

Running a single test case from a test file using the MySQL adapter:

bundle exec rake test:mysql2 TEST=test/cases/database_configurations_test.rb TESTOPTS="'-n /test_name_goes_here"

You can test only the functionality you are working on currently.

## Git Conventions

- How to name a branch
- How to write a commit message
- How to describe a PR

Look at the past PRs to answer these questions.

- How to report bugs?
- How do they ask for help?

Notice how they communicate and give feedback.

- Provide context
- Write in a descriptive way
- Ask good questions

## Contributing

- Good first issues: https://github.com/rails/rails/labels/good%20first%20issue
- Reproducible Bugs: https://github.com/rails/rails/issues?q=is:issue+is:open+label:%22With+reproduction+steps%22

- Follow the steps
- Reproduce the error
- Add a failing test
- Fix the error
- Make the test pass

[Issue reproduction script](https://github.com/rails/rails/issues/42716)
Run the script: ruby reproduce.rb

Finding issues with reproduction steps:

- Go to https://github.com/rails/rails/issues
- Filter out any issues labeled as stale
- Skip the issues that already have an open Pull Request
- Choose the ones that have the label with reproduction steps
- Bookmark at least 3 issues that look promising to you
- Set a 10 minutes timer
- Go over these 3 issues, read the description and discussion, and choose just one
- Set a 30 minutes timer and try to reproduce the issue

Answer the following questions:

- What did you find?
- What questions do you have about the issue?
- Do you have a solution to propose?

Share them in the comments.

- [Verify if an issue is valid by reproducing it.](https://github.com/rails/rails/issues/42727)

- Add reproduction steps to issues that don't have it yet.

- [Update and maintain the documentation](https://github.com/rails/rails/pull/42055)

- [Check out related projects](http://www.github.com/rails)

## Tips

- [Pry debug guide](https://www.hexdevs.com/posts/pry-debug-in-5-minutes/)
- [Implicit to Explicit](https://www.shakacode.com/blog/railsconf-2021-implicit-to-explicit-decoding-rubys-magical-syntax/)
- Test all important scenarios
- Check Github Actions that run when a PR is opened.
- Review PRs and comment, question or add a suggestion

Learn how to:

- read other people’s code
- read documentation
- write good documentation, commits, and Pull Requests
- navigate a large codebase
- ask for feedback and submit code reviews
- improve your communication skills
- understand how Rails features work
- Learn OOP/design patterns: why, when, and where to use them
- How to test an app's configuration, etc.

- [OS Contribution](https://www.hexdevs.com/posts/ruby-on-rails-open-source-contribution/)
- [Subscribe to YouTube channel](https://www.youtube.com/c/hexdevs/)

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


