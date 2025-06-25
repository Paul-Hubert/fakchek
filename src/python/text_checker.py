from model import call_openai
from source_search import find_source
import re

def fact_check_text(text):
    # Read the OpenAI API key from a file
    
    prompt = "Hello, is this statement true ? Write Yes or No in the beginning followed by an explanation "
    prompt += text

    source = find_source(text)

    if source != "":
        prompt += "\n Here is additional context from a google search to help fact check : "
        prompt += source

    str = call_openai(prompt)

    (answer, explanation) = extract_answer(str)

    return (answer, explanation)


"""
Extracts whether the response starts with 'Yes' or 'No' (case-insensitive),
and returns a tuple (answer, explanation).
If neither is found, returns (None, response).
"""
def extract_answer(response):
    # Match 'Yes' or 'No' at the beginning, possibly followed by punctuation and whitespace
    match = re.match(r'^\s*(Yes|No)\b[\s:,-]*', response, re.IGNORECASE)
    if match:
        answer = match.group(1).capitalize().strip()
        #explanation = response[match.end():].lstrip()
        is_true = False
        if answer == 'Yes':
            is_true = True
        return (is_true, response)
    else:
        return (None, response)

