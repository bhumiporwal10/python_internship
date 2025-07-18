import numpy as np

arr = np.array([[6, -8, 73, -110], [np.nan, -8, 0, 94]])
arr = np.nan_to_num(arr, nan=0)  # Replace NaN with 0
interchanged = arr.T  # Interchange rows and columns
print(" Interchanged 2D array:\n", interchanged)



