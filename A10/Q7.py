
import numpy as np
from collections import Counter
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
avg = (arr1 + arr2) / 2
mean = np.mean([arr1, arr2])
median = np.median([arr1, arr2])

print("\n Average:\n", avg)
print("Mean:", mean)
print("Median:", median)
combined = np.concatenate((arr1.flatten(), arr2.flatten()))
counter = Counter(combined)
mode_value = counter.most_common(1)[0][0]
print("Mode:", mode_value)
