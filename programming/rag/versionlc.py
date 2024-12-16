"""
python versionlc.py                               
Traceback (most recent call last):
  File "/Users/bparanj/work/nuxt/programming/rag/versionlc.py", line 1, in <module>
    import langchain
ModuleNotFoundError: No module named 'langchain'

pip install langchain
"""

import langchain

print(langchain.__version__)

import openai

print(openai.__version__)
