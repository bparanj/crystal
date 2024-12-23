from typing import Literal, TypedDict, Annotated
from langchain_openai import ChatOpenAI
from pydantic import BaseModel
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage, BaseMessage
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages
import json

class SupervisorDecision(BaseModel):
    next: Literal["researcher", "coder", "FINISH"]

# Define the state structure
class State(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

# Initialize the model
model = ChatOpenAI(model="gpt-4", temperature=0)
supervisor_model = model.with_structured_output(SupervisorDecision)

agents = ["researcher", "coder"]
system_prompt_part_1 = f"""You are a supervisor tasked with managing a conversation between the
following workers: {agents}. Given the following user request,
respond with the worker to act next. Each worker will perform a
task and respond with their results and status. When finished,
respond with FINISH."""

system_prompt_part_2 = f"""Given the conversation above, who should act next? Or should we FINISH? Select one of: {', '.join(agents)}, FINISH"""

def supervisor(state):
    messages = [
        SystemMessage(content=system_prompt_part_1),
        *state["messages"],
        SystemMessage(content=system_prompt_part_2)
    ]
    decision = supervisor_model.invoke(messages)
    return {"next": decision.next}

# Agent implementations
researcher_prompt = """You are a research assistant. Your task is to gather and analyze information about the given topic.
Provide comprehensive research findings and relevant details."""

def researcher(state):
    messages = [
        SystemMessage(content=researcher_prompt),
        *state["messages"]
    ]
    response = model.invoke(messages)  # Use the regular model, not the structured output one
    return {"messages": state["messages"] + [AIMessage(content=response.content)]}

coder_prompt = """You are a coding assistant. Your task is to write, review, or modify code based on the requirements.
Provide clear, efficient, and well-documented code solutions."""

def coder(state):
    messages = [
        SystemMessage(content=coder_prompt),
        *state["messages"]
    ]
    response = model.invoke(messages)  # Use the regular model, not the structured output one
    return {"messages": state["messages"] + [AIMessage(content=response.content)]}

# Build the graph
builder = StateGraph(State)

builder.add_node("supervisor", supervisor)
builder.add_node("researcher", researcher)
builder.add_node("coder", coder)

# Add edges
builder.add_edge(START, "supervisor")
builder.add_conditional_edges(
    "supervisor",
    lambda x: x["next"] if x["next"] != "FINISH" else END
)
builder.add_edge("researcher", "supervisor")
builder.add_edge("coder", "supervisor")

graph = builder.compile()

# Example usage
input_data = {
    "messages": [
        HumanMessage(content="Create a Python function to calculate fibonacci numbers and explain the implementation.")
    ]
}

for output in graph.stream(input_data):
    print(json.dumps({
        'type': 'state_update',
        'data': {k: str(v) for k, v in output.items()}
    }))

# langgraph.errors.GraphRecursionError: Recursion limit of 25 reached without hitting a stop condition. You can increase the limit by setting the `recursion_limit` config key.
# For troubleshooting, visit: https://python.langchain.com/docs/troubleshooting/errors/GRAPH_RECURSION_LIMIT
# python supervisorex.py | jq
