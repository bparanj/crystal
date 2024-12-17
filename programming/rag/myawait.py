from langchain_openai.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
import asyncio

template = ChatPromptTemplate.from_messages([
    ('system', 'You are a helpful assistant.'), 
    ('human', '{question}')
])

model = ChatOpenAI()
chatbot = template | model

async def main():
    result = await chatbot.ainvoke({"question": "Which model providers offer LLMs?"})
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
