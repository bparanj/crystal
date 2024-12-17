from langchain_text_splitters import CharacterTextSplitter

loader = TextLoader("./test.txt")
docs = loader.load()
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splitted_docs = splitter.split_documents(docs)

