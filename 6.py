from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import chain
from langchain_core.runnables.base import RunnableSequence
from langchain_openai import ChatOpenAI

# Initialize the LLM
llm = ChatOpenAI(temperature=0)
retriever = ...
prompt = ...

rewrite_prompt = ChatPromptTemplate.from_template("""Provide a better search query for web search engine to answer the given question, end the queries with '**'. Question: {x} Answer: """)

def parse_rewriter_output(message):
    return message.content.strip('"').strip("**")

rewriter = rewrite_prompt | llm | parse_rewriter_output

@chain
def qa_rrr(input):
    # rewrite the query
    new_query = rewriter.invoke(input)
    # fetch relevant documents
    docs = retriever.get_relevant_documents(new_query)
    # format prompt
    formatted = prompt.invoke({"context": docs, "question": input})
    # generate answer
    answer = llm.invoke(formatted)
    return answer

qa_rrr.invoke("man that sam bankman fried trial was crazy! what is lanchain?")
