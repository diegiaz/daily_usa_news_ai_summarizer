import requests, json, os
from colorama import Fore, Style, init
from openai import OpenAI
init(autoreset=True)
from dotenv import load_dotenv  
import os
load_dotenv()  # <-- to load .env variables

# API configurations
news_api_key = os.getenv('NEWS_API_KEY')
openai_api_key = os.getenv('OPENAI_API_KEY_2')
client = OpenAI(api_key= openai_api_key)

country = "us"

url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={news_api_key}"
result = requests.get(url)
data = result.json()
#print(json.dumps(data, indent=2))

# Process top 5 articles
for article in data["articles"][0:5]:
    print(Fore.CYAN + f"Article:{article['title']}")
    print(Fore.GREEN + f"Source: {article['source']['name']}")
    
    # Prepare content for OpenAI
    article_content = f"Title: {article['title']}\n{article['content']}"
    
    try:
        # Get AI summary
        completion = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "user",
                    "content": f"Please provide a brief, clear summary of this news article in 2-3 sentences: {article_content}"
                }
            ]
        )
        print(Fore.YELLOW + "AI Summary:")
        print(Fore.WHITE + completion.choices[0].message.content)
        print(Fore.BLUE + f"Full article: {article['url']}")
        print(Style.DIM + "-" * 80)
        
    except Exception as e:
        print(Fore.RED + f"Error getting AI summary: {e}")
