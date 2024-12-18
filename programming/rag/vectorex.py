from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_postgres.vectorstores import PGVector
from langchain_core.documents import Document

from pprint import pprint

# brew install postgresql
# pip install psycopg2-binary  
# pip install "psycopg[binary]"

# Connection settings
connection_string = "postgresql+psycopg://langchain:langchain@localhost:6024/langchain"
COLLECTION_NAME = "triz_collection"  # Add a collection name

# 1. Load and inspect raw documents
loader = TextLoader('./test.txt')
raw_documents = loader.load()

print("=== Raw Document ===")
print(f"Number of documents: {len(raw_documents)}")
print("First document content:")
print(raw_documents[0].page_content[:200] + "...")  # Show first 200 chars
print(f"Metadata: {raw_documents[0].metadata}")
print("\n")

# 2. Split and inspect chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
documents = text_splitter.split_documents(raw_documents)

print("=== Split Documents ===")
print(f"Number of chunks: {len(documents)}")
print("First chunk content:")
print(documents[0].page_content[:200] + "...")
print(f"First chunk metadata: {documents[0].metadata}")
print("\n")

# Initialize embeddings
embeddings = OpenAIEmbeddings()

# Create vector store
db = PGVector.from_documents(
    documents=documents,
    embedding=embeddings,
    collection_name=COLLECTION_NAME,
    connection=connection_string  
)

# 4. Perform similarity search and inspect results
query = "triz"
search_results = db.similarity_search(query, k=4)

print("=== Search Results ===")
print(f"Number of results: {len(search_results)}")
for i, doc in enumerate(search_results, 1):
    print(f"\nResult {i}:")
    print("Content:")
    print(doc.page_content[:200] + "...")  # Show first 200 chars
    print(f"Metadata: {doc.metadata}")
    print("-" * 50)

# 5. Optional: Get raw scores with similarity_search_with_score
search_results_with_scores = db.similarity_search_with_score(query, k=4)

print("\n=== Search Results with Scores ===")
for i, (doc, score) in enumerate(search_results_with_scores, 1):
    print(f"\nResult {i} (Score: {score}):")
    print("Content:")
    print(doc.page_content[:200] + "...")
    print(f"Metadata: {doc.metadata}")
    print("-" * 50)


# Continue from db.add_documents([Document...

# After adding documents, here's how to delete specific documents
# Instead of using ids, we need to use metadata

# Add documents (without specifying ids since PGVector doesn't use them)
db.add_documents([
    Document(
        page_content="there are rabbits in the yard", 
        metadata={"location": "yard", "topic": "animals", "doc_id": "1"}
    ),
    Document(
        page_content="ducks are also found in the yard", 
        metadata={"location": "yard", "topic": "animals", "doc_id": "2"}
    )
])

# To delete a specific document, use metadata filtering

# This will delete the document about ducks
# db.delete(
#     {"page_content": "ducks are also found in the yard"}
# )

# Or delete by metadata
db.delete(
    {"doc_id": "2"}
)

# To delete all documents with specific metadata
# db.delete(
#     {"location": "yard", "topic": "animals"}
# )
