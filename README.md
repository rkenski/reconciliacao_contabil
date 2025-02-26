# Accounting Reconciliation using OpenAI Embeddings

This project automates accounting reconciliation by leveraging OpenAI embeddings to process and compare text data. The script is modular and structured for maintainability and scalability.

## Project Structure

```
accounting_reconciliation/
│── data/                    # Folder for input and output files
│── src/                     # Source code for the project
│   │── __init__.py           # Makes the folder a package
│   │── config.py             # Configuration (e.g., environment variables)
│   │── data_processing.py    # File operations and data handling
│   │── embeddings.py         # OpenAI embedding handling
│   │── main.py               # Main script to run reconciliation
│── .env                      # (Ignored) Stores API keys securely
│── .gitignore                # Ignores .env and data files
│── requirements.txt          # Required dependencies
│── README.md                 # Project documentation
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/accounting_reconciliation.git
   cd accounting_reconciliation
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up environment variables by creating a `.env` file in the root directory:
   ```bash
   OPENAI_API_KEY=your_openai_api_key
   ```

## Usage

1. Place your input CSV file in the `data/` folder (e.g., `input.csv`).
2. Run the main script:
   ```bash
   python src/main.py
   ```
3. The processed embeddings will be saved in `data/embeddings.csv`.

## Configuration

- **`config.py`**: Stores environment variables and configurable parameters.
- **`data_processing.py`**: Handles file operations (loading/saving data).
- **`embeddings.py`**: Fetches OpenAI embeddings for text data.
- **`main.py`**: Orchestrates the workflow.

## Contributing
Feel free to fork this repository and submit pull requests with improvements.

## License
MIT License
