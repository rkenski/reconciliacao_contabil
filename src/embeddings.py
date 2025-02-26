import openai
import os
import time
import pandas as pd
import concurrent.futures
from openai.error import APIConnectionError
from pathlib import Path

def get_embedding(text, model="text-embedding-3-large", retry_count=3):
    """Get the embedding for a given text."""
    for _ in range(retry_count):
        try:
            return openai.Embedding.create(input=text, model=model)
        except APIConnectionError:
            time.sleep(1)
    print(f"Failed to get embedding for text: {text}")
    return None