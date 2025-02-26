import re, os, pickle, time
import numpy as np
from scipy.optimize import linear_sum_assignment

def hungarian(cost_matrix, audit_dict, rev_audit_dict, emp_dict, rev_emp_dict, audit, emp):
    row_ind, col_ind = linear_sum_assignment(cost_matrix)
    assigned_data = {
        'audit_ID': [audit_dict[x] for x in row_ind],
        'audit_text': audit[row_ind],
        'empresa_id': [emp_dict[x] for x in col_ind],
        'empresa_text': emp[col_ind],
        'penalty': cost_matrix[row_ind, col_ind]
    }
    return pd.DataFrame(assigned_data)
