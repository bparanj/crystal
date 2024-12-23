from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.messages import trim_messages
from langchain_openai import ChatOpenAI

# Initialize the trimmer
trimmer = trim_messages(
    max_tokens=65,
    strategy="last",
    token_counter=ChatOpenAI(model="gpt-4"),  # Fixed model name from "gpt-4o" to "gpt-4"
    include_system=True,
    allow_partial=False,
    start_on="human",
)

# Create message list
messages = [
    SystemMessage(content="you're a good assistant"),
    HumanMessage(content="hi! I'm bob"),
    AIMessage(content="hi!"),
    HumanMessage(content="I like vanilla ice cream"),
    AIMessage(content="nice"),
    HumanMessage(content="whats 2 + 2"),
    AIMessage(content="4"),
    HumanMessage(content="thanks"),
    AIMessage(content="no problem!"),
    HumanMessage(content="having fun?"),
    AIMessage(content="yes!"),
]

# Trim the messages
result = trimmer.invoke(messages)

# Print each message in the result for better readability
print("\nTrimmed messages:")
for msg in result:
    print(f"{msg.type}: {msg.content}")
