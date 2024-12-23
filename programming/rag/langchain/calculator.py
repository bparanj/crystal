import ast
import operator
from langchain_core.tools import tool

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
