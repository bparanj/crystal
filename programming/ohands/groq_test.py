from groq import Groq
import os
import time

def test_groq_connection(api_key: str) -> None:
    """Test connection to Groq API"""
    try:
        # Initialize Groq client
        client = Groq(api_key=api_key)
        
        # Simple test prompt
        test_prompt = "Write a simple Python function that calculates the factorial of a number."
        
        print("Sending test request to Groq API...")
        start_time = time.time()
        
        # Make API call
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": test_prompt,
                }
            ],
            model="llama2-70b-4096",  # Groq's LLaMA 2 model
            temperature=0.7,
            max_tokens=500,
            top_p=1,
            stream=False
        )
        
        # Calculate response time
        response_time = time.time() - start_time
        
        # Print success message and response
        print("\nAPI Connection Successful!")
        print(f"Response Time: {response_time:.2f} seconds")
        
        print("\nTest Response:")
        print("-" * 50)
        print(chat_completion.choices[0].message.content)
        print("-" * 50)
        
        # Print usage information if available
        if hasattr(chat_completion, 'usage'):
            print("\nUsage Information:")
            print(f"Prompt tokens: {chat_completion.usage.prompt_tokens}")
            print(f"Completion tokens: {chat_completion.usage.completion_tokens}")
            print(f"Total tokens: {chat_completion.usage.total_tokens}")
        
    except Exception as e:
        print(f"\nError connecting to Groq API: {str(e)}")
        print("\nPlease check:")
        print("1. API key is correct")
        print("2. Internet connection is working")
        print("3. Groq API service is available")
        print("4. You have sufficient API credits")

def main():
    # Get API key from environment variable
    api_key = os.getenv("GROQ_API_KEY")
    
    if not api_key:
        print("Error: GROQ_API_KEY environment variable not found")
        print("\nPlease set your API key using:")
        print("export GROQ_API_KEY='your-api-key-here'")
        return
    
    # Test the connection
    test_groq_connection(api_key)

if __name__ == "__main__":
    print("Groq API Connection Test")
    print("=" * 50)
    main()