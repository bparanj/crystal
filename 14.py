from langchain.chains import GraphCypherQAChain

graph.refresh_schema()
cypher_chain = GraphCypherQAChain.from_llm(cypher_llm = ChatOpenAI(temperature=0, model_name='gpt-4'), qa_llm = ChatOpenAI(temperature=0), graph=graph, verbose=True)
cypher_chain.run("How many open tickets are there?")

