from langchain_text_splitters import (Language, RecursiveCharacterTextSplitter)

markdown_text = """
# LangChain
Building applications with LLMs through composability
## Quick Install
```bash
pip install langchain
```
As an open source project in a rapidly developing field, we are open to contributions.
"""

md_splitter = RecursiveCharacterTextSplitter.from_language(language=Language.MARKDOWN, chunk_size=60, chunk_overlap=0)
md_docs = md_splitter.create_documents([markdown_text], [{"source": "https://www.langchain.com"}])

print(f"Total number of chunks: {len(md_docs)}")

# Print each chunk with its metadata
for i, doc in enumerate(md_docs):
    print(f"\nChunk {i+1}:")
    print("="*50)
    print("Content:")
    print(doc.page_content)
    print("\nMetadata:")
    print(doc.metadata)
    print(f"Length: {len(doc.page_content)} characters")
    print("="*50)
