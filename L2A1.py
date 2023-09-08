import pandas as pd
import numpy as np

data = pd.read_excel(r"19CSE305_LabData_Set3.1.xlsx", sheet_name='thyroid0387_UCI')

data_types = {}

def determine_data_type(column):
    unique_values = column.unique()
    if len(unique_values) <= 10:
        return 'nominal'  
    return 'ordinal'  

for col in data.columns:
    data_types[col] = determine_data_type(data[col])

nominal_cols = [col for col, dtype in data_types.items() if dtype == 'nominal']
ordinal_cols = [col for col, dtype in data_types.items() if dtype == 'ordinal']

numeric_cols = data.select_dtypes(include=['number'])
data_range = numeric_cols.describe().loc[['min', 'max']]

missing_values = data.isin(['?']).sum()

outliers = {}
for col in numeric_cols.columns:
    mean = numeric_cols[col].mean()
    std = numeric_cols[col].std()
    lower_bound = mean - 3 * std
    upper_bound = mean + 3 * std
    outliers[col] = len(numeric_cols[(numeric_cols[col] < lower_bound) | (numeric_cols[col] > upper_bound)])

numeric_mean = numeric_cols.mean()
numeric_variance = numeric_cols.var()

print("Data Types (Nominal or Ordinal)")
for col, dtype in data_types.items():
    print(f"{col}: {dtype}")

print("\nEncoding Schemes")
print("Nominal :", nominal_cols)
print("Ordinal :", ordinal_cols)

print("\nData Range")
print(data_range)

print("\nMissing Values")
print(missing_values)

print("\nOutliers")
print(outliers)

print("\nMean and Variance for Numeric Variables")
print("Mean:")
print(numeric_mean)
print("\nVariance:")
print(numeric_variance)
