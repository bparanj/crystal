from langchain_core.messages import (
  AIMessage,
  HumanMessage, 
  SystemMessage,
  filter_messages
)
from langchain_openai import ChatOpenAI

messages = [
  SystemMessage(content="you are a good assistant", id="1"),
  HumanMessage(content="example input", id="2", name="example_user"),
  AIMessage(content="example output", id="3", name="example_assistant"),
  HumanMessage(content="real input", id="4", name="bob"), 
  AIMessage(content="real output", id="5", name="alice")
]

# Filter only human messages
print("\n1. Filter only human messages:")
human_messages = filter_messages(messages, include_types=["human"])
for msg in human_messages:
   print(f"Type: {msg.__class__.__name__}, Content: {msg.content}, Name: {msg.name}, ID: {msg.id}")

# Filter by excluding example names
print("\n2. Filter by excluding example names:")
filtered_by_name = filter_messages(messages, exclude_names=["example_user", "example_assistant"])
for msg in filtered_by_name:
   print(f"Type: {msg.__class__.__name__}, Content: {msg.content}, Name: {getattr(msg, 'name', 'N/A')}, ID: {msg.id}")

# Filter by message types and exclude specific ID
print("\n3. Filter by message types and exclude ID 3:")
filtered_by_type_and_id = filter_messages(messages, include_types=[HumanMessage, AIMessage], exclude_ids=["3"])
for msg in filtered_by_type_and_id:
   print(f"Type: {msg.__class__.__name__}, Content: {msg.content}, Name: {msg.name}, ID: {msg.id}")

# Create chain with filter
model = ChatOpenAI()
filter_ = filter_messages(exclude_names=["example_user", "example_assistant"])
chain = filter_ | model

# Test the chain
response = chain.invoke(messages)
print("\n4. Chain response after filtering:")
print(response)
