from langchain_community.document_loaders import TextLoader

# Create loader instance
loader = TextLoader("./test.txt")

# Load the documents
documents = loader.load()

# Print the content of the documents
for doc in documents:
    print(doc.page_content)