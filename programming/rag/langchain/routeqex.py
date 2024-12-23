from typing import Literal
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableLambda

# Data model
class RouteQuery(BaseModel):
    """Route a user query to the most relevant datasource."""
    datasource: Literal["python_docs", "js_docs"] = Field(
        ..., 
        description="Given a user question choose which datasource would be most relevant for answering their question"
    )

# LLM with function call
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
structured_llm = llm.with_structured_output(RouteQuery)

# Prompt
system = """You are an expert at routing user questions to the appropriate data source. 
Based on the programming language the question is referring to, route it to the relevant data source."""

prompt = ChatPromptTemplate.from_messages([
    ("system", system),
    ("human", "{question}")
])

# Define router 
router = prompt | structured_llm

def choose_route(result):
    if result.datasource.lower() == "python_docs":
        # Logic for Python docs
        return "chain for python docs"
    else:
        # Logic for JS docs
        return "chain for js_docs"

# Create full chain
full_chain = router | RunnableLambda(choose_route)

# Example usage
question = """Why doesn't the following code work:
    from langchain_core.prompts import ChatPromptTemplate
    prompt = ChatPromptTemplate.from_messages(["human", "speak in {language}"])
    prompt.invoke("french")
    """

# Run the chain
result = full_chain.invoke({"question": question})
print(result)  # Will print "chain for python docs"
