'''
# Dict
my_student = {
    "name" : "Meena",
    "grades" : [90, 78, 83, 67, 89]
}


# Function to return the average grade
def average_grade(student):
    return sum(student["grades"]) / len(student["grades"])


print(average_grade(my_student))
'''

# Define the class
class Student:
    def __init__(self, new_name, new_grades):
        self.name = new_name
        self.grades = new_grades

    def average(self):
        return sum(self.grades) / len(self.grades)


student_one = Student('Meena', [67, 89, 90, 78, 92])
student_two = Student('Bob', [77, 88, 98, 68, 94])

print(student_one.name, student_one.grades, student_one.average())
print(student_two.name, student_two.grades, student_two.average())






