from langchain_community.tools.sql_database.tool import QuerySQLDataBaseTool
from langchain_community.utilities import SQLDatabase
from langchain.chains import create_sql_query_chain
from langchain_openai import ChatOpenAI

# replate this with the connection details of your db
db = SQLDatabase.from_uri("sqlite:///Chinook.db")
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
# convert question to sql query
write_query = create_sql_query_chain(llm, db)
# Execute sql query
execute_query = QuerySQLDataBaseTool(db=db)
# combined
chain = write_query | execute_query

