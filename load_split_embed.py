from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings

loader = TextLoader("./test.txt")
doc = loader.load()
"""
[
    Document(page_content='document loaders\n\nUse document loaders to load data from a source as `Document`\'s. A `Document` is a piece of text\nand asociated metadata. For example, there are document loaders for loading a simple `.txt` file, for loading the text\ncontents of any web page, or even for loading a transcript of a YouTube video.\n\nEvery document loader exposes two methods:\n1. "Load": load documents from the configured source\n2. "Load and split": load documents from the configured source and split them using the passed in text splitter\n\nThey optionally implement:\n\n3. "Lazy Load": load documents into memory lazily\n', metadata={'source': 'test.txt'})
]
"""
## Split the document
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=20)
chunks = text_splitter.split_documents(doc)
## Generate embeddings
model = OpenAIEmbeddings()
embeddings = embeddings_model.embed_documents(chunk.page_content for chunk in chunks)

