print("Hello World")

name = "Maria"
greeting = f"Hello {name}, how are you"
print(greeting)

name = "Rishan"
greeting = "Hello {}, how are you"
rishan_greeting = greeting.format(name)
print(rishan_greeting)

name = input('Enter you name:')
print(f"Hello, {name}")

age = input('Enter your age:')
int_age = int(age)
print(f'You have lived {int_age * 12} months')