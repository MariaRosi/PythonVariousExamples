d = {'Ram': 45, 'Nick': 23, 'Jack': 32}
print(d)

print(d['Nick']) #if the key passed not present then it thows key error
print(d.get('Nick'))
print(d.get('Sam')) #returns None
print(d.get('Sam', 'Not Found')) #passing default value
d['Nick'] = 25
print(d)

d.update({'Ram': 55, 'Jane': 20})
print(d)

del d['Jane']
print(d)

d.pop('Ram')
print(d)

d.update({'Ram': 55, 'Jane': 20})
print(d)

print(d.keys())
print(d.values())
print(d.items())

for k,v in d.items():
    print(k,v)

print('------------------------------------------------------------------')
tupple_d = (
    {'name': 'Ram', 'age': 45},
    {'name': 'Nick', 'age': 23},
    {'name': 'Jack', 'age': 32}
)

print(tupple_d)
print('Name = ', tupple_d[0]['name'], ', Age = ', tupple_d[0]['age'])
print('Name = ', tupple_d[1]['name'], ', Age = ', tupple_d[1]['age'])
print('Name = ', tupple_d[2]['name'], ', Age = ', tupple_d[2]['age'])

for each_element in tupple_d:
    print('Name = ', each_element['name'], ', Age = ', each_element['age'])

friends_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}

for name in friends_ages:
    print(f'Friend name {name}')

for age in friends_ages.values():
    print(f'Friend name {age}')

for name, age in friends_ages.items():
    print(f'Friend {name} is {age} years old')


guests = [('rolf', 25), ('adam', 28), ('jen', 24)]
d = dict(guests)
print(d)

###############################################################################
# Dict Comprehension
friends = ['Sam', 'bob', 'Jenny', 'divya', 'Sunil']
time_seen = [3, 2, 7, 10, 12]

long_time = {
    friends[i]: time_seen[i]
    for i in range(len(friends))
    if time_seen[i] > 5
}

print(long_time)

print(dict(zip(friends, time_seen)))

print(list(zip(friends, time_seen)))


