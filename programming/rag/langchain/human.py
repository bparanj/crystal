from langchain_openai.chat_models import ChatOpenAI
from langchain_core.messages import HumanMessage
import apikey

model = ChatOpenAI()
prompt = [HumanMessage('What is the capital of Switzerland?')]
completion = model.invoke(prompt)

print(completion.content)
