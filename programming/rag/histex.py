from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.runnables.history import RunnableWithMessageHistory

# Initialize the chat model
model = ChatOpenAI()

# Create the chat prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Answer all questions to the best of your ability."),
    ("placeholder", "{history}"),
    ("human", "{input}"),
])

# Create the basic chain
chain = prompt | model

# Dictionary to store chat histories
histories: dict[str, InMemoryChatMessageHistory] = {}

def get_session_history(session_id: str = '') -> InMemoryChatMessageHistory:
    """Get or create chat history for a session"""
    if session_id not in histories:
        histories[session_id] = InMemoryChatMessageHistory()
    return histories[session_id]

# Create chain with message history
chain_with_history = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history",
)

# Example usage
def chat_with_history(input_text: str, session_id: str):
    """Function to interact with the chain"""
    return chain_with_history.invoke(
        {"input": input_text},
        config={"configurable": {"session_id": session_id}},
    )

# Test the conversation
if __name__ == "__main__":
    # First session
    print("Session 1:")
    response1 = chat_with_history("Hi, I'm Bob!", "123")
    print("Response 1:", response1)
    
    response2 = chat_with_history("What's my name?", "123")
    print("Response 2:", response2)
    
    # New session
    print("\nSession 2:")
    response3 = chat_with_history("What's my name?", "456")
    print("Response 3:", response3)
