from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader

# Error in example code: CharacterTextSplitter instead of RecursiveCharacterTextSplitter
# Load and split the documents
loader = TextLoader("./test.txt")
docs = loader.load()
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splitted_docs = splitter.split_documents(docs)

# Print each split chunk with its index
for i, doc in enumerate(splitted_docs):
    print(f"\nChunk {i+1}:")
    print("="*50)
    print(doc.page_content)
    
    # Optionally, print chunk length and metadata
    print(f"\nChunk length: {len(doc.page_content)} characters")
    print("Metadata:", doc.metadata)
    print("="*50)
