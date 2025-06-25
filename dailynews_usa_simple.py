import requests, json, os
from colorama import Fore, Style, init
from dotenv import load_dotenv  
import os
load_dotenv()  # <-- to load .env variables

news_api_key = os.getenv("NEWS_API_KEY")
init(autoreset=True)


# Your API key
country = "us"
url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={news_api_key}"

# Parameters for the request
result = requests.get(url)
data = result.json()

# Simpler loop for first 10 articles
for article in data["articles"][:5]:
    print(Fore.CYAN + f"Title: {article['title']}")
    print(Fore.GREEN + f"   Source: {article['source']['name']}")
    print(Fore.YELLOW + f"   Content: {article['content']}")
    print(Fore.BLUE + f"   Link: {article['url']}")
    print(Style.DIM + "-" * 50)