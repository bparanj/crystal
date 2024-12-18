from langchain.chains.query_constructor.base import AttributeInfo
from langchain.retrievers.self_query.base import SelfQueryRetriever
from langchain_openai import OpenAI, OpenAIEmbeddings
from langchain_postgres.vectorstores import PGVector
from langchain_core.documents import Document
from lark import lark

# pip install lark langchain langchain-openai psycopg2-binary langchain-postgres

# Define the metadata fields
fields = [
    AttributeInfo(
        name="genre",
        description="The genre of the movie",
        type="string or list[string]",
    ),
    AttributeInfo(
        name="year",
        description="The year the movie was released",
        type="integer"
    ),
    AttributeInfo(
        name="director",
        description="The name of the movie director",
        type="string"
    ),
    AttributeInfo(
        name="rating",
        description="A 1-10 rating for the movie",
        type="float"
    )
]

# Create sample movie documents with metadata
movies = [
    Document(
        page_content="A group of thieves plan an elaborate heist in a dream world.",
        metadata={
            "genre": ["sci-fi", "action"],
            "year": 2010,
            "director": "Christopher Nolan",
            "rating": 8.8
        }
    ),
    Document(
        page_content="Two mafia families fight for control of organized crime in New York.",
        metadata={
            "genre": "crime",
            "year": 1972,
            "director": "Francis Ford Coppola",
            "rating": 9.2
        }
    ),
    Document(
        page_content="A tale of rebellion against an authoritarian regime in a dystopian future.",
        metadata={
            "genre": ["sci-fi", "drama"],
            "year": 1984,
            "director": "Michael Radford",
            "rating": 7.2
        }
    ),
    Document(
        page_content="A boy befriends a gentle giant who eats dreams and captures nightmares.",
        metadata={
            "genre": ["fantasy", "family"],
            "year": 2016,
            "director": "Steven Spielberg",
            "rating": 6.9
        }
    )
]

# Initialize PostgreSQL vector store
embeddings = OpenAIEmbeddings()
connection_string = 'postgresql+psycopg://langchain:langchain@localhost:6024/langchain'

# Create a new collection name for movies
COLLECTION_NAME = "movie_collection"

# Initialize the vector store with the movies
db = PGVector.from_documents(
    documents=movies,
    embedding=embeddings,
    collection_name=COLLECTION_NAME,
    connection=connection_string,
)

# Set up the retriever
description = "Brief summary of a movie"
llm = OpenAI(temperature=0)
retriever = SelfQueryRetriever.from_llm(
    llm=llm,
    vectorstore=db,
    document_contents=description,
    metadata_field_info=fields,
    verbose=True
)

def search_movies(query):
    """
    Search for movies using natural language queries that can reference both content and metadata.
    
    Args:
        query (str): Natural language query about movies
        
    Returns:
        list: Matching movie documents
    """
    try:
        docs = retriever.invoke(query)
        return docs
    except Exception as e:
        print(f"Error during search: {str(e)}")
        return []

# Example queries to demonstrate different search capabilities
example_queries = [
    "Find sci-fi movies with a rating above 8",
    "What movies were directed by Christopher Nolan?",
    "Show me movies released after 2000 that are in the fantasy genre",
    "Find crime movies from the 1970s",
]

def clear_collection():
    """
    Clear the existing collection from the database if it exists.
    """
    try:
        PGVector.drop_collection(
            collection_name=COLLECTION_NAME,
            connection_string=connection_string
        )
        print(f"Collection {COLLECTION_NAME} cleared successfully")
    except Exception as e:
        print(f"Error clearing collection: {str(e)}")

if __name__ == "__main__":
    # Optionally clear existing collection before adding new documents
    # clear_collection()
    
    print("Running example queries...\n")
    for query in example_queries:
        print(f"Query: {query}")
        results = search_movies(query)
        print(f"Found {len(results)} matching movies:")
        for doc in results:
            print(f"\nSummary: {doc.page_content}")
            print(f"Metadata: {doc.metadata}\n")
        print("-" * 50)