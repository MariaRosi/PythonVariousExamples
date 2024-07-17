import pandas as pd

student_basic_data = {
    'Name': ['Reena', 'Joy', 'Sameer', 'Jack', 'Seema'],
    'ID': ["sd01", "sd02", "sd03", "sd04", "sd05"],
    'Roll': [1, 2, 3, 4, 5]
}

student_basic_more_data = {
    'Name': ['Sai', 'Lina'],
    'ID': ["sd06", "sd07"],
    'Roll': [6, 7]
}

student_marks_data = {
    'Marks': [98, 56, 78, 82, 69],
    'Rank': [1, 5, 3, 2, 4]
}

df_student_basic_data = pd.DataFrame(student_basic_data)
df_student_marks_data = pd.DataFrame(student_marks_data)

df_student_join_data = df_student_basic_data.join(df_student_marks_data)

print(f"\nJoined data\n {df_student_join_data}")

