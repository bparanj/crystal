from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_openai.chat_models import ChatOpenAI
import apikey

model = ChatOpenAI()
system_message = SystemMessage('You are a helpful assitant that responds to questions with three exclamation marks')
human_message = HumanMessage('What is the capital of Norway?')
completion = model.invoke([system_message, human_message])
print(completion.content)
