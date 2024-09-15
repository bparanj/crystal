## Coding Standards

Identify the coding standards that apply to Rails. In the form of a table, compare their coverage against two other  used standards.

- How are the files named?
- How are items ordered in the source file?

For example:

1. Class variables
2. Instance variables
3. Constructors
4. Methods

Discuss the advantages and disadvantages of defining and declaring code elements in a strictly prescribed order. How do modern integrated development environments affect your view?

Propose methods to identify the correct tab settings for a source code file.

### Common File Names

README - Project overview
MANIFEST - List of project files with brief explanations
INSTALL - Installation instructions
Changelog - Code change summary

## Formatting

Devise a guideline that prescribes under what circumstances the formatting of an imported piece of code should be changed to conform to the local coding standards. Take into account code quality, readability, maintenance, revision control, and future integration issues.

## Naming Conventions

What are the naming conventions?

## Process Standards

Identify the process standards that apply to Rails. Explain what software elements (files, directories) have to be examined in order to verify that a system conforms to those standards.

The Rails framework follows several process standards to ensure the quality, consistency, and maintainability of its codebase. These standards are crucial for managing such a large and widely used open-source project. Key process standards in the Rails framework include:

1. **Coding Conventions and Style Guides**:
   - Rails adheres to a specific set of coding conventions and style guides, such as naming conventions, code formatting, and best practices in Ruby programming. This includes following the Ruby Style Guide and Rails-specific best practices.

2. **Test-Driven Development (TDD)**:
   - Rails strongly advocates for TDD. Contributions to the Rails codebase  require accompanying tests to validate the functionality of the code. This approach ensures that new features or bug fixes do not introduce regressions.

3. **Code Reviews**:
   - Pull requests submitted to the Rails repository undergo thorough code reviews by core team members or experienced contributors. This process ensures that all new code adheres to Rails standards and practices.

4. **Continuous Integration (CI)**:
   - Rails uses CI tools like GitHub Actions to automatically run tests and other checks on new pull requests and commits. This helps in identifying issues early in the development cycle.

5. **Documentation Standards**:
   - Documentation is an integral part of the development process in Rails. Code changes often require corresponding updates to documentation, ensuring that API references and guides remain current.

6. **Semantic Versioning (SemVer)**:
   - Rails follows Semantic Versioning for its release process. This standard dictates how version numbers are assigned and incremented based on the nature of changes (major, minor, patch).

7. **Contributor Licensing Agreement (CLA)**:
   - Contributors may need to agree to a CLA, which clarifies the legal terms under which contributions are made.

8. **Security Protocols**:
   - Rails has established protocols for handling security vulnerabilities,  a responsible disclosure policy and a process for releasing security patches.

9. **Community Involvement and RFCs**:
   - Major changes to the framework often involve community discussions. Rails encourages the use of Request for Comments (RFCs) or similar mechanisms for proposing substantial changes.

10. **Accessibility and Internationalization Standards**:
    - Rails aims to ensure that its features are accessible and support internationalization, adhering to relevant standards in these areas.

These process standards contribute to the robustness, reliability, and community trust in the Rails framework, making it a preferred choice for web application development. They are crucial for coordinating the efforts of the many contributors who work on Rails, from all over the world.
