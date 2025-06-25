import pandas as pd


A = pd.DataFrame({
    'ID': [1, 2],
    'Name': ['Bhumi', 'Advait']
})

B = pd.DataFrame({
    'ID': [3, 4],
    'Name': ['Kiva', 'Taehyung']
})

C = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Marks': [98, 97, 99, 100]
})

AB = pd.concat([A, B], ignore_index=True)
print("Concatenated A and B:\n", AB)

result = AB.merge(C, on='ID')
print("\nFinal Merged DataFrame:\n", result)
