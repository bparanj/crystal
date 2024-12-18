from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import chain
from langchain_core.runnables import RunnablePassthrough
from langchain_core.runnables.base import RunnableSequence
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

prompt_rag_fusion = ChatPromptTemplate.from_template("""You are a helpful assistant that generates multiple search queries based on a single input query. \n
                                                     Generate multiple search queries related to: {question} \n
                                                     Output (4 queries):""")

def parse_queries_output(message):
    return message.content.split('\n')

def get_relevant_docs_batch(queries):
    results = []
    for query in queries:
        docs = retriever.invoke(query)
        results.append(docs)
    return results

def reciprocal_rank_fusion(results: list[list], k=60):
    fused_scores = {}
    documents = {}
    for docs in results:
        for rank, doc in enumerate(docs):
            doc_str = doc.page_content
            if doc_str not in fused_scores:
                fused_scores[doc_str] = 0
                documents[doc_str] = doc
            fused_scores[doc_str] += 1 / (rank + k)
    reranked_doc_strs = sorted(fused_scores, key=lambda d: fused_scores[d], reverse=True)
    return [documents[doc_str] for doc_str in reranked_doc_strs]

query_gen = prompt_rag_fusion | llm | parse_queries_output

retrieval_chain = (
    RunnablePassthrough(lambda x: {"question": x}) | 
    query_gen | 
    get_relevant_docs_batch | 
    reciprocal_rank_fusion
)

prompt = ChatPromptTemplate.from_template("""Answer the following question based on this context:
                                          {context}
                                          Question: {question}
                                          """)

@chain
def multi_query_qa(input):
    docs = retrieval_chain.invoke(input)
    context = "\n\n".join(doc.page_content for doc in docs)
    formatted = prompt.invoke({"context": context, "question": input})
    answer = llm.invoke(formatted)
    return answer.content

result = multi_query_qa.invoke("What is TRIZ?")
print(result)
