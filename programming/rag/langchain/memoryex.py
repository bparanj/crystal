from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Answer all questions to the best of your ability."),
    ("placeholder", "{messages}"),
])
model = ChatOpenAI()
chain = prompt | model
result = chain.invoke({
    "messages": [
        ("human","Translate this sentence from English to French: I love programming."),
        ("ai", "J'adore la programmation."),
        ("human", "What did you just say?"),
    ],
})
print(result)
