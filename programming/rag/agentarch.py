import ast
import json
import operator

from langchain_core.messages import HumanMessage
from typing import Annotated, TypedDict
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langgraph.graph import START, StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition

# Supported operators
OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
}

@tool
def calculator(query: str) -> str:
    """A simple calculator tool. Input should be a mathematical expression."""
    try:
        # Parse the query into an AST
        tree = ast.parse(query, mode='eval')
        
        # Ensure the expression is safe
        if not all(isinstance(node, (ast.Expression, ast.BinOp, ast.Num, ast.UnaryOp)) for node in ast.walk(tree)):
            return "Error: Unsupported or unsafe expression."

        # Evaluate the AST
        result = evaluate(tree.body)
        return str(result)
    except Exception as e:
        return f"Error: {e}"

def evaluate(node):
    """Evaluate a safe AST node."""
    if isinstance(node, ast.BinOp):  # Binary operation
        left = evaluate(node.left)
        right = evaluate(node.right)
        return OPERATORS[type(node.op)](left, right)
    elif isinstance(node, ast.UnaryOp):  # Unary operation
        operand = evaluate(node.operand)
        if isinstance(node.op, ast.UAdd):  # Unary +
            return +operand
        elif isinstance(node.op, ast.USub):  # Unary -
            return -operand
    elif isinstance(node, ast.Num):  # Number
        return node.n
    else:
        raise ValueError(f"Unsupported expression: {node}")

search = DuckDuckGoSearchRun()
tools = [search, calculator]
model = ChatOpenAI(temperature=0.1).bind_tools(tools)

class State(TypedDict):
    messages: Annotated[list, add_messages]

def model_node(state: State) -> State:
    res = model.invoke(state["messages"])
    return {"messages": res}

builder = StateGraph(State)
builder.add_node("model", model_node)
builder.add_node("tools", ToolNode(tools))
builder.add_edge(START, "model")
builder.add_conditional_edges("model", tools_condition)
builder.add_edge("tools", "model")
graph = builder.compile()

input = {
  "messages": [
    HumanMessage("How old was the 30th president of the United States when he died?")
  ]
}

def serialize(obj):
    """Custom serializer for non-JSON-serializable objects."""
    if hasattr(obj, "__dict__"):  # For objects with attributes
        return obj.__dict__
    else:
        return str(obj)  # Fallback for objects without __dict__

for c in graph.stream(input):
    try:
        print(json.dumps(c, indent=4, default=serialize))
    except TypeError as e:
        print(f"Error serializing object: {e}")
        print(c)

# To add color, run this program with: python agentarch.py | jq