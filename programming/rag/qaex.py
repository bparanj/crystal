from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_postgres.vectorstores import PGVector
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnableLambda

# Load and split documents
raw_documents = TextLoader('./test.txt').load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
documents = text_splitter.split_documents(raw_documents)

# Setup vector store
model = OpenAIEmbeddings()
connection = 'postgresql+psycopg://langchain:langchain@localhost:6024/langchain'
db = PGVector.from_documents(documents, model, connection=connection)

# Setup components
retriever = db.as_retriever()
prompt = ChatPromptTemplate.from_template("""Answer the question based only on the following context:
{context}
Question: {question}
""")
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

def create_chain(func):
    def run(input):
        # fetch relevant documents
        docs = retriever.invoke(input)
        # format prompt
        formatted = prompt.invoke({"context": docs, "question": input})
        # generate answer
        answer = llm.invoke(formatted)
        return {"answer": answer, "docs": docs}
    
    return RunnableLambda(run)

@create_chain
def qa(input):
    pass

# Run the chain
response = qa.invoke("What is TRIZ?")

# Print results
print("\nAnswer:", response["answer"].content)
print("\nSource Documents:")
for i, doc in enumerate(response["docs"], 1):
    print(f"\nDocument {i}:")
    print(doc.page_content[:200] + "...")