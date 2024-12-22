from typing import TypedDict
from langgraph.graph import START, StateGraph

# Define the parent graph state
class State(TypedDict):
    foo: str

# Define the subgraph state
class SubgraphState(TypedDict):
    # None of these keys are shared with the parent graph state
    bar: str
    baz: str

# Define subgraph node
def subgraph_node(state: SubgraphState):
    return {"bar": state["bar"] + "baz"}

# Build the subgraph
subgraph_builder = StateGraph(SubgraphState)
subgraph_builder.add_node("subgraph_node", subgraph_node)
subgraph_builder.add_edge(START, "subgraph_node")
subgraph = subgraph_builder.compile()

# Define a node in the parent graph
def node(state: State):
    # Transform the state to the subgraph state
    response = subgraph.invoke({"bar": state["foo"]})
    # Transform response back to the parent state
    return {"foo": response["bar"]}

# Build the parent graph
builder = StateGraph(State)
# Note that we are using `node` function instead of a compiled subgraph
builder.add_node("node", node)
builder.add_edge(START, "node")
graph = builder.compile()

# Example usage
state = {"foo": "foo"}
for result in graph.stream(state):
    print(result)
