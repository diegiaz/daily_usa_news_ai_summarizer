openai_ask.py is a very simple structure of calling openai API and interact with it.
Please remember you need to get yourself an OPEN AI key a newsapi key to use the scripts.

# News Summarizer Scripts

This workspace contains Python scripts to fetch and summarize the latest news headlines from the United States using NewsAPI and OpenAI's GPT models.

## Project Structure

```
94_openai.py
dailynewsusa_detailed.py
dailynewsusa_simple.py
requirements.txt
```

## File Descriptions

- **[dailynewsusa_simple.py](dailynewsusa_simple.py)**  
  Fetches the top 5 news headlines from the US and prints their titles, sources, content, and links in a simple, colorized format.

- **[dailynewsusa_detailed.py](dailynewsusa_detailed.py)**  
  Fetches the top 5 news headlines from the US, then uses OpenAI's GPT model to generate a brief summary for each article. The output includes the title, source, AI-generated summary, and a link to the full article.

- **[94_openai.py](94_openai.py)**  
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
  python dailynewsusa_simple.py
  ```

- To fetch news headlines and get AI-generated summaries:
  ```sh
  python dailynewsusa_detailed.py
  ```

- To test OpenAI GPT with a sample prompt:
  ```sh
  python 94_openai.py
  ```

## Notes

- The scripts use the `colorama` library for colored terminal output.
- For security, avoid sharing your API keys publicly.
- You can change the country or number of articles by editing the relevant variables in the scripts.

---

**Author:**  
This project is for educational purposes and demonstrates basic integration with NewsAPI and OpenAI GPT