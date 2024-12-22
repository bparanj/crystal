import json
from typing import Annotated, TypedDict
from langchain_core.messages import (
    AIMessage,
    BaseMessage,
    HumanMessage,
    SystemMessage,
)
from langchain_openai import ChatOpenAI
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages

# Initialize the model
model = ChatOpenAI()

# Define the state structure
class State(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

# System prompt for generating essays
generate_prompt = SystemMessage(
    "You are an essay assistant tasked with writing excellent 3-paragraph essays."
    " Generate the best essay possible for the user's request."
    " If the user provides critique, respond with a revised version of your previous attempts."
)

# Function to generate the essay or revised version
def generate(state: State) -> State:
    answer = model.invoke([generate_prompt] + state["messages"])
    return {"messages": state["messages"] + [answer]}  # Append the generated message

# System prompt for critiquing essays
reflection_prompt = SystemMessage(
    "You are a teacher grading an essay submission. Generate critique and recommendations for the user's submission."
    " Provide detailed recommendations, including requests for length, depth, style, etc."
)

# Function to critique the essay
def reflect(state: State) -> State:
    # Invert the messages for reflection
    cls_map = {AIMessage: HumanMessage, HumanMessage: AIMessage}
    translated = [reflection_prompt, state["messages"][0]] + [
        cls_map[msg.__class__](content=msg.content) for msg in state["messages"][1:]
    ]
    answer = model.invoke(translated)
    # Treat the critique as human feedback for the generator
    return {"messages": state["messages"] + [HumanMessage(content=answer.content)]}

# Function to decide if the process should continue
def should_continue(state: State):
    if len(state["messages"]) > 6:
        # Stop after 3 iterations (each having 2 messages: essay and critique)
        return END
    else:
        return "reflect"

# Build the state graph
builder = StateGraph(State)
builder.add_node("generate", generate)
builder.add_node("reflect", reflect)
builder.add_edge(START, "generate")
builder.add_conditional_edges("generate", should_continue)
builder.add_edge("reflect", "generate")
graph = builder.compile()

# Example input to start the process
input_data = {
    "messages": [
        HumanMessage(content="Write an essay on the benefits of renewable energy.")
    ]
}

# Run the graph
state = {"messages": input_data["messages"]}

import json

def message_to_dict(msg):
    return {
        'type': msg.__class__.__name__,
        'content': msg.content,
        **{k: v for k, v in msg.__dict__.items() if k not in ['content']}
    }

# Run the graph
for output in graph.stream(state):
    state_dict = {
        key: {'messages': [message_to_dict(msg) for msg in value['messages']]}
        for key, value in output.items()
    }
    print(json.dumps(state_dict))

# python reflectionex.py | jq
