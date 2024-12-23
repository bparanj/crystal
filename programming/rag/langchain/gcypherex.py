from langchain_openai import ChatOpenAI
from langchain.chains import GraphCypherQAChain
from langchain_community.graphs import Neo4jGraph
from typing import List, Tuple

"""
Install Neo4j Desktop (version 5.24.2)
Create a new project called "testg"
Create a new database called "graphdb"
Install APOC Plugin
Set the password to "password" in the Desktop app
Start the server
"""

class CustomNeo4jGraph(Neo4jGraph):
    @property
    def get_schema(self) -> Tuple[str, str]:
        """Return the schema of the Neo4j database."""
        return self.schema, self.structured_schema

# Initialize Neo4j connection
graph = CustomNeo4jGraph(
    url="bolt://localhost:7687",
    username="neo4j",
    password="password"  # Replace with your actual password
)

# Print current schema
print("Current Database Schema:")
graph.refresh_schema()
print(graph.schema)

# Create some sample ticket data
setup_query = """
MERGE (t1:Ticket {id: 1, status: 'open', title: 'First ticket'})
MERGE (t2:Ticket {id: 2, status: 'open', title: 'Second ticket'})
MERGE (t3:Ticket {id: 3, status: 'closed', title: 'Third ticket'})
"""

# Execute the setup query
graph.query(setup_query)

# Refresh schema after creating data
graph.refresh_schema()

# Initialize the LLM
llm = ChatOpenAI(model="gpt-4", temperature=0)

# Create the chain
chain = GraphCypherQAChain.from_llm(
    llm=llm,
    graph=graph,
    verbose=True,
    return_direct=True,
    allow_dangerous_requests=True
)

# Run the query
print("\nQuerying for open tickets:")
response = chain.invoke("How many open tickets are there?")
print("\nResponse:", response)