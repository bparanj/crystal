
## Patching

1. Looking at what software you have in place
2. Researching what vulnerabilities have been discovered in that software
3. Upgrading the vulnerable software to secure versions
4. Testing to make sure that the new versions work

## Tools

- Metasploit

## Library Inventory

Start by taking an inventory of the third-party dependencies in the software your organization builds.

## Library Dependencies

1. Find the supported versions of your code using source control.
2. Find the direct library dependencies your code has.
3. Find the transitive library dependencies your code has - that is, find the dependencies of your dependencies.

Get a full list of all of the applications developed by your company.

1. Find all the codebases.
2. For each codebase, manually put together a list of the direct and transitive dependencies.
3. Find another codebase you overlooked and manually put together a list of its direct and transitive dependencies. Now you’ve found all the codebases.
4. Write a script to automate dependency detection.
5. Find another codebase that no one told you about.
6. Take the automated script and integrate it into each project’s continuous integration system.
7. Find another codebase. No, really. This is all of them this time.
8. Document the script and train the build team in its use.
9. The next time a project is started, have the build team add the dependency-finding script to the build process.
10. Find one more codebase.


## Question 1

How to find the supported versions of Rails project using source control?

To find the supported versions of a Rails project using source control, you can follow these steps:

1. Clone the Rails project repository:
   ```
   git clone <repository_url>
   ```

2. Navigate to the project directory:
   ```
   cd <project_directory>
   ```

3. Check the project's Gemfile:
   Open the `Gemfile` in a text editor and look for the `gem 'rails'` line. It should specify the version or version constraint of Rails used in the project. For example:
   ```ruby
   gem 'rails', '~> 6.1.0'
   ```
   This indicates that the project supports Rails versions greater than or equal to 6.1.0 but less than 6.2.0.

4. Check the project's `.ruby-version` file (if present):
   Some projects use a `.ruby-version` file to specify the Ruby version they are compatible with. Open the file and check the Ruby version mentioned. For example:
   ```
   2.7.2
   ```
   This indicates that the project is compatible with Ruby version 2.7.2.

5. Check the project's `Gemfile.lock`:
   The `Gemfile.lock` file contains the exact versions of all the gems used in the project, including Rails. Open the `Gemfile.lock` file and look for the `rails` gem entry. It will specify the exact version of Rails used in the project. For example:
   ```
   rails (6.1.3)
   ```
   This indicates that the project is currently using Rails version 6.1.3.

6. Check the project's documentation or README:
   Many projects include information about the supported Rails versions in their documentation or README file. Look for any mentions of Rails versions or compatibility requirements in these files.

7. Check the project's continuous integration (CI) configuration:
   If the project uses a CI system, such as Travis CI or CircleCI, check the configuration file (e.g., `.travis.yml` or `.circleci/config.yml`) to see which Rails versions are being tested against. This can give you an idea of the supported versions.

By following these steps, you should be able to determine the supported Rails versions for a given project using its source control repository. Keep in mind that the supported versions may change over time as the project evolves, so it's always a good idea to refer to the project's documentation and release notes for the most up-to-date information.

To find the supported versions of a Rails project using source control, you can follow these steps:

### 1. Check the `Gemfile` and `Gemfile.lock`
The `Gemfile` specifies the dependencies for the project, including the version of Rails. The `Gemfile.lock` provides the exact versions of all dependencies installed.

1. Open the `Gemfile` and look for the line specifying the Rails version:
   ```ruby
   gem 'rails', '5.2.3' # Example version
   ```

2. The `Gemfile.lock` will show the specific version installed:
   ```ruby
   rails (5.2.3)
   ```

### 2. Check Version Control Tags
Tags in version control systems (like Git) can indicate releases and supported versions.

1. List all tags to see if there are any tags that indicate version numbers:
   ```bash
   git tag
   ```

2. If the tags follow a naming convention like `vX.Y.Z` (e.g., `v5.2.3`), they can help you identify supported versions.

### 3. Check Branches
Sometimes different branches are maintained for different versions.

1. List all branches:
   ```bash
   git branch -a
   ```

2. Look for branches that indicate versions, such as `stable-5-2`, `release-6-0`, etc.

### 4. Check Versioning Files or Documentation
Some projects maintain a `VERSION` file or documentation that lists supported versions.

1. Look for a `VERSION` file in the root directory of the project.
2. Check the `README.md` or any `docs/` directory for information about supported versions.

### 5. Check Changelog
The `CHANGELOG.md` file often lists changes by version and can help identify supported versions.

1. Open the `CHANGELOG.md` file and look for version entries:
   ```markdown
   ## [5.2.3] - 2020-01-01
   - Some changes
   ```

### Example
Here is an example of how you might find the Rails version specified in a `Gemfile`:

```ruby
source 'https://rubygems.org'

gem 'rails', '~> 6.0.3'
```

The `Gemfile.lock` might look like this:

```
GEM
  specs:
    rails (6.0.3.4)
      actioncable (= 6.0.3.4)
      actionmailbox (= 6.0.3.4)
      actionmailer (= 6.0.3.4)
      actionpack (= 6.0.3.4)
      actiontext (= 6.0.3.4)
      actionview (= 6.0.3.4)
      activejob (= 6.0.3.4)
      activemodel (= 6.0.3.4)
      activerecord (= 6.0.3.4)
      activestorage (= 6.0.3.4)
      activesupport (= 6.0.3.4)
      bundler (>= 1.3.0)
      railties (= 6.0.3.4)
      sprockets-rails (>= 2.0.0)
```

### Summary
- **Check `Gemfile` and `Gemfile.lock`** for the Rails version.
- **Use `git tag`** to find version tags.
- **Use `git branch -a`** to find branches for different versions.
- **Look for a `VERSION` file or documentation** that lists supported versions.
- **Check the `CHANGELOG.md`** for version entries.

These steps will help you identify the supported versions of a Rails project using source control.

## Question 2

How to find the direct library dependencies of a Rails project?

To find the direct library dependencies of a Rails project, you can use the following methods:

1. Check the project's Gemfile:
   The `Gemfile` is a file in the root directory of a Rails project that lists all the gem dependencies required by the project. Open the `Gemfile` in a text editor and look for the `gem` lines. Each `gem` line specifies a library dependency. For example:
   ```ruby
   gem 'rails', '~> 6.1.0'
   gem 'sqlite3'
   gem 'puma'
   gem 'sass-rails'
   ```
   These lines indicate that the project directly depends on the `rails`, `sqlite3`, `puma`, and `sass-rails` gems.

2. Run `bundle list` command:
   Open a terminal, navigate to the project's root directory, and run the following command:
   ```
   bundle list
   ```
   This command will display a list of all the gems that are directly required by the project, along with their versions. The output will look something like this:
   ```
   Gems included by the bundle:
     * actioncable (6.1.3)
     * actionmailbox (6.1.3)
     * actionmailer (6.1.3)
     * actionpack (6.1.3)
     * actiontext (6.1.3)
     * actionview (6.1.3)
     * activejob (6.1.3)
     * activemodel (6.1.3)
     * activerecord (6.1.3)
     * activestorage (6.1.3)
     * activesupport (6.1.3)
     * bundler (2.2.15)
     * puma (5.2.2)
     * rails (6.1.3)
     * sass-rails (6.0.0)
     * sqlite3 (1.4.2)
     * ...
   ```

3. Use `bundle show` command:
   Another way to find the direct dependencies is by using the `bundle show` command followed by the name of a specific gem. For example:
   ```
   bundle show rails
   ```
   This command will display the path and version of the `rails` gem that is directly required by the project.

4. Check the project's documentation or README:
   Some projects may list their direct dependencies or provide instructions on how to set up the project's dependencies in their documentation or README file. Look for any mentions of required gems or installation instructions.

By using these methods, you can identify the direct library dependencies of a Rails project. Keep in mind that these dependencies may have their own dependencies (transitive dependencies), which are automatically resolved by the bundler when running `bundle install`.

It's also worth noting that the `Gemfile.lock` file in the project's root directory contains the exact versions of all the gems (direct and transitive) used in the project. You can open this file to see a complete list of all the gems and their versions that are currently being used by the project.

To find the direct library dependencies of a Rails project, you typically look at the `Gemfile` and the `Gemfile.lock` files. The `Gemfile` lists the libraries (gems) that the project directly depends on, while the `Gemfile.lock` provides a snapshot of all dependencies, including transitive ones. Here’s how to identify the direct dependencies:

### Step-by-Step Guide

#### 1. Review the `Gemfile`
The `Gemfile` lists all the gems that the Rails project directly depends on. Each `gem` line specifies a direct dependency.

Example `Gemfile`:
```ruby
source 'https://rubygems.org'

gem 'rails', '~> 6.0.3'
gem 'pg', '>= 0.18', '< 2.0'
gem 'puma', '~> 4.1'
gem 'sass-rails', '>= 6'
gem 'webpacker', '~> 4.0'
gem 'turbolinks', '~> 5'
gem 'jbuilder', '~> 2.7'
```

Each `gem` line is a direct dependency. In this example, the direct dependencies are:
- rails
- pg
- puma
- sass-rails
- webpacker
- turbolinks
- jbuilder

#### 2. Check the `Gemfile.lock` for Confirmation
The `Gemfile.lock` file lists all dependencies, including direct and transitive dependencies. To verify direct dependencies, you can look at the top of the `Gemfile.lock`, under the `DEPENDENCIES` section.

Example `Gemfile.lock` (partial):
```
GEM
  remote: https://rubygems.org/
  specs:
    actioncable (6.0.3.4)
    actionmailbox (6.0.3.4)
    ...

DEPENDENCIES
  jbuilder (~> 2.7)
  pg (>= 0.18, < 2.0)
  puma (~> 4.1)
  rails (~> 6.0.3)
  sass-rails (>= 6)
  turbolinks (~> 5)
  webpacker (~> 4.0)
```

The `DEPENDENCIES` section confirms the direct dependencies listed in the `Gemfile`.

### Tools to Automate Dependency Analysis

#### 1. Bundler
You can use Bundler to list the direct dependencies:

```bash
bundle list
```

While this command lists all gems, focusing on the `Gemfile` entries provides direct dependencies.

#### 2. Gemnasium or Similar Services
Tools like [Gemnasium](https://gemnasium.com) or other dependency management services can analyze your `Gemfile` and `Gemfile.lock` and provide a detailed report of direct and indirect dependencies.

### Summary
- **Check the `Gemfile`**: Lists all direct dependencies explicitly.
- **Verify with `Gemfile.lock`**: Look under the `DEPENDENCIES` section to confirm direct dependencies.
- **Use Tools**: Use Bundler or other dependency management tools for more detailed analysis.

By following these steps, you can identify the direct library dependencies of a Rails project accurately.

## Followup Question 1

How to Use Bundler for more detailed analysis?

Bundler is a powerful tool for managing dependencies in Ruby projects, including Rails applications. It provides several commands and features that allow you to perform more detailed analysis of your project's dependencies. Here are some ways to use Bundler for detailed dependency analysis:

1. `bundle outdated` command:
   Running the `bundle outdated` command will show you a list of gems that have newer versions available than the ones currently specified in your `Gemfile.lock`. This helps you identify gems that may need updating. The output will include the gem name, current version, latest version, and the source of the update. For example:
   ```
   $ bundle outdated
   Fetching gem metadata from https://rubygems.org/..........
   Fetching gem metadata from https://rubygems.org/.
   Resolving dependencies...

   Outdated gems included in the bundle:
     * nokogiri (newest 1.11.3, installed 1.11.2) in group "default"
     * rails (newest 6.1.3.2, installed 6.1.3) in group "default"
   ```

2. `bundle viz` command:
   The `bundle viz` command generates a visual dependency graph of your project's gems. It creates an image file that shows the relationships between gems, including their dependencies. To use this command, you need to have the `graphviz` library installed on your system. Run the following command to generate the dependency graph:
   ```
   $ bundle viz
   ```
   This will create a file named `gem_graph.png` in the current directory, representing the dependency graph.

3. `bundle info` command:
   The `bundle info` command provides detailed information about a specific gem. You can use it to view the gem's version, source, dependencies, and more. For example:
   ```
   $ bundle info rails
   * rails (6.1.3)
       Summary: Full-stack web application framework.
       Homepage: https://rubyonrails.org
       Path: /path/to/gems/rails-6.1.3
       Git: https://github.com/rails/rails.git
       Gem: https://rubygems.org/gems/rails-6.1.3.gem
   ```

4. `bundle show` command with dependencies:
   You can use the `bundle show` command with the `--paths` flag to display the paths of all the gems in your bundle, including their dependencies. This gives you a complete list of all the gems used in your project. Run the following command:
   ```
   $ bundle show --paths
   ```
   The output will include the gem names and their corresponding paths.

5. Analyzing the `Gemfile.lock`:
   The `Gemfile.lock` file contains detailed information about the exact versions of all the gems used in your project, including their dependencies. You can open this file and examine its contents to understand the complete dependency tree. The file lists the gems, their versions, and the dependencies they require.

6. Using third-party tools:
   There are several third-party tools and plugins available that provide additional dependency analysis capabilities for Bundler. Some popular ones include:
   - `bundler-audit`: Checks for known security vulnerabilities in your project's gem dependencies.
   - `fasterer`: Suggests faster alternatives to some commonly used Ruby idioms.
   - `ruby-lint`: Performs static code analysis and identifies potential issues in your Ruby code.

By leveraging these Bundler features and tools, you can gain a deeper understanding of your project's dependencies, identify potential issues, and make informed decisions about updating or optimizing your gem dependencies.

Bundler provides several commands and options to help you analyze your project's dependencies in detail. Here are some useful commands and techniques:

### 1. List All Gems
To list all gems that are part of your project, including their versions and sources, you can use:
```bash
bundle list
```
This command will show all the gems installed for the project, both direct and transitive dependencies.

### 2. Show Details of a Specific Gem
To see detailed information about a specific gem, including its dependencies and installed versions, you can use:
```bash
bundle show <gem_name>
```
For example:
```bash
bundle show rails
```

### 3. Analyze Dependency Graph
To visualize and analyze the dependency graph, you can use:
```bash
bundle viz
```
This command generates a visual representation of the gem dependency graph. You can specify the output format as a PNG or PDF file:
```bash
bundle viz --format=png
```
Or:
```bash
bundle viz --format=pdf
```

### 4. Check for Outdated Gems
To check which gems are outdated and can be updated, you can use:
```bash
bundle outdated
```
This command will list all the gems that have newer versions available.

### 5. Detailed Information about Installed Gems
To get detailed information about all installed gems, you can use:
```bash
bundle info
```
This command provides a summary of all gems, including their versions and dependencies.

### 6. Using `Bundler::LockfileParser`
For a more programmatic approach, you can use the `Bundler::LockfileParser` class to parse the `Gemfile.lock` file and extract detailed information about dependencies.

Example script:
```ruby
require 'bundler'

lockfile_contents = Bundler.read_file('Gemfile.lock')
lockfile = Bundler::LockfileParser.new(lockfile_contents)

puts "Gems:"
lockfile.specs.each do |spec|
  puts "#{spec.name} (#{spec.version})"
end

puts "\nDependencies:"
lockfile.dependencies.each do |name, dependency|
  puts "#{name} depends on #{dependency.requirement}"
end
```

### 7. Exploring `Gemfile` and `Gemfile.lock` Manually
The `Gemfile` specifies direct dependencies, and the `Gemfile.lock` contains a more detailed snapshot, including both direct and transitive dependencies.

#### `Gemfile` Example:
```ruby
source 'https://rubygems.org'

gem 'rails', '~> 6.0.3'
gem 'pg', '>= 0.18', '< 2.0'
gem 'puma', '~> 4.1'
gem 'sass-rails', '>= 6'
gem 'webpacker', '~> 4.0'
gem 'turbolinks', '~> 5'
gem 'jbuilder', '~> 2.7'
```

#### `Gemfile.lock` Example (Partial):
```
GEM
  remote: https://rubygems.org/
  specs:
    actioncable (6.0.3.4)
    actionmailbox (6.0.3.4)
    actionmailer (6.0.3.4)
    ...

DEPENDENCIES
  jbuilder (~> 2.7)
  pg (>= 0.18, < 2.0)
  puma (~> 4.1)
  rails (~> 6.0.3)
  sass-rails (>= 6)
  turbolinks (~> 5)
  webpacker (~> 4.0)
```

### Summary
- **Use `bundle list`**: To list all installed gems.
- **Use `bundle show <gem_name>`**: To get details about a specific gem.
- **Use `bundle viz`**: To visualize the dependency graph.
- **Use `bundle outdated`**: To check for outdated gems.
- **Use `bundle info`**: To get detailed information about installed gems.
- **Use `Bundler::LockfileParser`**: For programmatic analysis of `Gemfile.lock`.

These commands and techniques will help you perform a detailed analysis of your Rails project's dependencies using Bundler.

## Question 3

How to find the transitive library dependencies in a Rails project?

To find the transitive library dependencies in a Rails project, you can use Bundler's built-in functionality. Transitive dependencies are the dependencies of your project's direct dependencies. Here are a few methods to identify transitive dependencies:

1. Using `bundle show` command:
   Run the following command in your Rails project's root directory:
   ```
   $ bundle show
   ```
   This command will display a list of all the gems used in your project, including both direct and transitive dependencies. Each gem will be listed along with its version and the path where it is installed.

2. Using `bundle list` command:
   Run the following command in your Rails project's root directory:
   ```
   $ bundle list
   ```
   This command will display a list of all the gems used in your project, including transitive dependencies. However, unlike `bundle show`, it does not provide the installation path for each gem.

3. Examining the `Gemfile.lock`:
   The `Gemfile.lock` file in your Rails project contains detailed information about all the gems and their dependencies. Open the `Gemfile.lock` file and examine its contents. You will see a list of all the gems, including transitive dependencies, along with their exact versions.

   Each gem in the `Gemfile.lock` is listed under a specific group (e.g., `default`, `development`, `test`). The gems listed under each group include both direct and transitive dependencies.

   For example, if you have a gem named `devise` as a direct dependency, you will see it listed in the `Gemfile.lock`. Below `devise`, you will find its transitive dependencies, such as `bcrypt`, `orm_adapter`, etc.

4. Using `bundle viz` command:
   The `bundle viz` command generates a visual dependency graph of your project's gems. It shows the relationships between gems, including transitive dependencies. To use this command, you need to have the `graphviz` library installed on your system.

   Run the following command in your Rails project's root directory:
   ```
   $ bundle viz
   ```
   This command will create a file named `gem_graph.png` in the current directory, representing the dependency graph. You can open this file to visualize the dependencies and their relationships.

5. Using third-party tools:
   There are several third-party tools available that can help you analyze your project's dependencies, including transitive dependencies. Some popular tools include:
   - `bundler-stats`: Provides a web-based interface to visualize and analyze your project's gem dependencies.
   - `deppractice`: A command-line tool that identifies unused and outdated dependencies in your project.

   These tools can give you additional insights into your project's dependency tree and help you identify transitive dependencies.

By using these methods, you can effectively identify the transitive library dependencies in your Rails project. Understanding the complete dependency tree is important for managing your project's dependencies, identifying potential conflicts, and keeping your project up to date with the latest gem versions.

To find the transitive library dependencies in a Rails project, you primarily use the `Gemfile.lock` file. The `Gemfile.lock` file provides a detailed snapshot of all the gems installed, including both direct and transitive dependencies. Here are the steps to identify these dependencies:

### 1. Inspect the `Gemfile.lock` File

The `Gemfile.lock` file is generated by Bundler and lists all the gems in your project along with their dependencies.

#### Example `Gemfile.lock` Structure:

```
GEM
  remote: https://rubygems.org/
  specs:
    actioncable (6.0.3.4)
      actionpack (= 6.0.3.4)
      nio4r (~> 2.0)
      websocket-driver (>= 0.6.1)
    actionmailbox (6.0.3.4)
      actionpack (= 6.0.3.4)
      activejob (= 6.0.3.4)
      activerecord (= 6.0.3.4)
    ...

DEPENDENCIES
  jbuilder (~> 2.7)
  pg (>= 0.18, < 2.0)
  puma (~> 4.1)
  rails (~> 6.0.3)
  sass-rails (>= 6)
  turbolinks (~> 5)
  webpacker (~> 4.0)

BUNDLED WITH
   2.1.4
```

### 2. Identify Direct Dependencies

Direct dependencies are listed under the `DEPENDENCIES` section. For example:
```
DEPENDENCIES
  jbuilder (~> 2.7)
  pg (>= 0.18, < 2.0)
  puma (~> 4.1)
  rails (~> 6.0.3)
  sass-rails (>= 6)
  turbolinks (~> 5)
  webpacker (~> 4.0)
```

### 3. Find Transitive Dependencies

Transitive dependencies are listed under the `specs` section, indented under their respective parent gems. For example:
```
GEM
  remote: https://rubygems.org/
  specs:
    actioncable (6.0.3.4)
      actionpack (= 6.0.3.4)   # Transitive dependency
      nio4r (~> 2.0)           # Transitive dependency
      websocket-driver (>= 0.6.1)  # Transitive dependency
    ...
```

### 4. Use Bundler Commands

Bundler provides commands to help you understand the dependency tree.

#### `bundle list`

This command lists all the gems in your project, both direct and transitive.
```bash
bundle list
```

#### `bundle show <gem_name>`

This command shows detailed information about a specific gem, including its dependencies.
```bash
bundle show rails
```

#### `bundle viz`

This command generates a visual representation of the dependency graph. You need Graphviz installed for this command.
```bash
bundle viz --format=png
```

### 5. Using `Bundler::LockfileParser`

For a more programmatic approach, you can use the `Bundler::LockfileParser` class in a Ruby script to parse the `Gemfile.lock` file and extract information about dependencies.

#### Example Ruby Script:
```ruby
require 'bundler'

lockfile_contents = Bundler.read_file('Gemfile.lock')
lockfile = Bundler::LockfileParser.new(lockfile_contents)

puts "Direct Dependencies:"
lockfile.dependencies.each do |name, dependency|
  puts "#{name} (#{dependency.requirement})"
end

puts "\nAll Dependencies:"
lockfile.specs.each do |spec|
  puts "#{spec.name} (#{spec.version})"
  spec.dependencies.each do |dep|
    puts "  depends on #{dep.name} (#{dep.requirement})"
  end
end
```

### Summary

- **Inspect `Gemfile.lock`**: Manually check the `GEM` and `DEPENDENCIES` sections.
- **Use Bundler Commands**: Use `bundle list`, `bundle show <gem_name>`, and `bundle viz` for detailed analysis.
- **Programmatic Analysis**: Use `Bundler::LockfileParser` to parse the `Gemfile.lock` file and extract dependencies.

These methods will help you identify both direct and transitive dependencies in your Rails project.
