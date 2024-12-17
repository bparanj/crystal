from langchain_openai import OpenAIEmbeddings

model = OpenAIEmbeddings()
embeddings = model.embed_documents([
    "Hi there!", 
    "Oh, hello!", 
    "What's your name?", 
    "My friends call me world", 
    "Hello World!"])
print(embeddings)
