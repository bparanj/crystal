# In the terminal:
# pip3 install langchain-openai
# pip3 install --upgrade pip

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
