import numpy as np

arr = np.array([[3, 7, 2], [9, 1, 5]])

print("Original Array:\n", arr)

print("Maximum value:", arr.max())

print("Minimum value:", arr.min())

print("Shape:", arr.shape)

print("All elements:")
for i in arr:
    for j in i:
        print(j)

print("\nSpecific element [1][2]:", arr[1][2])

total = np.sum(arr)
print("Sum of all elements:", total)


a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("\nArray A:", a)
print("Array B:", b)

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

