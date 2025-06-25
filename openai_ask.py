from openai import OpenAI
from dotenv import load_dotenv  
import os
load_dotenv()  # <-- to load .env variables
# Initialize the client with direct API key


api_key = os.getenv("OPENAI_API_KEY_2")
client = OpenAI(api_key)

content = "Whats the president of USA?"

try:
    completion = client.chat.completions.create(
        model="gpt-4o",  # Changed from gpt-4 to gpt-4o for more recent knowledge
        messages=[
            {
                "role": "user",
                "content": content
            }
        ]
    )
  
    print(completion.choices[0].message.content)

except Exception as e:
    print(f"An error occurred: {e}")