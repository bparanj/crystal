from langchain.prompts import ChatPromptTemplate

perspectives_prompt = ChatPromptTemplate.from_template("""You are an AI language model assistant. Your task is to generate five different versions of the given user question to retrieve relevant documents from a vector database. By generating multiple perspectives on the user question, your goal is to help the user overcome some of the limitations of the distance-based similarity search. Provide these laternative questions separated by newlines. Original question: {question}""")

def parse_queries_output(message)
    return message.content.split('\n')

query_gen = perspectives_prompt | llm | parse_queries_output

def get_unique_union(document_lists):
    # Flatten list of lists, and dedupe them
    deduped_docs = { doc.page_content: doc for sublist in document_lists for doc in sublist }
    # return a flat list of unique docs
    return list(deduped_docs.values())

retrieval_chain = query_gen | retriever.batch | get_unique_union
prompt = ChatPromptTemplate.from_template("""Answer the following question based on this context:
                                          {context}
                                          Question: {question}""")
llm = ChatOpenAI(temperature=0)
@chain
def multi_query_qa(input):
    # fetch relevant documents
    docs = retrieval_chain.invoke(input)
    # format prompt
    formatted = prompt.invoke({"context": docs, "question": input})
    # generate answer
    answer = llm.invoke(formatted)
    return answer

multi_query_qa.invoke("What is TRIZ?")
