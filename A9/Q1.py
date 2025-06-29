import numpy as np

arr1 = np.array([[1, 2, 3]])
arr2 = np.array([[4, 5, 6],[7, 8, 9]])

combined = np.concatenate((arr2, arr1), axis=0)
print("Using concatenate:\n", combined)
