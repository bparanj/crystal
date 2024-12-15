1. Install `python-dotenv`:  
   ```bash
   pip install python-dotenv
   ```

2. Create a `.env` file in your project root. Add variables:  
   ```env
   API_KEY=your_api_key_here
   ```

3. In your Python code:  
   ```python
   import os
   from dotenv import load_dotenv

   load_dotenv()        # loads variables from .env into environment
   api_key = os.getenv("API_KEY")
   ```
