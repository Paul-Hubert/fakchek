import openai
import os

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
            {"role": "user", "content": "Hello, is this statement true ? " + text}
        ]
    )

    return response.choices[0].message.content
