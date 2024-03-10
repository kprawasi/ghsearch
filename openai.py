# openai_integration.py

import openai

# Set up your OpenAI API key here
api_key = "YOUR_OPENAI_API_KEY"

def complete_text(prompt):
    openai.api_key = api_key
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    prompt = "I am looking for an open source project that helps with "
    completion = complete_text(prompt)
    print(completion)
