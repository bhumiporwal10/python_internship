import pandas as pd


data = [[1, 'A'], [2, 'B']]
df1 = pd.DataFrame(data, columns=['ID', 'Name'])
print(df1)

d = {'ID': [1, 2], 'Name': ['A', 'B']}
df2 = pd.DataFrame(d)
print(df2)

l = [[101, 'X'], [102, 'Y']]
df3 = pd.DataFrame(l, columns=['Code', 'Sub'])
print(df3)

t = [(1, 'Red'), (2, 'Blue')]
df4 = pd.DataFrame(t, columns=['ID', 'Color'])
print(df4)

ld = [{'ID': 1, 'Age': 21}, {'ID': 2, 'Age': 22}]
df5 = pd.DataFrame(ld)
print(df5)
