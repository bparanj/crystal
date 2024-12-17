from langchain_text_splitters import (Language, RecursiveCharacterTextSplitter)

PYTHON_CODE = """
def hello_world():
    print("Hello, World!")
# call the function
hello_world()
"""

python_splitter = RecursiveCharacterTextSplitter.from_language(language=Language.PYTHON, chunk_size=50, chunk_overlap=0)
python_docs = python_splitter.create_documents([PYTHON_CODE])

print(f"Total chunks: {len(python_docs)}")

# Print each chunk with its index
for i, doc in enumerate(python_docs):
    print(f"\nChunk {i+1}:")
    print("="*50)
    print(doc.page_content)
    print(f"\nChunk length: {len(doc.page_content)} characters")
