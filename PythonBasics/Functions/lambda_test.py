def divide(x,y):
    return x/y


print(divide(15, 3))

result = lambda x, y: x/y
print(result(15,3))

avg = lambda grades: sum(grades)/len(grades)
total = lambda grades: sum(grades)
top = lambda grades: max(grades)

'''
operations = {
    'average': avg,
    'total': total,
    'top': top
}

operations = {
    'average': lambda grades: sum(grades)/len(grades),
    'total': lambda grades: sum(grades),
    'top': lambda grades: max(grades)
}
'''

operations = {
    'average': lambda grades: sum(grades)/len(grades),
    'total': sum,
    'top': max
}

student_grades = [
    {'name': 'Bob', 'grades': (80, 96, 68, 50)},
    {'name': 'Nick', 'grades': (67, 90, 68)},
    {'name': 'Sally', 'grades': (80, 82, 67, 50, 78)},
    {'name': 'Rose', 'grades': (80, 96, 68, 50, 90, 45)}
    ]

for each_student in student_grades:
    student_name =  each_student['name']
    student_grades = each_student['grades']

    print(f'Student Name = {student_name}')
    operation = input('Do you want average or total or top grade')
    operation_function = operations[operation]

    print(operation_function(student_grades))


