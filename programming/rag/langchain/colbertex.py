from ragatouille import RAGPretrainedModel
import requests
import os
import torch

# Force CPU usage : This is still looking for GPU
os.environ['CUDA_VISIBLE_DEVICES'] = ''
torch.cuda.is_available = lambda: False

# Initialize RAG model
RAG = RAGPretrainedModel.from_pretrained("colbert-ir/colbertv2.0")

def get_wikipedia_page(title: str):
    """
    Retrieve the full text content of a Wikipedia page.
    :param title: str - Title of the Wikipedia page.
    :return: str - Full text content of the page as raw string.
    """
    URL = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "titles": title,
        "prop": "extracts",
        "explaintext": True,
    }
    headers = {"User-Agent": "RAGatouille_tutorial/0.0.1 (ben@clavie.eu)"}
    response = requests.get(URL, params=params, headers=headers)
    data = response.json()
    page = next(iter(data["query"]["pages"].values()))
    return page["extract"] if "extract" in page else None

# Get the document
full_document = get_wikipedia_page("Hayao_Miyazaki")

# Create an index
RAG.index(
    collection=[full_document],
    index_name="Miyazaki-123",
    max_document_length=180,
    split_documents=True
)

# Query
results = RAG.search(query="What animation studio did Miyazaki found?", k=3)
print(results)

# Use as langchain retriever
retriever = RAG.as_langchain_retriever(k=3)
response = retriever.invoke("What animation studio did Miyazaki found?")
print(response)
