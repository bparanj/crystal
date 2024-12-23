from langchain_core.messages import (
   AIMessage,
   HumanMessage,
   SystemMessage,
   merge_message_runs,
)

messages = [
   SystemMessage("you're a good assistant."),
   SystemMessage("you always respond with a joke."),
   HumanMessage([{"type": "text", "text": "i wonder why it's called langchain"}]),
   HumanMessage("and who is harrison chasing anyways"),
   AIMessage(
       'Well, I guess they thought "WordRope" and "SentenceString" just didn\'t have the same ring to it!'
   ),
   AIMessage("Why, he's probably chasing after the last cup of coffee in the office!"),
]

merged_messages = merge_message_runs(messages)
for message in merged_messages:
   role = message.__class__.__name__.replace('Message', '')
   print(f"{role}: {message.content}")
