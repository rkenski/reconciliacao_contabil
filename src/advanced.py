import pandas as pd
from pathlib import Path
from functions import hungarian
from embeddings import load_embeddings

def run_advanced_reconciliation():
    data_folder = Path("data")
    empresa_df = pd.read_excel(data_folder / "input.xlsx", sheet_name="Empresa")
    hanoi_df = pd.read_excel(data_folder / "input.xlsx", sheet_name="Inventário")
    embeddings = load_embeddings(data_folder / "embeddings")
    cost_matrix, audit_dict, rev_audit_dict, emp_dict, rev_emp_dict, audit, emp = get_cost_matrix(
        empresa_df, hanoi_df, embeddings)
    assigned_df = hungarian(cost_matrix, audit_dict, rev_audit_dict, emp_dict, rev_emp_dict, audit, emp)
    assigned_df.to_excel(data_folder / "reconciled_output.xlsx", index=False)
    print("Reconciliation complete!")

if __name__ == "__main__":
    run_advanced_reconciliation()