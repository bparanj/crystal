from langchain_core.messages import (
   AIMessage,
   HumanMessage,
   SystemMessage,
   merge_message_runs,
)
from langchain_openai import ChatOpenAI

messages = [
   SystemMessage(content="you're a good assistant."),
   SystemMessage(content="you always respond with a joke."),
   HumanMessage(content="i wonder why it's called langchain"),
   HumanMessage(content="and who is harrison chasing anyways"),
   AIMessage(content='Well, I guess they thought "WordRope" and "SentenceString" just didn\'t have the same ring to it!'),
   AIMessage(content="Why, he's probably chasing after the last cup of coffee in the office!")
]

model = ChatOpenAI()
merger = merge_message_runs()
chain = merger | model

response = chain.invoke(messages)
print(f"{response.__class__.__name__.replace('Message', '')}: {response.content}")
