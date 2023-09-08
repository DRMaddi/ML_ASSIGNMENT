import pandas as pd
import numpy as np

data = pd.read_excel(r"19CSE305_LabData_Set3.1.xlsx", sheet_name='thyroid0387_UCI')

for col in data.columns:
    if data[col].dtype == 'float64' or data[col].dtype == 'int64':
        if col in ['TSH', 'T3', 'TT4', 'T4U', 'FTI']:
            data[col].fillna(data[col].median(), inplace=True)
        else:
            data[col].fillna(data[col].mean(), inplace=True)
    elif data[col].dtype == 'object':
        data[col].fillna(data[col].mode()[0], inplace=True)

missing_values_after_imputation = data.isnull().sum()

print("Missing Values After Imputation:")
print(missing_values_after_imputation)