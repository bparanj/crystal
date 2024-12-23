from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.agents import create_openai_functions_agent
from langchain.agents import AgentExecutor
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.tools import tool
import asyncio

@tool
def search_president_facts(query: str) -> str:
    """Search for facts about US presidents"""
    return """Calvin Coolidge was the 30th president of the United States. 
    He died on January 5, 1933 at the age of 60 in Northampton, Massachusetts."""

model = ChatOpenAI(
    model="gpt-4",
    temperature=0,
    streaming=True
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that answers questions about US Presidents."),
    MessagesPlaceholder(variable_name="messages"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

tools = [search_president_facts]
agent = create_openai_functions_agent(model, tools, prompt)
app = AgentExecutor(agent=agent, tools=tools, verbose=True)

async def main():
    input_data = {
        "messages": [
            HumanMessage(content="How old was the 30th president of the United States when he died?")
        ]
    }
    
    output = app.astream_events(input_data, version="v2")
    print("\nSearching for information...\n")
    
    async for event in output:
        event_type = event.get("event", "")
        event_data = event.get("data", {})
        
        if event_type == "on_tool_start":
            print(f"Using tool: {event_data.get('input', {}).get('query', 'unknown')}")
        elif event_type == "on_tool_end":
            print(f"\nFound: {event_data.get('output', 'No results')}\n")
        elif event_type == "on_chat_model_stream":
            if chunk := event_data.get("chunk"):
                if content := chunk.content:
                    print(content, end="")
    
    print("\nSearch complete.")

if __name__ == "__main__":
    asyncio.run(main())