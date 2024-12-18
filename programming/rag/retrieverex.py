from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_postgres.vectorstores import PGVector

# Load the document, split it into chunks
raw_documents = TextLoader('./test.txt').load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
documents = text_splitter.split_documents(raw_documents)

# embed each chunk and insert it into the vector store
model = OpenAIEmbeddings()
connection = 'postgresql+psycopg://langchain:langchain@localhost:6024/langchain'
db = PGVector.from_documents(documents, model, connection = connection)
# create retriever
retriever = db.as_retriever()
# fetch relevant documents
docs = retriever.invoke("What is TRIZ?")

for doc in docs:
    print(f"\nContent: {doc.page_content}\n")

print(f"After retriever with k = 2: \n")

# create retriever with k = 2
retriever = db.as_retriever(search_kwargs={"k": 2})
# fetch the 2 most relevant documents
docs = retriever.invoke("What is TRIZ?")

for doc in docs:
    print(f"\nContent: {doc.page_content}\n")