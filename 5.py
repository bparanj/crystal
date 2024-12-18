from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import chain

retriever = db.as_retriever()
prompt = ChatPromptTemplate.from_template("""Answer the question based only on the following context:
{context}
Question: {question}
""")
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
@chain
def qa(input):
    # fetch relevant documents
    docs = retriever.get_relevant_documents(input)
    # format prompt
    formatted = prompt.invoke({"context": docs, "question": input)
    # generate answer
    answer = llm.invoke(formatted)

    return {"answer": answer, "docs": docs}

qa.invoke("What is TRIZ?")
