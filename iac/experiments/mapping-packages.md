When verifying the installation of packages with tools like Goss, the discrepancy between package names used by package managers (like `apt` for Ubuntu) and the actual command or program names can indeed pose a challenge. This discrepancy arises because a package may install a program with a different name, or a single package might install multiple binaries.

To handle such cases, especially for creating verification scripts or Goss test configurations, you need a mapping between package names and the commands or programs they install. Here's how you can approach this:

### 1. **Create a Mapping**

Prepare a mapping of package names to the expected command or program names. This can be a simple dictionary if you're scripting in Python, or a direct mapping in your Goss tests.

**Example Mapping in Python:**

```python
package_to_command = {
    "git-core": "git",
    # Add more mappings as needed
}
```

### 2. **Use the Mapping for Verification**

When preparing your Goss tests or any script that verifies package installations, use the mapped command or program names instead of the package names for actual verification.

**Example for Goss:**

If you're checking for `git-core`, but the command to verify installation is `git`, your Goss test should look something like this:

```yaml
command:
  git:
    exists: true
```

### 3. **Handling Multiple Binaries**

Some packages install more than one binary. In such cases, you might want to verify the existence of all relevant binaries. Extend your mapping or verification logic accordingly.

### 4. **Example Implementation for Goss**

Given a YAML or JSON configuration that maps package names to commands, you could dynamically generate a Goss configuration file that reflects these mappings.

### 5. **Automating the Mapping**

Automatically generating this mapping can be challenging because it requires knowledge of what each package installs. However, for common packages or within the scope of a specific project, manually creating this mapping based on the packages you know you'll be installing is feasible.

### Conclusion

For tools like Goss, focusing on the commands or programs that should be available after package installation is a practical approach. This method ensures your tests validate the operational aspect of the packages—ensuring the software is not just installed but also functional as expected by the end-users or other dependent applications.
