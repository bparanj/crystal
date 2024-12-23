import sqlite3
from langchain_community.tools import QuerySQLDatabaseTool  # Updated import
from langchain_community.utilities import SQLDatabase
from langchain.chains import create_sql_query_chain
from langchain_openai import ChatOpenAI

# First, let's download the Chinook database if it doesn't exist
def setup_chinook_database():
    """Download and setup the Chinook database if it doesn't exist"""
    import urllib.request
    import os
    
    if not os.path.exists("Chinook.db"):
        print("Downloading Chinook database...")
        url = "https://raw.githubusercontent.com/lerocha/chinook-database/master/ChinookDatabase/DataSources/Chinook_Sqlite.sqlite"
        urllib.request.urlretrieve(url, "Chinook.db")
        print("Database downloaded successfully!")

# Setup the database
setup_chinook_database()

# Initialize components
db = SQLDatabase.from_uri("sqlite:///Chinook.db")
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# Create the chain components
write_query = create_sql_query_chain(llm, db)
execute_query = QuerySQLDatabaseTool(db=db)

# Combine into a single chain
chain = write_query | execute_query

def query_database(question: str):
    """
    Query the database using natural language.
    
    Args:
        question (str): Natural language question about the database
        
    Returns:
        str: The query results
    """
    try:
        result = chain.invoke({"question": question})
        return result
    except Exception as e:
        return f"Error executing query: {str(e)}"

def get_table_info():
    """Get information about all tables in the database"""
    conn = sqlite3.connect("Chinook.db")
    cursor = conn.cursor()
    
    # Get all table names
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    table_info = {}
    for (table_name,) in tables:
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()
        table_info[table_name] = [
            f"{col[1]} ({col[2]})" for col in columns
        ]
    
    conn.close()
    return table_info

# Example queries demonstrating different aspects of the Chinook database
example_queries = [
    "How many tracks are there in the database?",
    "What are the top 5 selling artists?",
    "List all albums by Artist 'Queen'",
    "What is the total sales amount for each country?",
    "Who are the employees with the title 'Sales Support Agent'?"
]

if __name__ == "__main__":
    print("Chinook Database Query System\n")
    
    # Print database tables and schema for reference
    print("Database Schema:")
    table_info = get_table_info()
    for table_name, columns in table_info.items():
        print(f"\nTable: {table_name}")
        print("Columns:")
        for column in columns:
            print(f"  - {column}")
    print("\n" + "="*50 + "\n")
    
    # Run example queries
    print("Running example queries:\n")
    for question in example_queries:
        print(f"Question: {question}")
        result = query_database(question)
        print(f"Result: {result}\n")
        print("-"*50 + "\n")
    
    # Interactive mode
    print("\nEnter your own questions (type 'exit' to quit):")
    while True:
        question = input("\nYour question: ")
        if question.lower() == 'exit':
            break
        result = query_database(question)
        print(f"\nResult: {result}")
