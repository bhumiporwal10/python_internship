import numpy as np
from numpy.linalg import inv, solve

A = np.array([[1, -2, 3],
              [-1, 3, -1],
              [2, -5, 5]])

B = np.array([9, -6, 17])

# Using solve()
solution = solve(A, B)
print("\n Solution using linalg.solve():", solution)

# Using Inverse method
A_inv = inv(A)
X = A_inv.dot(B)
print("Solution using Inverse Matrix method:", X)
