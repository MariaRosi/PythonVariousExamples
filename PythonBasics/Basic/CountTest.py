'''word='cucumber'
print ('count of cu = ', word.count('cu'))
print ('pos of er -->', word.index('er'))
print ('pos of co -->', word.index('co'))
'''
for i in range(101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)