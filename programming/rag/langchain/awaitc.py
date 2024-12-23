from langchain_openai.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import chain
import asyncio

template = ChatPromptTemplate.from_messages([
    ('system', 'You are a helpful assistant and you know about Large Language Models (LLMs)'),
    ('human', '{question}')
])
model = ChatOpenAI()

@chain
async def chatbot(values):
    """Asynchronous execution of chatbot"""
    prompt = await template.ainvoke(values)
    return await model.ainvoke(prompt)

async def main():
    result = await chatbot.ainvoke({
        "question": "which model providers offer LLMs"
    })
    print(result)

# Run the async main function
if __name__ == "__main__":
    asyncio.run(main())
