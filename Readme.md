# News Summarizer Scripts

This workspace contains Python scripts to fetch and summarize the latest news headlines from the United States using NewsAPI and OpenAI's GPT models.

## Project Structure

```
openai_ask.py
dailynews_usa_ai.py
dailynews_usa_simple.py
requirements.txt
```

## File Descriptions

- **[dailynewsusa_simple.py](dailynews_usa_simple.py)**  
  Fetches the top 5 news headlines from the US and prints their titles, sources, content, and links in a simple, colorized format.

- **[dailynewsusa_detailed.py](dailynews_usa_ai.py)**  
  Fetches the top 5 news headlines from the US, then uses OpenAI's GPT model to generate a brief summary for each article. The output includes the title, source, AI-generated summary, and a link to the full article.

- **[94_openai.py](openai_ask.py)**  
  Demonstrates how to use the OpenAI API to answer a simple question using the GPT model.

- **[requirements.txt](requirements.txt)**  
  Lists the required Python packages to run the scripts.

## Setup

1. **Install dependencies**  
   Run the following command in your terminal:
   ```sh
   pip install -r requirements.txt
   ```

2. **API Keys**  
   - The scripts require a NewsAPI key and an OpenAI API key.
   - The keys are already included in the scripts for demonstration, but you should replace them with your own for production use.

## Usage

- To fetch and print simple news headlines:
  ```sh
  python dailynews_usa_simple.py
  ```
  

- To fetch news headlines and get AI-generated summaries:
  ```sh
  python dailynews_usa_ai.py
  ```

- To test OpenAI GPT with a sample prompt:
  ```sh
  python openai_ask.py
  ```

## Notes

- The scripts use the `colorama` library for colored terminal output.
- For security, avoid sharing your API keys publicly.
- You can change the country or number of articles by editing the relevant variables in the scripts.

---

**Author:**  
Diegiaz
This project is for educational purposes and demonstrates basic integration with NewsAPI and OpenAI GPT
