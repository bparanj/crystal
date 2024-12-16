When using virtual environments, you can use either `pip` or `pip3` - they'll work the same way as long as your virtual environment is activated. Here's why:

1. Inside an activated virtual environment, `pip` automatically points to the correct Python version of your virtual environment. The virtual environment ensures isolation, so you don't need to specifically use `pip3`.

2. However, `pip3` will also work fine - it's just being explicit about using Python 3.

The key point is making sure your virtual environment is activated before running any pip commands. You can tell it's activated when you see the virtual environment name in parentheses at the start of your command prompt, like:

```bash
(myenv) $
```

Best practices:
- Always activate your virtual environment first: `source venv/bin/activate` (Unix/macOS) or `venv\Scripts\activate` (Windows)
- Use `pip` for simplicity once the environment is activated
- Use `pip list` to verify package installations in your environment
- Use `which pip` (Unix/macOS) or `where pip` (Windows) to confirm you're using the virtual environment's pip
