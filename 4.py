from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

retriever = db.as_retriever()
prompt = ChatPromptTemplate.from_template("""Answer the question based only on the following context:
{context}
Question: {question}
""")
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
chain = prompt | llm
# fetch relevant documents
docs = retriever.get_relevant_documents("What is TRIZ?")
chain.invoke({"context": docs, "question": "What is TRIZ?"})
