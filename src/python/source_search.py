from model import call_openai
import requests
from bs4 import BeautifulSoup

def find_source(text):
    search_prompt = call_openai("Write only a google search prompt looking for a source to fact check this text : " + text)
    # search google and get first result, extract text body from webpage

    url = google_search(search_prompt)
    if url:
        print(url)
        page_text = extract_text_from_url(url)
        print(page_text)
        return page_text
    else:
        return ""


def google_search(query):
    # Use DuckDuckGo as a simple alternative to Google for scraping
    search_url = "https://duckduckgo.com/html/"
    params = {"q": query}
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(search_url, params=params, headers=headers)
    
    print(response.text)
    soup = BeautifulSoup(response.text, "html.parser")
    results = soup.find_all("a", class_="result__a")
    print(results)
    if results:
        return results[0].get("href")
    return None

def extract_text_from_url(url):
    try:
        resp = requests.get(url, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(resp.text, "html.parser")
        # Remove scripts and styles
        for tag in soup(["script", "style", "noscript"]):
            tag.decompose()
        # Get visible text
        texts = soup.stripped_strings
        return " ".join(texts)
    except Exception as e:
        return ""

