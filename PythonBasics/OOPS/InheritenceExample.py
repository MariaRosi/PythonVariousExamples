class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average_marks(self):
        return sum(self.marks) / len(self.marks)


class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

    def weekly_salary(self):
        return self.salary * 37.5


ws1 = WorkingStudent('Neena', 'MIT', 15)
ws1.marks.append(78)
ws1.marks.append(98)
print(ws1.name, ws1.school, ws1.marks, ws1.average_marks(), ws1.weekly_salary())
