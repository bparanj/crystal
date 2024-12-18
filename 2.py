from langchain.indexes import SQLRecordManager, index

record_manager = SQLRecordManager(namespace, db_url="postgresql+psyscopg://langchain:langchain@localhost:6024/langchain")

# Create the schema if it doesn't exist
record_manager.create_schema()
index(
    [doc1Updated, doc2],
    record_manager,
    vectorstore,
    cleanup='incremental')
