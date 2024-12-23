from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

# Initialize the chat model and history
chat = ChatOpenAI()
chat_history = InMemoryChatMessageHistory()

# Create a chat prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant that can translate between English and French."),
    ("human", "{input}"),
])

# Create the chain
chain = prompt | chat

# Add messages to chat history
chat_history.add_user_message("Translate this sentence from English to French: I love programming.")
chat_history.add_ai_message("J'adore la programmation.")
print("Chat history:", chat_history.messages)

# First interaction
response = chain.invoke({
    "input": "Translate this sentence from English to French: I love programming.",
    "chat_history": chat_history.messages
})
chat_history.add_ai_message(response)

# Second interaction
input2 = "What did I just ask you?"
chat_history.add_user_message(input2)
result = chain.invoke({
    "input": input2,
    "chat_history": chat_history.messages
})

print("\nFinal result:", result)
