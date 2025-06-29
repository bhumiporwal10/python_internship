import numpy as np
null_vec = np.zeros(10)
print(null_vec)
null_vec[5] = 11
print("Updated null vector:\n", null_vec)

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 1:4])
