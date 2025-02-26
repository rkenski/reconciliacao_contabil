import pandas as pd
from pathlib import Path

def load_data(filepath):
    """Load data from a given file path. Supports CSV and Excel formats."""
    filepath = Path(filepath)
    if filepath.suffix == ".csv":
        return pd.read_csv(filepath)
    elif filepath.suffix in [".xls", ".xlsx"]:
        return pd.read_excel(filepath)
    else:
        raise ValueError("Unsupported file format. Use .csv or .xlsx")

def save_data(df, filename, output_folder, mode='csv'):
    """Save data in the specified format. Supports CSV, Parquet, and Excel."""
    file_path = Path(output_folder) / filename
    if mode == 'csv':
        df.to_csv(file_path, index=False)
    elif mode == 'parquet':
        df.to_parquet(file_path, index=False)
    elif mode == 'xlsx':
        df.to_excel(file_path, index=False)
    else:
        raise ValueError("Unsupported format. Use 'csv', 'parquet', or 'xlsx'.")

    print(f"Saved data to {file_path}")
