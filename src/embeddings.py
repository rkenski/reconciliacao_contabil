import openai
import time
from openai.error import APIConnectionError
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def get_embedding(text, model="text-embedding-3-large", retry_count=3):
    """Get the embedding for a given text."""
    for _ in range(retry_count):
        try:
            return openai.Embedding.create(input=text, model=model)
        except APIConnectionError:
            time.sleep(1)  # Wait before retrying
    print(f"Failed to get embedding for text: {text}")
    return None