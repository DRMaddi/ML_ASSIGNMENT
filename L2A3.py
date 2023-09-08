import pandas as pd
from sklearn.preprocessing import MinMaxScaler

data = pd.read_excel(r"19CSE305_LabData_Set3.1.xlsx", sheet_name='thyroid0387_UCI')

data.replace('?', pd.NA, inplace=True)

numeric_attributes = ['age', 'TSH', 'T3', 'TT4', 'T4U', 'FTI']

data[numeric_attributes] = data[numeric_attributes].fillna(data[numeric_attributes].median())

minmax_scaler = MinMaxScaler()

data[numeric_attributes] = minmax_scaler.fit_transform(data[numeric_attributes])

print("Normalized Data:")
print(data.head())
