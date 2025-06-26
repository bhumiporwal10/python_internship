import pandas as pd

dates = pd.date_range(start='2023-01-01', periods=5)
print(dates)

df = pd.DataFrame({'dob': ['2005-10-10', '2000-08-15']})
df['dob'] = pd.to_datetime(df['dob'])
print(df)
