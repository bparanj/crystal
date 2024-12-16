# In the terminal:
# pip3 install langchain-openai
# pip3 install --upgrade pip

```python
"""
pip show langchain
Name: langchain
Version: 0.3.12
Summary: Building applications with LLMs through composability
Home-page: https://github.com/langchain-ai/langchain
Author: 
Author-email: 
License: MIT
Location: /opt/homebrew/lib/python3.11/site-packages
Requires: aiohttp, langchain-core, langchain-text-splitters, langsmith, numpy, pydantic, PyYAML, requests, SQLAlchemy, tenacity
Required-by: langchain-community
"""
```

# In the Jupyter notebook:

```python
from langchain_openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the model
model = OpenAI(model='gpt-3.5-turbo-instruct')

# Create and run the prompt
prompt = 'Bugs Bunny is'
completion = model.invoke(prompt)
print(completion)
```

In the virtual environment, you need to:

1. First, install all required packages:
```bash
pip install python-dotenv openai langchain-openai
```

2. Create a `.env` file in your project directory:
```bash
touch .env
```

3. Open the `.env` file and add your OpenAI API key:
```bash
OPENAI_API_KEY=your-api-key-here
```

4. Make sure your Python script and `.env` file are in the same directory. Here's the complete code with error checking:

```python
from langchain_openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Check if API key is loaded
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    raise ValueError("No OpenAI API key found. Please check your .env file.")

# Initialize the model
model = OpenAI(model='gpt-3.5-turbo-instruct')

# Create and run the prompt
prompt = 'Bugs Bunny is'
completion = model.invoke(prompt)
print(completion)
```
