import asyncio
from contextlib import aclosing
from typing import Dict, List, Any
from langchain.schema import HumanMessage
from langchain_neo4j import Neo4jGraph

# NOT WORKING
async def process_stream(graph: Any, input_data: Dict[str, List[Any]], config: Dict[str, Any]) -> None:
    """
    Process a stream of chunks with event-based cancellation support.
    """
    event = asyncio.Event()
    
    try:
        async with aclosing(graph.astream(input_data, config)) as stream:
            async for chunk in stream:
                if event.is_set():
                    print("Stream cancelled")
                    break
                print(f"Received chunk: {chunk}")  # Debug print
                
                if isinstance(chunk, dict):
                    if 'type' in chunk:
                        if chunk['type'] == 'text':
                            print(f"Text: {chunk['text']}")
                        elif chunk['type'] == 'error':
                            print(f"Error: {chunk['error']}")
                    else:
                        print(f"Raw chunk: {chunk}")
                else:
                    print(f"Non-dict chunk: {chunk}")
    except Exception as e:
        print(f"Stream processing error: {str(e)}")
        raise

async def main():
    # Initialize your graph
    graph = Neo4jGraph(
        url="bolt://localhost:7687",
        username="neo4j",
        password="password"
    )
    
    input_data = {
        "messages": [
            HumanMessage("How old was the 30th president of the United States when he died?")
        ]
    }
    config = {"configurable": {"thread_id": "1"}}

    print("Starting stream processing...")
    await process_stream(graph, input_data, config)
    print("Stream processing completed")

if __name__ == "__main__":
    asyncio.run(main())