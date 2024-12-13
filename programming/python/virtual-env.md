
NOT TESTED CONTENT:

pipx install virtualenv

python<version> -m venv <virtual-environment-name>

source env/bin/activate

pip list

pip freeze > requirements.txt

pip install -r requirements.txt

deactivate

$ sudo apt update && sudo apt install software-properties-common

$ sudo add-apt-repository ppa:deadsnakes/ppa && sudo apt update

sudo apt install python3.x-full


Hatch and Rye are Python toolchains that focus on packaging, environment management, and dependency handling. They abstract away the need to install multiple Python versions system-wide. Instead, they manage project environments in a more portable and reproducible way.

On Ubuntu, you typically rely on `apt` and `venv` to manage Python installations and environments. This works well if you only need a few fixed versions. But if you want more flexibility, isolation, or are dealing with multiple projects that require different Python versions and dependencies, Hatch or Rye can simplify the process.

They integrate well with Ubuntu. However, these tools are newer and may have fewer community tutorials or system integrations compared to the standard `venv` and `virtualenv`. They make sense if you value cross-project consistency, easy environment creation, and simplified dependency workflows. For a beginner or a small project, sticking to `venv` and apt installations might be simpler. For complex, larger projects with evolving dependencies, Hatch and Rye can be worth it.

Think of Python installation and virtual environments much like how you handle Ruby installations and gems in a Rails project:

1. **System Python vs. System Ruby**:  
   On many systems, Python is already installed, much like system Ruby. But that version is part of the OS and often not the version you want for your project. Similarly, just as you often prefer managing Ruby versions yourself (with `rbenv` or `rvm`), you want to manage Python versions so they don’t conflict with system tools.

2. **Python Version Managers vs. rbenv/rvm**:  
   Python has tools like `pyenv` that mirror `rbenv` in concept. They let you install and switch between multiple Python versions without touching the system installation. This gives you fine-grained control, similar to how you might have multiple Ruby versions for different Rails projects.

3. **Virtual Environments vs. Bundler**:  
   In Ruby, you rely on a `Gemfile` and `bundle install` to ensure each project has the correct gems isolated from global gems. Python’s equivalent isolation tool is the virtual environment, created with `python -m venv myenv`. Once you activate this environment (`source myenv/bin/activate`), all libraries (`pip install ...`) go inside that environment’s directory. It’s like having a gemset local to your project, without polluting your system’s Python or other projects.

4. **Package Installation vs. Gems**:  
   Python uses `pip` and a `requirements.txt` or `pyproject.toml` for dependencies, which parallels `gem install` and `Gemfile.lock`. You run `pip install -r requirements.txt` inside your virtual environment, ensuring all installed packages stay confined. This mimics how Bundler ensures all gems resolve inside the local `.bundle` directory.

5. **Activating/Deactivating the Virtual Env**:  
   Just as you navigate to a project directory and use `rbenv local` or switch gemsets, you “enter” Python’s environment by activating it. This changes your shell’s path so `python` and `pip` now refer to the isolated versions. When you’re done, you “deactivate” it, returning to the system-wide Python setup.

In essence, Python version and environment management perform a similar role to rbenv/rvm and Bundler. They provide a clean, controlled way to manage languages and libraries across multiple projects without conflicts.

`pyenv` manages Python versions similarly to `rbenv`.  
`virtualenv` or the built-in `venv` module creates isolated environments, analogous to how RVM handles Ruby environments.

Yes. `pip` is to Python as `gem` is to Ruby. Running `pip install` is like using `gem install`: both fetch and install packages from their respective package repositories.
