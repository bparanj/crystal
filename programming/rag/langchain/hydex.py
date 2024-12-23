from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_postgres import PGVector
from typing import Dict, Any

# Database configuration
COLLECTION_NAME = "langchain_collection"
CONNECTION_STRING = 'postgresql+psycopg2://langchain:langchain@localhost:6024/langchain'

# Load and split documents
loader = TextLoader('./test.txt')
raw_documents = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
documents = text_splitter.split_documents(raw_documents)

# Setup vector store
embeddings = OpenAIEmbeddings()

# Initialize and populate vector store
db = PGVector.from_documents(
    documents=documents,
    embedding=embeddings,
    collection_name=COLLECTION_NAME,
    connection=CONNECTION_STRING,
)

# Initialize the retriever
retriever = db.as_retriever()

# Create prompts
prompt_hyde = ChatPromptTemplate.from_template("""Please write a scientific paper passage to answer the question
Question: {question}
Passage: """)

qa_prompt = ChatPromptTemplate.from_template("""Answer the following question based on this context:
Context: {context}
Question: {question}
""")

# Setup chains
llm = ChatOpenAI(temperature=0)
generate_hyde = prompt_hyde | llm | StrOutputParser()
retrieval_chain = generate_hyde | retriever

def qa_chain(input: Dict[str, Any]) -> str:
    # Get question from input
    question = input["question"]
    
    # Fetch relevant documents from the hyde retrieval chain
    docs = retrieval_chain.invoke({"question": question})
    
    # Extract text from documents
    context = "\n".join(doc.page_content for doc in docs)
    
    # Format prompt with context and question
    formatted_prompt = qa_prompt.format(context=context, question=question)
    
    # Generate answer
    answer = llm.invoke(formatted_prompt)
    return answer.content

# Example usage
if __name__ == "__main__":
    result = qa_chain({"question": "What is TRIZ?"})
    print(result)