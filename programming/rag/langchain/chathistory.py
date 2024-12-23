from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_postgres.vectorstores import PGVector

#  Start the postgres using Docker desktop

# Load the document, split it into chunks
raw_documents = TextLoader('./test.txt').load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
documents = text_splitter.split_documents(raw_documents)

# embed each chunk and insert it into the vector store
model = OpenAIEmbeddings()
connection = 'postgresql+psycopg://langchain:langchain@localhost:6024/langchain'
db = PGVector.from_documents(documents, model, connection=connection)
retriever = db.as_retriever()

from langchain_openai import ChatOpenAI
from langchain_core.runnables import chain
from langchain_core.prompts import ChatPromptTemplate
def get_msg_content(msg):
    return msg.content
contextualize_system_prompt = (
    "Given a chat history and the latest user question "
    "which might reference context in the chat history, "
    "formulate a standalone question which can be understood "
    "without the chat history. Do NOT answer the question, "
    "just reformulate it if needed and otherwise return it as is."
)
contextualize_prompt = ChatPromptTemplate.from_messages([
    ("system", contextualize_system_prompt),
    ("placeholder", "{chat_history}"),
    ("human", "{input}"),
])
contextualize_chain = (
    contextualize_prompt
    | ChatOpenAI()
    | get_msg_content
)
qa_system_prompt = (
    "You are an assistant for question-answering tasks. "
    "Use the following pieces of retrieved context to answer "
    "the question. If you don't know the answer, say that you "
    "don't know. Use three sentences maximum and keep the "
    "answer concise."
    "\n\n"
    "{context}"
)
qa_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", qa_system_prompt),
        ("placeholder", "{chat_history}"),
        ("human", "{input}"),
    ]
)
qa_chain = (
    qa_prompt
    | ChatOpenAI()
    | get_msg_content
) 
@chain
def history_aware_qa(input):
     # rephrase question if needed
     if input.get('chat_history'):
         question = contextualize_chain.invoke(input)
     else:
         question = input['input']
     # get context from retriever
     context = retriever.invoke(question)
     # get answer
     return qa_chain.invoke({
         **input,
         "context": context
     })

from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory

chat_history_for_chain = InMemoryChatMessageHistory()
qa_with_history = RunnableWithMessageHistory(
    history_aware_qa,
    lambda _: chat_history_for_chain,
    input_messages_key="input",
    history_messages_key="chat_history",
)
result = qa_with_history.invoke(
    {"input": "What is TRIZ?"},
    config={"configurable": {"session_id": "123"}},
)

print(result)


