import pandas as pd


df = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['A', 'B', 'C'],
    'Marks': [80, 45, 60]
})


for i, r in df.iterrows():
    print(r['ID'], r['Name'])


print(df[df['Marks'] > 50])


print(df.iloc[0])


print(df['Name'].head(2))


df1 = df[df['Marks'] >= 50]
print(df1)


new = {'ID': 4, 'Name': 'D', 'Marks': 90}
df.loc[len(df)] = new
print(df)


lst = df.values.tolist()
print(lst)
