from typing import Literal, TypedDict, Annotated
from langchain_openai import ChatOpenAI
from pydantic import BaseModel
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage, BaseMessage
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages

# This is different from the book because this is not using duckduckgo search. Still demonstrates the intermediate output
class SupervisorDecision(BaseModel):
    next: Literal["researcher", "fact_checker", "FINISH"]

class State(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]
    steps: int

# Initialize model
model = ChatOpenAI(model="gpt-4", temperature=0)
supervisor_model = model.with_structured_output(SupervisorDecision)

def supervisor(state):
    print("Supervisor thinking...")  # Debug print
    if state["steps"] >= 5:
        return {"next": "FINISH"}
    
    messages = [
        SystemMessage(content="You are a supervisor. Direct between: researcher (gets info), fact_checker (verifies), or FINISH (when done)."),
        *state["messages"]
    ]
    decision = supervisor_model.invoke(messages)
    print(f"Supervisor decided: {decision.next}")  # Debug print
    return {"next": decision.next}

def researcher(state):
    print("Researcher working...")  # Debug print
    messages = [
        SystemMessage(content="Research assistant: Find facts about US presidents."),
        *state["messages"]
    ]
    response = model.invoke(messages)
    print(f"Researcher response: {response.content}")  # Debug print
    return {
        "messages": state["messages"] + [AIMessage(content=response.content)],
        "steps": state["steps"] + 1
    }

def fact_checker(state):
    print("Fact checker working...")  # Debug print
    messages = [
        SystemMessage(content="Fact checker: Verify presidential information."),
        *state["messages"]
    ]
    response = model.invoke(messages)
    print(f"Fact checker response: {response.content}")  # Debug print
    return {
        "messages": state["messages"] + [AIMessage(content=response.content)],
        "steps": state["steps"] + 1
    }

# Build graph
builder = StateGraph(State)
builder.add_node("supervisor", supervisor)
builder.add_node("researcher", researcher)
builder.add_node("fact_checker", fact_checker)

# Add edges
builder.add_edge(START, "supervisor")
builder.add_conditional_edges(
    "supervisor",
    lambda x: x["next"] if x["next"] != "FINISH" else END
)
builder.add_edge("researcher", "supervisor")
builder.add_edge("fact_checker", "supervisor")

# Compile graph
graph = builder.compile()

# Run with debug prints
print("Starting graph execution...")  # Debug print
input_data = {
    "messages": [
        HumanMessage(content="How old was the 30th president of the United States when he died?")
    ],
    "steps": 0
}

try:
    for output in graph.stream(input_data):
        print("\nGraph output:", output)  # Print raw output
        if isinstance(output, dict):
            if 'messages' in output:
                print("\nMessage update:")
                for msg in output['messages']:
                    if isinstance(msg, AIMessage):
                        print(f"AI: {msg.content}")
            if 'next' in output:
                print(f"\nNext step: {output['next']}")
except Exception as e:
    print(f"Error occurred: {str(e)}")

print("Graph execution completed.")  # Debug print
