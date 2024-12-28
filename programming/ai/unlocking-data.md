## High Level Steps

### RAG Pipeline

- Initialize OpenAI API key
- Load HTML document from the Web
- Parse the HTML document for title, header and content
- Split the document using Semantic chunker
- Generate embeddings for every split using OpenAI embedding model
- Store the vector embedding and splits in the Chroma database
- Create a standardized interface for retrieving documents from the vector store.
- Fetch a pre-made RAG prompt template from LangChain Hub
- Post processing: Combine all the text content from multiple documents into a single string.
- Create an LLM instance using ChatOpenAI gpt-4o-mini model
- Create a pipeline:
		1. Takes a question and retrieves relevant documents
		2. Formats those documents and combines them with the question into a prompt
		3. Sends that prompt to an LLM
		4. Converts the LLM's response to a string

Explain at semantic level: 
be concise and as short as possible.
