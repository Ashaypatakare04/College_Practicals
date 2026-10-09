import numpy as np

a= np.array([[1,2,3],[4,5,6]])
print("2D Array1:\n",a)

b=np.array([[7,8,9],[10,11,12]])
print("2D Array2:\n",b)


print("\nAddition:\n",a+b)
print("\nSubtraction:\n",a-b)
print("\nMultiplication:\n",a*b)
print("\nDivision:\n",a/b)
print("\nTranspose of 1st array:\n",a.T)
print("\nExponential of 1st array:\n",np.exp(a))