from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import chain
from langchain_core.runnables.base import RunnableSequence
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_postgres.vectorstores import PGVector

# Load and split documents
raw_documents = TextLoader('./test.txt').load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
documents = text_splitter.split_documents(raw_documents)

# Setup vector store
model = OpenAIEmbeddings()
connection = 'postgresql+psycopg://langchain:langchain@localhost:6024/langchain'
db = PGVector.from_documents(documents, model, connection=connection)

# Initialize the LLM
llm = ChatOpenAI(temperature=0)
retriever = db.as_retriever()

# The prompt string
prompt = """Answer the question based on the following context:

Context: {context}

Question: {question}

Answer: """

rewrite_prompt = ChatPromptTemplate.from_template("""Provide a better search query for web search engine to answer the given question, end the queries with '**'. Question: {question} Answer: """)

def parse_rewriter_output(message):
    return message.content.strip('"').strip("**")

rewriter = rewrite_prompt | llm | parse_rewriter_output

@chain
def qa_rrr(question):
    # rewrite the query
    new_query = rewriter.invoke({"question": question})
    # fetch relevant documents
    docs = retriever.invoke(new_query)
    # format prompt
    context = "\n\n".join(doc.page_content for doc in docs)
    formatted = prompt.format(context=context, question=question)
    # generate answer
    answer = llm.invoke(formatted)
    return answer.content

# Test question
user_question = "man that sam bankman fried trial was crazy! what is triz?"
result = qa_rrr.invoke(user_question)
print(result)
