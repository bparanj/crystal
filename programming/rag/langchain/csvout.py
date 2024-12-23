from langchain_core.output_parsers import CommaSeparatedListOutputParser

parser = CommaSeparatedListOutputParser()
items = parser.invoke("apple, banana, cherry")
print(items)
