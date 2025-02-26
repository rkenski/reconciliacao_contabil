import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DATA_FOLDER = "data"

# data_processing.py
import pandas as pd
from pathlib import Path

def load_data(filepath):
    """Load data from a given file path."""
    return pd.read_csv(filepath)

def save_data(df, filename, output_folder, mode='csv'):
    """Save data in the specified format."""
    file_path = Path(output_folder) / filename
    if mode == 'csv':
        df.to_csv(file_path, index=False)
    elif mode == 'parquet':
        df.to_parquet(file_path, index=False)
    print(f"Saved data to {file_path}")
