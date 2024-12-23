from typing import TypedDict, Annotated, Sequence, Dict, Any
from langgraph.graph import MessageGraph, StateGraph
from langgraph.prebuilt import ToolNode
from langchain_core.tools import Tool
from uuid import uuid4

# Define the state schema
class State(TypedDict):
    input_text: str
    human_feedback: str | None
    final_output: str | None
    next_step: str

def analyze_data(data: str) -> str:
    """Analyzes input data and returns insights"""
    try:
        return f"Data analysis complete: {data}"
    except Exception as e:
        return f"Error in analysis: {str(e)}"

# Initialize tool
tool = Tool(
    name="analyze_data",
    description="Analyzes input data and returns insights",
    func=analyze_data
)

def initial_processor(state: State) -> Dict[str, Any]:
    """Initial processing to determine path."""
    try:
        text = state["input_text"]
        if "critical_decision" in text.lower():
            return {
                **state,
                "next_step": "human_review",
                "final_output": "Awaiting human review: " + text
            }
        else:
            # Direct analysis without tool node
            analysis_result = analyze_data(text)
            return {
                **state,
                "next_step": "end",
                "final_output": analysis_result
            }
    except Exception as e:
        return {
            **state,
            "next_step": "end",
            "final_output": f"Error in processing: {str(e)}"
        }

def human_processor(state: State) -> Dict[str, Any]:
    """Process human feedback if available."""
    if state["human_feedback"]:
        return {
            **state,
            "next_step": "end",
            "final_output": f"Processed with feedback: {state['human_feedback']}"
        }
    return {
        **state,
        "next_step": "end",
        "final_output": "Awaiting human review"
    }

def router(state: State) -> str:
    """Simple router based on next_step."""
    return state["next_step"]

# Build the graph
workflow = StateGraph(State)

# Add nodes
workflow.add_node("initial", initial_processor)
workflow.add_node("human_review", human_processor)
workflow.add_node("end", lambda x: x)

# Add edges
workflow.add_conditional_edges(
    "initial",
    router,
    {
        "human_review": "human_review",
        "end": "end"
    }
)

workflow.add_conditional_edges(
    "human_review",
    router,
    {
        "end": "end"
    }
)

# Set entry point
workflow.set_entry_point("initial")

# Compile graph
graph = workflow.compile()

def run_workflow(input_text: str, human_feedback: str | None = None) -> Dict[str, Any]:
    """Run the workflow with optional human feedback."""
    try:
        # Create initial state
        state = {
            "input_text": input_text,
            "human_feedback": human_feedback,
            "final_output": None,
            "next_step": "initial"
        }
        
        # Run the graph
        result = graph.invoke(state)
        return result
    except Exception as e:
        print(f"Error in workflow: {str(e)}")
        return {
            "input_text": input_text,
            "human_feedback": human_feedback,
            "final_output": f"Workflow error: {str(e)}",
            "next_step": "end"
        }

def print_result(result: Dict[str, Any]) -> None:
    """Pretty print the workflow result."""
    print(f"Input: {result['input_text']}")
    print(f"Output: {result['final_output']}")
    print("-" * 50)

if __name__ == "__main__":
    print("\nTest 1: Automatic processing")
    result1 = run_workflow("Please analyze this data automatically")
    print_result(result1)
    
    print("\nTest 2: Request requiring human review")
    result2 = run_workflow("This is a critical_decision that needs review")
    print_result(result2)
    
    print("\nTest 3: Providing human feedback")
    result3 = run_workflow(
        "This is a critical_decision that needs review",
        human_feedback="Approved with modifications"
    )
    print_result(result3)

"""
    1. Automatic Processing:
    - Input was regular data for analysis
    - System processed it automatically and returned a completion message
    - No human review was needed

    2. Request Requiring Human Review:
    - Input contained "critical_decision" which triggered human review
    - System correctly identified need for human review
    - Output shows it's awaiting human input, as no feedback was provided

    3. Human Feedback Processing:
    - Same critical decision input
    - Human feedback was provided ("Approved with modifications")
    - System successfully processed the feedback and included it in output

    The workflow is now working as intended with:
    - Correct branching logic (automatic vs human review path)
    - Proper state handling
    - Clear output messages
    - No errors or recursion issues
"""
