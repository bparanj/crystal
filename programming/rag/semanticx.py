from langchain.utils.math import cosine_similarity
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import chain
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

# Two prompts for different types of questions
physics_template = """You are a very smart physics professor. You are great at answering questions about physics in a concise and easy to understand manner. When you don't know the answer to a question you admit that you don't know.

Here is a question:
{question}"""

math_template = """You are a very good mathematician. You are great at answering math questions. You are so good because you are able to break down hard problems into their component parts, answer the component parts, and then put them together to answer the broader question.

Here is a question:
{question}"""

# Initialize embeddings model
embeddings = OpenAIEmbeddings()

# Create list of prompt templates and embed them
prompt_templates = [physics_template, math_template]
prompt_embeddings = embeddings.embed_documents(prompt_templates)

# Router chain that selects the appropriate prompt based on query similarity
@chain
def prompt_router(question: str):
    # Embed the input question
    query_embedding = embeddings.embed_query(question)
    # Compute similarity between question and each prompt template
    similarity = cosine_similarity([query_embedding], prompt_embeddings)[0]
    # Select the most similar prompt template
    most_similar = prompt_templates[similarity.argmax()]
    return PromptTemplate.from_template(most_similar)

# Create the full chain: router -> LLM -> output parser
semantic_router = (
    prompt_router 
    | ChatOpenAI(temperature=0) 
    | StrOutputParser()
)

# Example usage
def route_and_answer_question(question):
    """
    Routes a question to the appropriate expert and returns the answer.
    
    Args:
        question (str): The question to be answered
    
    Returns:
        str: The expert's response
    """
    try:
        # Pass the question directly
        response = semantic_router.invoke(question)
        return response
    except Exception as e:
        return f"Error processing question: {str(e)}"

# Example questions
questions = [
    "What is the relationship between force, mass, and acceleration?",
    "How do I solve a quadratic equation?",
    "Can you explain how gravity works?",
    "What is the derivative of x^2?"
]

# Demonstrate routing and answers
if __name__ == "__main__":
    for question in questions:
        print(f"\nQuestion: {question}")
        print("Answer:", route_and_answer_question(question))
