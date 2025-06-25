import os
import openai

def get_key():
    with open(os.path.join(os.path.dirname(__file__), 'openai_key.txt'), 'r') as f:
        OPENAI_API_KEY = f.read().strip()
        return OPENAI_API_KEY
    
def call_openai(prompt):
    # Create an OpenAI client
    client = openai.OpenAI(api_key=get_key())

    # Example: Call the OpenAI Chat API (GPT-3.5/4) using v1.0.0+ syntax
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # or "gpt-4"
        messages=[
            {"role": "system", "content": "You are a professional fact checker."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content