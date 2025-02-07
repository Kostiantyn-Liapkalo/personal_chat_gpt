from openai import OpenAI
from dotenv import load_dotenv
import os

# Loading environment variables from .env
load_dotenv(".env")

# Initializing the OpenAI client using an API key from .env
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Text generation
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Write a haiku about recursion in programming."}
    ]
)

# Output the result
print(completion.choices[0].message.content)