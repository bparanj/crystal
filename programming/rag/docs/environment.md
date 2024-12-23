# Create a virtual environment
python3 -m venv rag

# Activate it
source rag/bin/activate  # On Unix/macOS

# Install the required packages
pip3 install langchain-openai python-dotenv openai

# Now run your script
python completion.py
