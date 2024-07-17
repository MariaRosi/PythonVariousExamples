import pandas as pd

student_data = {
    'Name': ['Reena', 'Joy', 'Sameer', 'Jack', 'Seema'],
    'Marks': [98, 56, 78, 82, 69],
    'Rank': [1, 5, 3, 2, 4]
}

df = pd.DataFrame(student_data)
print(df)

df = pd.DataFrame(student_data, index=['rowA', 'rowB', 'rowC', 'rowD', 'rowE'],)
print(df)

print(df.loc['rowA', 'Name'])

print(df.loc['rowA'])

print(df.iloc[[1, 3]])

df.add({'Name' : 'Sunny'})

for col in df:
    print(col)


print(f"The dimension {df.ndim}")
print(f"The size {df.size}")
print(f"The shape {df.shape}")
print(f"The index {df.index}")

print(f"The transposec {df.T}")

print(f"The top 3 rows {df.head(3)}") # Default top 5 rows
print(f"The last 3 rows {df.tail(3)}")
