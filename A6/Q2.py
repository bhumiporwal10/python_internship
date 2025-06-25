import pandas as pd

left = pd.DataFrame({
    'Name': ['v1', 'v2', 'v3'],
    'Subject': ['hindi', 'korean', 'english'],
    'Id': [24, 12, 27]
})

right = pd.DataFrame({
    'Name': ['b1', 'b2', 'b3'],
    'Subject': ['hindi', 'chemistry', 'physics'],
    'Id': [24, 12, 27]
})

# Inner Merge - only matching 'Id'
print("Inner Merge (on Id):")
result = left.merge(right, on='Id')
print(result)

# Right Join on Subject
print("\n Right Join (on Subject):")
r = right.merge(left, on='Subject', how='right')
print(r)

# Left Join on Subject
print("\n Left Join (on Subject):")
r = right.merge(left, on='Subject', how='left')
print(r)

# Outer Join on Subject
print("\n Outer Join (on Subject):")
r = right.merge(left, on='Subject', how='outer')
print(r)

# Join using index
print("\n Join using index:")
resu = left.join(right, lsuffix='_left', rsuffix='_right')
print(resu)
