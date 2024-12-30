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

Run the chain with user query

## RAG Pipeline Review

Steps 1 to 10 is the same as first one.

Step 11:

This code creates a RAG (Retrieval Augmented Generation) pipeline where:
1. Two parallel inputs are processed: retrieved documents (formatted via `format_docs`) and the user's question (passed through unchanged)
2. These inputs are fed into a prompt template
3. The populated prompt goes to a language model (llm)
4. The LLM's response is converted to a string

Think of it as: get relevant docs → combine with question → generate answer → format output.

## Security API Key

Uses dotenv instead of using environment variable for the API key.

This RAG pipeline: formats retrieved documents → combines them with a prompt → sends to LLM → formats output as string. The key difference from the previous version is it assumes documents are already retrieved and just need formatting.

## Common Vectorization Techniques

1. Initialize OpenAI API key
2. Create embedding function using OpenAI
3. Create embedding for user query
4. Load document from the Web
5. Split the document using Semantic chunker
6. Extract the text content from the splits
7. Create a TF-IDF vectorizer
8. Generate TF-IDF matrix
9. Get the vocabulary, term frequencies, and corresponding IDF values
10. Create a list of tuples containing word, TF, and IDF values
11. Sort the list by IDF values in descending order
12. Print the grid of top 10 words, TF, and IDF values

TD-IDF scoring for user query

- User query embedding
- Calculate cosine similarity between the new content and the original documents
- Find the index of the document with the highest similarity score
- Print the text of the top document


Creating and Saving doc2vec model:

- Extract the text content from the splits
- Tokenize the documents
- Create tagged documents for Doc2Vec
- Train the Doc2Vec model
- Try it with 1536D vectors
- Save the trained model to a file

Using doc2vec saved model

- Load the saved model
- Calculate the document vectors
- User query for embedding
- Tokenize the new content
- Infer the vector for the new content
- Calculate cosine similarity between the new content vector and the document vectors
- Find the index of the document with the highest similarity score
- Print the text of the top document


Using BERT

- Extract the text content from the splits
- Load BERT tokenizer and model
- Get the vector size of the BERT embeddings
- Tokenize the documents
- Calculate the document embeddings
- New content (question) for embedding
- Tokenize the new content
- Calculate the embedding for the new content
- Calculate cosine similarity between the new content embedding and the document embeddings
- Find the index of the document with the highest similarity score
- Print the text of the top document
- Embed the splits
- Create a retriever for the vector store
- Print the retrieved document

Retrieval and Generation

- Use a RAG prompt from hub
- Create a relevance prompt template to check relevance. It has question and retrieved context variables. Relevance score seems to be an output variable (value is not provided)
- Post processing - format the docs by joining each document with two new lines
- Extract relevance score and if it falls below a certain value, say: I don't know.

RAG Chain from Docs

This RAG pipeline has three main steps:

1. Format retrieved documents (like before)
2. Run two parallel processes:
   - Score document relevance to question using LLM
   - Generate answer from documents using LLM
3. Apply conditional logic to final answer based on relevance score

End result: provides quality-controlled answers by considering document relevance.

RAG Chain with Source:

This chain combines two operations in sequence:
1. Parallel retrieval of documents and passing through the question
2. Feed both into the previous `rag_chain_from_docs` pipeline to get quality-controlled answers with sources

It's adding document retrieval as the first step before the previous chain.

Send the user query to the RAG chain with source.
Print the relevance score and the answer to the question.

## Distance Metrics

- Encode sentences
- Print embeddings
- Calculate Euclidean distance and print the values
- Print dot product
- Print cosine distance

## Hybrid Custom

- Extract text from PDF file
- Split the text into chunks with overlap
- Create Document objects from text splits. Document contains the text content and a numbered ID as metadata.

Create a Chroma vector database:

1. Initialize a ChromaDB client
2. Converting documents to vector embeddings
3. Store them in a named collection for later similarity search

- Create dense retriever
- Create sparse retriever

Define a custom hybrid search function (as opposed to using LangChain EnsembleRetriever)

Step 1: Retrieve the top-k documents from both dense search and sparse search.

Combine the document IDs and remove duplicates
Create dictionaries to store the reciprocal ranks

Step 2: Calculate the reciprocal rank for each document in dense and sparse search results.
Step 3: Sum the reciprocal ranks for each document.
Step 4: Sort the documents based on their combined reciprocal rank scores.
Step 5: Retrieve the documents based on the sorted document IDs.
Step 6: Return the final ranked and sorted list, truncated by the top-k parameter

Retrieval and Generation

- Relevance check prompt (same as previous notebook)
- Post processing: Format docs
- Extract score and check for relevance score to map to "I don't know"

Pipeline steps:

1. Format docs
2. Parallel processing:
   - Check relevance: question + context → LLM score
   - Generate answer: question + context → LLM response
3. Apply conditional logic based on relevance score

Result: Quality-controlled answer based on document relevance.

Parallel execution: 

Retrieves relevant docs via hybrid search + passes question through, then feeds both into previous RAG pipeline for quality-controlled answer generation.

Send the user query to RAG
Print the relevance score, answer and retrieved docs

## Hybrid Ensemble

...






Explain at a semantic level: 

be concise and as short as possible.






















































Start on this after finishing the Unlocking Data:

https://github.com/Denis2054/RAG-Driven-Generative-AI/blob/main/Chapter01/RAG_Overview.ipynb

















