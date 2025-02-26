import os
from pathlib import Path
from dotenv import load_dotenv
import pandas as pd
import openai
import time
from tqdm.auto import tqdm
from openai.error import APIConnectionError

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def get_embedding(text, model="text-embedding-3-large", retry_count=3):
    """Get the embedding for a given text."""
    for _ in range(retry_count):
        try:
            return openai.Embedding.create(input=text, model=model)
        except APIConnectionError as e:
            time.sleep(1)  # Wait a period of time before retrying
    print(f"Failed to get embedding for text: {text}")
    return None

def save_embeddings(df, filename, output_folder, mode='parquet'):
    """Save the embeddings to a file."""
    file_path = output_folder / filename
    if mode == 'parquet':
        df.to_parquet(file_path)
    elif mode == 'csv':
        df.to_csv(file_path)
    elif mode == 'pkl':
        df.to_pickle(file_path)
    else:
        print("Mode not recognized")
        return None
    print(f"Saved embeddings to {file_path}")

def process_texts(frases, indices, output_folder, start_batch=0):
    """Main function to process all texts and save them in batches."""
    batch_size = 100
    for i in range(0, len(frases), batch_size):
        batch_idx = start_batch + (i // batch_size)
        print(f"Processing batch {batch_idx}")
        try:
            batch_embeddings = [get_embedding(text) for text in frases[i:i+batch_size]]
            df = pd.DataFrame({'index': indices[i:i+batch_size], 'embedding': batch_embeddings})
            save_embeddings(df, f'embeddings_batch_{batch_idx}.parquet', output_folder)
        except Exception as e:
            print(f"Error processing batch {batch_idx}: {e}")

if __name__ == "__main__":
    data_folder = Path("data")
    data_folder.mkdir(exist_ok=True)
    frases = ["Example text 1", "Example text 2"]  # Replace with actual data
    indices = list(range(len(frases)))
    process_texts(frases, indices, data_folder)
