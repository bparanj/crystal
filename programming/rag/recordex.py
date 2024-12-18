from langchain.indexes import SQLRecordManager, index
from langchain_core.documents import Document
from langchain_postgres.vectorstores import PGVector
from langchain_openai import OpenAIEmbeddings
from datetime import datetime

# Define namespace
namespace = "my_documents"
print(f"\n=== Initializing Record Manager with namespace: {namespace} ===")

# Initialize record manager
record_manager = SQLRecordManager(
    namespace=namespace, 
    db_url="postgresql+psycopg://langchain:langchain@localhost:6024/langchain"
)

print("\n=== Creating Schema ===")
record_manager.create_schema()

# Create documents with unique identifiers
current_time = datetime.now().isoformat()
doc1Updated = Document(
    page_content="there are rabbits in the yard",
    metadata={
        "source": "yard_docs_1",
        "version": "2",
        "timestamp": current_time,
        "doc_uuid": "doc1"
    }
)

doc2 = Document(
    page_content="ducks are also found in the yard",
    metadata={
        "source": "yard_docs_2",
        "version": "1",
        "timestamp": current_time,
        "doc_uuid": "doc2"
    }
)

# Initialize embeddings and connection string
print("\n=== Initializing Vector Store ===")
embeddings = OpenAIEmbeddings()
CONNECTION_STRING = "postgresql+psycopg://langchain:langchain@localhost:6024/langchain"

# Create temporary document for initialization
init_doc = Document(
    page_content="initialization document",
    metadata={"doc_uuid": "init"}
)

# Initialize vector store with the temporary document
print("\n=== Creating Vector Store ===")
vectorstore = PGVector.from_documents(
    documents=[init_doc],
    collection_name="triz_collection",
    connection=CONNECTION_STRING,
    embedding=embeddings,
    pre_delete_collection=True
)

# Delete the initialization document
print("\n=== Cleaning Initialization Document ===")
vectorstore.delete({"doc_uuid": "init"})

# Now use the record manager to add the actual documents
print("\n=== Adding Documents via Record Manager ===")
index_result = index(
    [doc1Updated, doc2],
    record_manager,
    vectorstore,
    cleanup='full',
    source_id_key="doc_uuid"
)

# Verify final state
print("\n=== Final Verification ===")
final_results = vectorstore.similarity_search("yard", k=10)
print(f"\nFinal count of documents: {len(final_results)}")
for i, doc in enumerate(final_results, 1):
    print(f"\nDocument {i}:")
    print(f"Content: {doc.page_content}")
    print(f"Metadata: {doc.metadata}")

# Check for duplicates
def check_duplicates(results):
    seen = set()
    duplicates = []
    for doc in results:
        doc_id = doc.metadata.get('doc_uuid')
        if doc_id in seen:
            duplicates.append(doc_id)
        seen.add(doc_id)
    return duplicates

duplicates = check_duplicates(final_results)
if duplicates:
    print("\nWarning: Found duplicate documents with IDs:", duplicates)
else:
    print("\nNo duplicates found!")
