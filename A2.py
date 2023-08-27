import pandas
import numpy

dataframe=pandas.read_excel(r"Lab Session1 Data.xlsx",sheet_name="Purchase data")

Adata=dataframe.iloc[0:10,1:4]
A=Adata.to_numpy()

Cdata=dataframe.iloc[0:10,4:5]
C=Cdata.to_numpy()

Ain=numpy.linalg.pinv(A)
X=numpy.matmul(Ain,C)
Ain=numpy.linalg.pinv(A)
X=numpy.matmul(Ain,C)
print("The model vector X for predicting the cost of the products available with the vendor: ")
print(X)
