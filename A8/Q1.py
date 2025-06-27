import numpy as np

random = np.random.rand(3, 3)
print("Random array:\n", random)

empty = np.empty((4, 2))
print("Empty array (4x2):\n", empty)

full = np.full((4, 2), 9)
print("Full array (4x2):\n", full)

zeros = np.zeros((3, 5))
print("Zeros array (3x5):\n", zeros)

ones = np.ones((4, 3, 2))
print("Ones array (4x3x2):\n", ones)
