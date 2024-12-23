from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings

# Error: embeddings_model is used instead of model in the book

# 1. Load the document
loader = TextLoader("./test.txt")
docs = loader.load()  # Note: Changed 'doc' to 'docs' as it returns a list

# View the loaded document
print("Original Document:")
print("="*50)
for doc in docs:
    print("Content:", doc.page_content)
    print("Metadata:", doc.metadata)
    print("="*50)

# 2. Split the document
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=20)
chunks = text_splitter.split_documents(docs)

# View the chunks
print("\nSplit Chunks:")
print("="*50)
for i, chunk in enumerate(chunks):
    print(f"\nChunk {i+1}:")
    print(chunk.page_content)
    print(f"Metadata: {chunk.metadata}")
    print("="*50)

# 3. Generate embeddings
embeddings_model = OpenAIEmbeddings()  # Fixed variable name
embeddings = embeddings_model.embed_documents([chunk.page_content for chunk in chunks])

# View embeddings
print("\nEmbeddings:")
print("="*50)
for i, embedding in enumerate(embeddings):
    print(f"Embedding {i+1} length: {len(embedding)}")
    print(f"First few values: {embedding[:5]}")  # Show first 5 values
    print("="*50)
