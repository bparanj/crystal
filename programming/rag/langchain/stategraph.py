from typing import Annotated, TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_openai import ChatOpenAI 
from langchain.schema import HumanMessage, AIMessage
from langchain.schema.messages import BaseMessage
from langgraph.checkpoint.memory import MemorySaver

class State(TypedDict):
    messages: Annotated[list, add_messages]

builder = StateGraph(State)
model = ChatOpenAI()

# Keep track of all messages
message_history = []

def chatbot(state: State):
    """Add a chatbot node"""
    # Add new message to history
    message_history.extend(state["messages"])
    # Use entire message history for context
    response = model.invoke(message_history)
    if isinstance(response, BaseMessage):
        message_history.append(response)
        return {"messages": [response]}
    return {"messages": [AIMessage(content=str(response))]}

builder.add_node("chatbot", chatbot)
builder.add_edge(START, 'chatbot')
builder.add_edge('chatbot', END)

graph = builder.compile()

# First interaction
result_1 = graph.invoke({
    "messages": [HumanMessage(content='hi, my name is Bugs Bunny')]
})

for message in result_1["messages"]:
    if isinstance(message, HumanMessage):
        print("Human:", message.content)
    elif isinstance(message, AIMessage):
        print("Assistant:", message.content)

# Second interaction using the established context
result_2 = graph.invoke({
    "messages": [HumanMessage(content='what is my name?')]
})

for message in result_2["messages"]:
    if isinstance(message, HumanMessage):
        print("Human:", message.content)
    elif isinstance(message, AIMessage):
        print("Assistant:", message.content)
