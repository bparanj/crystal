from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

prompt_hyde = ChatPromptTemplate.from_template("""Please write a scientific paper passage to answer the question
                                               Question: {question}
                                               Passage: """)
generate_doc = (prompt_hyde | ChatOpenAI(temperature=0) | StrOutputParser())
retrieval_chain = generate_doc | retriever
prompt = ChatPromptTemplate.from_template("""Answer the following question base on this context:
                                          {context}
                                          Question: {question}
                                          """)
llm = ChatOpenAI(temperature=0)
@chain
def qa(input):
    # fetch relevant documents from the hyde retrieval chain defined earlier
    docs = retrieval_chain.invoke(input)
    # format prompt
    formatted = prompt.invoke({"context": docs, "question": input})
    # generate answer
    answer = llm.invoke(formatted)

    return answer

qa.invoke("What is TRIZ?")

