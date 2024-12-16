from langchain_openai.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import chain

template = ChatPromptTemplate.from_messages([('system', 'You are a helpful assistant and you know about Large Language Models (LLMs)'), ('human', '{question}')])
model = ChatOpenAI()

@chain
def chatbot(values):
    """Enable streaming or async support to chatbot method"""
    prompt = template.invoke(values)
    for token in model.invoke(prompt):
        yield token

for part in chatbot.stream({
    "question": "Which model providers offer Large Language Models"
}):
    print(part)
