# pip install pypdf

from langchain_community.document_loaders import PyPDFLoader

# Create loader instance
loader = PyPDFLoader("./lev-triz.pdf")

# Load all pages
pages = loader.load()

# Print content of each page along with its page number
for i, page in enumerate(pages):
    print(f"\nPage {i+1}:")
    print("="*50)
    print(page.page_content)
    
    # Optionally, print metadata for each page
    print("\nMetadata:")
    print(page.metadata)
    print("="*50 + "\n")
