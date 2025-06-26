import pandas as pd

df = pd.read_csv("students")

# Basic info
print(df.info())

print(df.describe())

print(df.head(10))
print(df.tail(10))

print(df.columns)

print(df.shape)

print(df['Name'].value_counts())
