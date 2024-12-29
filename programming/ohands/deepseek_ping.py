from openai import OpenAI
import os

def test_deepseek_connection(api_key: str) -> None:
    """Test connection to DeepSeek Coder API"""
    try:
        # Initialize client with DeepSeek base URL
        client = OpenAI(
            api_key=api_key,
            base_url="https://api.deepseek.com/v1"
        )
        
        # Simple test prompt
        test_prompt = "Write a simple Python function that adds two numbers."
        
        print("Sending test request to DeepSeek Coder...")
        
        # Make API call
        response = client.chat.completions.create(
            model="deepseek-coder-33b-instruct",
            messages=[
                {"role": "user", "content": test_prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )
        
        # Print response
        print("\nAPI Connection Successful!")
        print("\nTest Response:")
        print("-" * 50)
        print(response.choices[0].message.content)
        print("-" * 50)
        
        # Print usage information
        print("\nUsage Information:")
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Completion tokens: {response.usage.completion_tokens}")
        print(f"Total tokens: {response.usage.total_tokens}")
        
    except Exception as e:
        print(f"\nError connecting to DeepSeek API: {str(e)}")
        print("\nPlease check:")
        print("1. API key is correct")
        print("2. Internet connection is working")
        print("3. DeepSeek API service is available")

def main():
    # Get API key from environment variable
    api_key = os.getenv("DEEPSEEK_API_KEY")
    
    if not api_key:
        print("Error: DEEPSEEK_API_KEY environment variable not found")
        print("\nPlease set your API key using:")
        print("export DEEPSEEK_API_KEY='your-api-key-here'")
        return
    
    # Test the connection
    test_deepseek_connection(api_key)

if __name__ == "__main__":
    print("DeepSeek Coder API Connection Test")
    print("=" * 50)
    main()