import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import pairwise_distances

data = pd.read_excel(r"19CSE305_LabData_Set3.1.xlsx", sheet_name='thyroid0387_UCI')


selected_data = data.iloc[:20, 1:-1]  

selected_data = selected_data.replace('?', np.nan)

selected_data = selected_data.fillna(0)

non_numeric_columns = selected_data.select_dtypes(exclude=[np.number]).columns

selected_data = pd.get_dummies(selected_data, columns=non_numeric_columns)

jc_matrix = 1 - pairwise_distances(selected_data, metric='hamming')

smc_matrix = 1 - pairwise_distances(selected_data, metric='matching')

sns.set(style="white")
plt.figure(figsize=(10, 4))

plt.subplot(121)
sns.heatmap(jc_matrix, annot=True, cmap="YlGnBu", cbar=False, xticklabels=False, yticklabels=False)
plt.title("Jaccard Coefficient")

plt.subplot(122)
sns.heatmap(smc_matrix, annot=True, cmap="YlGnBu", cbar=False, xticklabels=False, yticklabels=False)
plt.title("Simple Matching Coefficient")

plt.tight_layout()
plt.show()

