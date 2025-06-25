from model import call_openai
import os
import requests
from bs4 import BeautifulSoup

def find_source(text):
    search_prompt = call_openai("Write only a google search prompt looking for a source to fact check this text : " + text)
    # search google and get first result, extract text body from webpage

    url = google_search(search_prompt)
    if url:
        page_text = extract_text_from_url(url)
        print(page_text)
        return page_text
    else:
        return ""



def google_search(query):
    key = get_key()

    # Call Custom Search JSON API with key
    search_engine_id = "51278d25f36c44d64"  # Replace with your actual search engine ID

    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": key,
        "cx": search_engine_id,
        "q": query,
        "num": 1
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        results = response.json()
        if "items" in results and len(results["items"]) > 0:
            return results["items"][0]["link"]
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

def get_key():
    with open(os.path.join(os.path.dirname(__file__), 'google_key.txt'), 'r') as f:
        KEY = f.read().strip()
        return KEY
