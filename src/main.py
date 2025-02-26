from pathlib import Path
from data_processing import load_data, save_data
from embeddings import get_embedding
import pandas as pd

def process_texts(file_path, output_folder):
    """Process texts from a file and save their embeddings."""
    df = load_data(file_path)
    df['embedding'] = df['text'].apply(get_embedding)
    save_data(df, "embeddings.csv", output_folder)

if __name__ == "__main__":
    data_folder = Path("data")
    data_folder.mkdir(exist_ok=True)
    input_file = data_folder / "input.csv"  # Replace with actual file
    process_texts(input_file, data_folder)
