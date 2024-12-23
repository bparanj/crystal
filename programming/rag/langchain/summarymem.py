from operator import itemgetter
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.messages import trim_messages
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

# Initialize the trimmer
trimmer = trim_messages(
   max_tokens=65,
   strategy="last", 
   token_counter=ChatOpenAI(model="gpt-4"),
   include_system=True,
   allow_partial=False,
   start_on="human"
)

# Create prompt template
prompt = ChatPromptTemplate.from_messages([
   ("system", "You are a helpful assistant. Answer all questions to the best of your ability."),
   ("placeholder", "{messages}"),
])

# Initialize model
model = ChatOpenAI()

# Create chain with trimmer
chain = {"messages": trimmer} | prompt | model

# Initialize chat history 
history = InMemoryChatMessageHistory()

# Create chain with message history
with_message_history = RunnableWithMessageHistory(
   chain,
   lambda: history,
   input_messages_key="messages",
   history_messages_key="messages"
)

# Example usage
response = with_message_history.invoke(
   {"messages": [HumanMessage(content="whats my name?")]}
)
print(response)
