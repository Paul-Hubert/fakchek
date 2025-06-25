import openai
import os
import re

def fact_check_text(text):
    # Read the OpenAI API key from a file
    with open(os.path.join(os.path.dirname(__file__), 'openai_key.txt'), 'r') as f:
        OPENAI_API_KEY = f.read().strip()

    # Create an OpenAI client
    client = openai.OpenAI(api_key=OPENAI_API_KEY)

    # Example: Call the OpenAI Chat API (GPT-3.5/4) using v1.0.0+ syntax
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # or "gpt-4"
        messages=[
            {"role": "system", "content": "You are a professional fact checker."},
            {"role": "user", "content": "Hello, is this statement true ? Write Yes or No in the beginning followed by an explanation " + text}
        ]
    )

    str = response.choices[0].message.content

    print(str)

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

