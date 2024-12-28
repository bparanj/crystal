## High Level Steps

### RAG Pipeline

1. Initialize OpenAI API key
2. Load HTML document from the Web
3. Parse the HTML document for title, header and content
4. Split the document using Semantic chunker
5. Generate embeddings for every split using OpenAI embedding model
6. Store the vector embedding and splits in the Chroma database
7. Create a standardized interface for retrieving documents from the vector store.
8. Fetch a pre-made RAG prompt template from LangChain Hub
9. Post processing: Combine all the text content from multiple documents into a single string.
10. Create an LLM instance using ChatOpenAI gpt-4o-mini model
11. Create a pipeline:
		1. Takes a question and retrieves relevant documents
		2. Formats those documents and combines them with the question into a prompt
		3. Sends that prompt to an LLM
		4. Converts the LLM's response to a string

Explain at semantic level: rag_chain_with_source = RunnableParallel(
    {"context": retriever, "question": RunnablePassthrough()}
).assign(answer=rag_chain_from_docs)
be concise and as short as possible.

## Sources

Steps 1, 2, 3, 4, 5, 6, 7, 8, 9 is same as before.

Step 10:

This creates a similar pipeline but starts with pre-retrieved documents instead of doing retrieval. It:

1. Takes documents that were already retrieved and formats them
2. Combines them with the query into a prompt
3. Sends to LLM
4. Converts response to string

The key difference from the previous chain is that document retrieval happens before this chain runs.

Step 11:

This creates a pipeline that runs two parallel operations:
1. Retrieves relevant documents and gets the question
2. Passes those to the previous chain to generate an answer

The result contains both the retrieved context and the generated answer together in the output, allowing you to trace the source documents used.

Step 12:

Question - run the chain
