from langgraph.graph import START, StateGraph
from typing import TypedDict

class State(TypedDict):
    foo: str  # this key is shared with the subgraph

class SubgraphState(TypedDict):
    foo: str  # this key is shared with the parent graph
    bar: str

# Define subgraph
def subgraph_node(state: SubgraphState):
    # The subgraph node communicates with the parent graph via the shared "foo" key
    return {"foo": state["foo"] + "bar", "bar": "baz"}  # Update "foo" and provide a new "bar"

subgraph_builder = StateGraph(SubgraphState)
subgraph_builder.add_node("subgraph_node", subgraph_node)
subgraph_builder.add_edge(START, "subgraph_node")
subgraph = subgraph_builder.compile()

# Define parent graph
def parent_node(state: State):
    # Pass the "foo" key to the subgraph
    return {"foo": state["foo"]}

builder = StateGraph(State)
builder.add_node("parent_node", parent_node)
builder.add_node("subgraph", subgraph)
builder.add_edge(START, "parent_node")
builder.add_edge("parent_node", "subgraph")

graph = builder.compile()

# Example usage
state = {"foo": "foo"}
for result in graph.stream(state):
    print(result)
