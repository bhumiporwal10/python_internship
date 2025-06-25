import pandas as pd

dates = ['2024-01-01', '2024-02-15', '2024-03-10']
converted = pd.to_datetime(dates)
print(converted)
