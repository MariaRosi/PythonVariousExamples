
import datetime

class Employee:
    pay_increase_rate = 1.5

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def pay_increase(self):
        self.pay = int(self.pay * self.pay_increase_rate)

    @classmethod
    def create_instance_from_string(cls, str):
        first_name, last_name, pay = str.split('-')
        return cls(first_name, last_name, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

class Developer(Employee):
    def __init__(self,first_name, last_name, pay, prog_lang):
        super().__init__(first_name, last_name, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self,first_name, last_name, pay, governed_employee = None):
        super().__init__(first_name, last_name, pay)
        if governed_employee is None:
            self.governed_employee = []
        else:
            self.governed_employee = governed_employee

    def add_governed_employee(self, emp):
        if emp not in self.governed_employee:
            self.governed_employee.append(emp)
            print('Inside add_governed_employee ', self.governed_employee)

    def remove_governed_employee(self, emp):
        if emp in self.governed_employee:
            self.governed_employee.remove(emp)

    def display_governed_employee(self):
        for emp in self.governed_employee:
            print('Inside display_governed_employee ', emp.fullname())

developer1 = Developer('Sam', 'Kumar', 65000, 'Java')
print('Full Name = ' + developer1.fullname() + ', Programming Language = ' + developer1.prog_lang)


emp1 = Employee('Divya', 'Saha', 50000)
emp2 = Employee('Sunny', 'Singh', 50000)

manager1 = Manager('Abhishek', 'Singh', 90000, [emp1])
manager1.display_governed_employee()
manager1.add_governed_employee(emp2)
manager1.display_governed_employee()
manager1.add_governed_employee(developer1)
manager1.display_governed_employee()
manager1.remove_governed_employee(developer1)
manager1.display_governed_employee()
print(emp1)

print('{} {}'.format(emp1.first_name, emp1.last_name))
print('{} {}'.format(emp2.first_name, emp2.last_name))

print(emp1.fullname())
print(Employee.fullname(emp1))

print(emp2.fullname())
print(Employee.fullname(emp2))

print(emp1.pay)

emp1.pay_increase()

print(emp1.pay)

Employee.pay_increase_rate = 2

print(emp1.pay_increase_rate)
print(emp2.pay_increase_rate)

emp1.pay_increase_rate = 1.8

print(emp1.pay_increase_rate)
print(emp2.pay_increase_rate)
print('==============================================')
emp3 = Employee.create_instance_from_string('Akhil-Das-70000')
print(emp3.fullname())
print(emp3.pay)

date = datetime.date(2024, 2, 1)

print(Employee.is_workday(date))

date = datetime.date(2024, 2, 4)

print(Employee.is_workday(date))
