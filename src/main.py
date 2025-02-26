from data_processing import load_data, save_data
from embeddings import get_embedding
import pandas as pd

def process_texts(file_path, output_folder):
    df = load_data(file_path)
    df['embedding'] = df['text'].apply(get_embedding)
    save_data(df, "embeddings.csv", output_folder)

if __name__ == "__main__":
    process_texts("data/input.csv", "data")
