from typing import Literal
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI

# Data model
class RouteQuery(BaseModel):
    """Route a user query to the most relevant datasource."""
    datasource: Literal["python_docs", "js_docs"] = Field(..., description="Given a uwer question choose which datasource would be most relevant for answering their question")

# LLM with function call
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
structured_llm = llm.with_structured_output(RouteQuery)
# prompt
system = """You are an expert at routing a user question to the appropriate data source. 
Based on the programming language the question is referring to, route it to the relevant data source."""
prompt = ChatPromptTemplate.from_messages([
    ("system", system),
    ("human", "{question}")
    ])
# define router 
router = prompt | structured_llm
question = """Why doesn't the following code work:
    from langchain_core.prompts import ChatPromptTemplate
    prompt = ChatPromptTemplate.from_messages(["human", "speak in {language}"])
    prompt.invoke("french")
    """
result = router.invoke({"question": question })
result.datasource
# python_docs

def choose_route(result):
    if "python_docs" in result.datasource.lower():
        ### logic here
        return "chain for python docs"
    else:
        ## else logic
        return "chain for js_docs"

full_chain = router | RunnableLambda(choose_route)

