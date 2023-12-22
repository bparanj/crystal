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