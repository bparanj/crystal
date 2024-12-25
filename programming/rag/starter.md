## Starter Template

Poetry project for a RAG AI application.  

```bash
my-rag-project/
├── pyproject.toml          # Poetry dependencies and project metadata
├── poetry.lock            # Locked dependencies
├── .env                   # Environment variables
├── .gitignore            # Git ignore file
├── README.md             # Project documentation
├── src/
│   ├── __init__.py
│   ├── config/           # Configuration management
│   │   ├── __init__.py
│   │   └── settings.py
│   ├── data/            # Data processing
│   │   ├── __init__.py
│   │   ├── loader.py
│   │   └── preprocessor.py
│   ├── retrieval/       # RAG retrieval components
│   │   ├── __init__.py
│   │   ├── embeddings.py
│   │   ├── vectorstore.py
│   │   └── retriever.py
│   └── utils/           # Utility functions
│       ├── __init__.py
│       └── logger.py
└── tests/              # Test directory
    ├── __init__.py
    ├── test_retrieval.py
    └── test_data.py
```

Here's the `pyproject.toml` with common RAG dependencies:

```toml
[tool.poetry]
name = "my-rag-project"
version = "0.1.0"
description = "RAG-based AI application"
authors = ["Your Name <your.email@example.com>"]

[tool.poetry.dependencies]
python = "^3.9"
langchain = "^0.1.0"
langchain-community = "^0.0.16"
langchain-openai = "^0.0.3"
chromadb = "^0.4.22"
python-dotenv = "^1.0.0"
tiktoken = "^0.5.2"
unstructured = "^0.11.0"
beautifulsoup4 = "^4.12.2"
faiss-cpu = "^1.7.4"

[tool.poetry.group.dev.dependencies]
pytest = "^7.4.4"
black = "^23.12.1"
isort = "^5.13.2"
mypy = "^1.8.0"
ruff = "^0.1.9"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

And a starter `.env` template:

```env
OPENAI_API_KEY=your_key_here
CHUNK_SIZE=1000
CHUNK_OVERLAP=200
MODEL_NAME=gpt-3.5-turbo
EMBEDDING_MODEL=text-embedding-3-large
```

Example file contents:

```python
# src/config/settings.py
from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 1000))
    CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 200))
    MODEL_NAME = os.getenv("MODEL_NAME", "gpt-3.5-turbo")
    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "text-embedding-3-large")

# src/retrieval/embeddings.py
from langchain_openai import OpenAIEmbeddings
from src.config.settings import Settings

def get_embeddings():
    return OpenAIEmbeddings(
        model=Settings.EMBEDDING_MODEL,
        openai_api_key=Settings.OPENAI_API_KEY
    )

# src/retrieval/retriever.py
from langchain_community.vectorstores import Chroma
from src.retrieval.embeddings import get_embeddings

def create_retriever(documents, collection_name="my_collection"):
    embeddings = get_embeddings()
    vectorstore = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        collection_name=collection_name
    )
    return vectorstore.as_retriever(search_kwargs={"k": 4})
```

To get started:

```bash
# Create new project
mkdir my-rag-project
cd my-rag-project

# Initialize Poetry
poetry init

# Install dependencies
poetry install

# Activate virtual environment
poetry shell
```

This structure provides:
1. Clean separation of concerns
2. Environment variable management
3. Common RAG dependencies pre-configured
4. Development tools (linting, formatting, type checking)
5. Testing setup

