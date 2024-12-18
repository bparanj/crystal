from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_postgres.vectorstores import PGVector
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load and split the documents
raw_documents = TextLoader('./test.txt').load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
documents = text_splitter.split_documents(raw_documents)

# Setup the vector store
model = OpenAIEmbeddings()
connection = 'postgresql+psycopg://langchain:langchain@localhost:6024/langchain'
db = PGVector.from_documents(documents, model, connection=connection)

# Setup the retriever and chain
retriever = db.as_retriever()
prompt = ChatPromptTemplate.from_template("""Answer the question based only on the following context:
{context}
Question: {question}
""")
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

chain = prompt | llm
docs = retriever.invoke("What is TRIZ?")
response = chain.invoke({"context": docs, "question": "What is TRIZ?"})
print(f"Response content: {response.content}")
