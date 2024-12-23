THE FOLLOWING CODE IS USING 0.0.194. USE ONLY THE HIGH LEVEL STEPS.

Here’s a sample **RAG (Retrieval-Augmented Generation)** workflow using LangChain. This example demonstrates the core components: document loading, vector database indexing, and query generation using a language model.

---

### Step 1: Install Dependencies
Make sure you have the necessary libraries installed:
```bash
pip install langchain openai pinecone tiktoken
```

---

### Step 2: Import Libraries and Set Up API Keys
```python
from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import pinecone
import os

# Set up API keys (replace with your actual keys)
os.environ["OPENAI_API_KEY"] = "your-openai-api-key"
pinecone.init(api_key="your-pinecone-api-key", environment="your-pinecone-environment")
```

---

### Step 3: Load and Split Documents
Load your documents (e.g., text files, PDFs, etc.) and split them into chunks for indexing.

```python
# Load documents
loader = TextLoader("example.txt")  # Replace with your file
documents = loader.load()

# Split text into manageable chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = text_splitter.split_documents(documents)
```

---

### Step 4: Create Vector Store with Pinecone
Convert documents into embeddings and store them in a vector database for retrieval.

```python
# Create embeddings using OpenAI
embeddings = OpenAIEmbeddings()

# Set up Pinecone vector store
index_name = "rag-example"
pinecone.create_index(index_name, dimension=1536)
vector_store = Pinecone(index_name, embeddings.embed_query, embeddings)

# Add documents to the vector store
vector_store.add_documents(docs)
```

---

### Step 5: Build the RAG Chain
Use the vector store as the retriever for your language model.

```python
# Set up retriever
retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 3})

# Create a RetrievalQA chain
llm = OpenAI(model="gpt-4")
rag_chain = RetrievalQA(llm=llm, retriever=retriever)
```

---

### Step 6: Query the RAG System
Pass user queries to the RAG system and get answers augmented with retrieved documents.

```python
# Example query
query = "What are the key benefits of renewable energy?"
result = rag_chain.run(query)

# Display the result
print("Query:", query)
print("Answer:", result)
```

---

### Explanation of Components
1. **Document Loader**: Reads raw text or other file types into a format usable by LangChain.
2. **Text Splitter**: Breaks large documents into smaller chunks for embedding.
3. **Vector Store**: Stores embeddings and retrieves relevant chunks based on similarity.
4. **Retriever**: Searches the vector store for relevant chunks.
5. **LLM (Language Model)**: Combines retrieved information with the query to generate an answer.

---

### Customization Options
- **Document Loaders**: Use `UnstructuredLoader` or `PyPDFLoader` for PDFs or other formats.
- **Vector Stores**: Replace Pinecone with FAISS for local storage.
- **LLMs**: Use Hugging Face models if you prefer open-source options.

---

To keep track of the input data and its source document for retrieval-augmented generation (RAG), you can extend the workflow by storing metadata about each document. This metadata helps identify the source used to generate the answer and facilitates updating or reindexing when the source changes.

Here’s how you can implement this:

---

### 1. **Track Metadata for Each Document**

When loading and indexing documents, include metadata such as:
- Source file name or URL.
- Timestamps for version tracking.
- Tags or categories for easier filtering.

#### Update the Document Loading and Indexing Step:
```python
# Load documents with metadata
loader = TextLoader("example.txt")  # Replace with your file
documents = loader.load()

# Add metadata to each document
for doc in documents:
    doc.metadata = {"source": "example.txt", "last_updated": "2023-12-22"}

# Split text into manageable chunks with metadata preserved
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = text_splitter.split_documents(documents)

# Add documents with metadata to the vector store
vector_store.add_documents(docs)
```

---

### 2. **Retrieve Metadata Alongside Results**

Modify the retriever to include metadata with the retrieved documents:
```python
# Retrieve documents with metadata
retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 3})

# Run query with metadata
results = retriever.get_relevant_documents("What are the key benefits of renewable energy?")
for result in results:
    print("Content:", result.page_content)
    print("Source:", result.metadata["source"])
    print("Last Updated:", result.metadata["last_updated"])
```

---

### 3. **Integrate Metadata in the RAG Chain**

Update the RAG chain to include document metadata in the final output:
```python
from langchain.chains import RetrievalQAWithSourcesChain

# Create a RetrievalQA chain with sources
rag_chain = RetrievalQAWithSourcesChain(llm=llm, retriever=retriever)

# Query the RAG chain
query = "What are the key benefits of renewable energy?"
result = rag_chain.run(query)

# Display the final result and sources
print("Answer:", result["answer"])
print("Sources:", result["sources"])
```

---

### 4. **Reindex When Source Changes**

You can track and reindex a document when its source file changes:
- Monitor files for changes using file watchers (e.g., `watchdog` library in Python).
- When a change is detected, reload the file, split it, and update the vector store.

#### Example Code for Reindexing:
```python
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == "example.txt":
            print("Source document changed. Reindexing...")
            updated_documents = loader.load()
            updated_chunks = text_splitter.split_documents(updated_documents)
            vector_store.add_documents(updated_chunks)

# Watch the directory for changes
event_handler = FileChangeHandler()
observer = Observer()
observer.schedule(event_handler, path=".", recursive=False)
observer.start()

# Keep the program running to monitor changes
try:
    while True:
        pass
except KeyboardInterrupt:
    observer.stop()
observer.join()
```

---

### Summary of Workflow:
1. **Metadata Tracking**:
   - Store file names, timestamps, and other details in document metadata.
2. **Result Attribution**:
   - Retrieve and display metadata with the answer.
3. **Change Detection**:
   - Monitor source documents for changes and reindex them automatically.

This setup ensures traceability of sources, provides context for answers, and keeps the indexed database up-to-date.
