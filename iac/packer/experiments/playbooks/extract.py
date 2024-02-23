import yaml

package_map = {
    "git-core": "git"
    # Add more mappings if needed for other packages in packages.yml file
}

# Open and read the playbook file
with open("./packages.yml", "r") as f:
    data = yaml.safe_load(f)

# Find the task that installs packages using apt
for play in data:
    for task in play['tasks']:
        if task['name'] == 'Install development tools and libraries':
            packages = task['ansible.builtin.apt']['name']  # Access packages here
            break  # Can break out of the loop since you found the packages

# Write mapped packages to the file
with open("packages.txt", "w") as f:
    for package in packages:
        program_name = package_map.get(package, package)  # Get mapped name or use original
        f.write(program_name + "\n")
