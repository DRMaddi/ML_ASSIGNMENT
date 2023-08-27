import pandas
import numpy

dataframe=pandas.read_excel(r"Lab Session1 Data.xlsx",sheet_name="Purchase data")

Adata=dataframe.iloc[0:10,1:4]
A=Adata.to_numpy()

Cdata=dataframe.iloc[0:10,4:5]
C=Cdata.to_numpy()

Ain=numpy.linalg.pinv(A)
X=numpy.matmul(Ain,C)

Au = numpy.hstack((A, C))
dimensionality=numpy.linalg.matrix_rank(Au)

print("Dimensionality: ",dimensionality)
print()
print("Number of vectors: ",dimensionality)
print()
rank_A=numpy.linalg.matrix_rank(A)
print("Rank of matrix: ",rank_A)
print()
Ain=numpy.linalg.pinv(A)
X=numpy.matmul(Ain,C)
print("The matrix X containing the costs of Candies, Mangoes, Milk Packets respecively: ")
print(X)