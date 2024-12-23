from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

# Define the Joke schema
class Joke(BaseModel):
    setup: str = Field(description="The setup of the joke")
    punchline: str = Field(description="The punchline to the joke")

# Initialize the ChatOpenAI model with structured output
model = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)
model = model.with_structured_output(Joke)

# Create a system message to guide the model
system_message = """You are a comedian specialized in creating clean, family-friendly jokes. 
When given a topic, create a joke with a setup and punchline structure."""

# Function to generate a joke
def get_joke(topic: str):
    messages = [
        HumanMessage(content=f"Tell me a family-friendly joke about {topic}")
    ]
    return model.invoke(messages)

# Example usage
if __name__ == "__main__":
    try:
        joke = get_joke("dogs")
        print(f"Setup: {joke.setup}")
        print(f"Punchline: {joke.punchline}")
    except Exception as e:
        print(f"Error generating joke: {str(e)}")

