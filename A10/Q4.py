import numpy as np
array = np.array([[1, -2, 3], [-4, 5, -6]])
array[array < 0] = 0
print("\n Negative Replaced with 0:\n", array)
