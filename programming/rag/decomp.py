# Declarative composition showing the use of LCEL - LangChain Expression Language

from langchain_openai.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

template = ChatPromptTemplate.from_messages([
    ('system', 'You are a helpful assistant.'), 
    ('human', '{question}')])
model = ChatOpenAI()
chatbot = template | model
result = chatbot.invoke({"question": "Which model providers offer LLMs?"})
print(result)