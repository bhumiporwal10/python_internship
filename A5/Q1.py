import pandas as pd

d = {'a': 10, 'b': 20, 'c': 30}
s1 = pd.Series(d)
print(s1)


l = [1, 2, 3, 4]
s2 = pd.Series(l)
print(s2)


print(s2[0])
print(s2[:2])
