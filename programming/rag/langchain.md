
- [Install Python](https://wiki.python.org/moin/BeginnersGuide/Download)
- [Install Jupyter](https://jupyter.org/install)

```
pip install jupyterlab
jupyter lab
```

- Install LangChain

```
pip install langchain langchain_openai langchain_community langchain-text-splitters langchain-postgres
```

pip install langchain openai

pip install langchain langchain-openai python-dotenv openai


- export OPENAI_API_KEY=your-key
- Open Jupyter notebook


```python
from langchain_openai.llms import OpenAI
model = OpenAI(model='​​gpt-3.5-turbo-instruct')
prompt = 'The sky is'
completion = model.invoke(prompt) 
completion
```

## Questions




## Tasks

- Add .env to the .gitignore file

