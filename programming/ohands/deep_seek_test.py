import requests
import os
from typing import Optional

class DeepSeekAPITester:
    def __init__(self, api_key: Optional[str] = None):
        """Initialize the API tester with optional API key."""
        self.api_key = api_key or os.getenv('DEEPSEEK_API_KEY')
        self.base_url = "https://api.deepseek.com/v1"

    def test_connection(self) -> dict:
        """Test the API connection and authentication."""
        if not self.api_key:
            raise ValueError("API key not provided. Set DEEPSEEK_API_KEY environment variable or pass it to the constructor.")

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        try:
            # Simple test request - modify endpoint as needed
            response = requests.get(
                f"{self.base_url}/models",
                headers=headers
            )

            if response.status_code == 200:
                return {
                    "status": "success",
                    "message": "API connection successful",
                    "data": response.json()
                }
            elif response.status_code == 401:
                return {
                    "status": "error",
                    "message": "Authentication failed. Invalid API key.",
                    "error_code": response.status_code
                }
            else:
                return {
                    "status": "error",
                    "message": f"API request failed with status code: {response.status_code}",
                    "error_code": response.status_code,
                    "response": response.text
                }

        except requests.exceptions.RequestException as e:
            return {
                "status": "error",
                "message": f"Connection error: {str(e)}",
                "error": str(e)
            }

def main():
    """Main function to run the API test."""
    # Get API key from environment variable or input
    api_key = os.getenv('DEEPSEEK_API_KEY')
    if not api_key:
        api_key = input("Please enter your Deep Seek API key: ")

    # Initialize tester
    tester = DeepSeekAPITester(api_key)

    try:
        # Run test
        result = tester.test_connection()

        # Print results
        print("\nAPI Test Results:")
        print("-" * 50)
        print(f"Status: {result['status']}")
        print(f"Message: {result['message']}")

        # Print additional data if successful
        if result['status'] == 'success':
            print("\nAvailable Models:")
            for model in result.get('data', {}).get('data', []):
                print(f"- {model['id']}")

    except Exception as e:
        print(f"\nError during test execution: {str(e)}")

if __name__ == "__main__":
    main()