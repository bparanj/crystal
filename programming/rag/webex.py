from langchain_community.document_loaders import WebBaseLoader

# Create loader instance
loader = WebBaseLoader("https://www.langchain.com/")

# Load the documents and store them in a variable
documents = loader.load()

# Print the content of each document
for doc in documents:
    print(doc.page_content)
    print("\n" + "="*50 + "\n")  # Separator between documents

for doc in documents:
    print("Content:", doc.page_content)
    print("Metadata:", doc.metadata)
    print("\n" + "="*50 + "\n")
