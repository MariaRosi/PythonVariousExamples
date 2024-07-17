l = ['a', 'b', 'c', 'd']
l2 = ['x', 'y',]
print(l)

l.append('e')
print(l)

l.insert(2, 'g')
print(l)

l.extend(l2)
print(l)

l.remove('b')
print(l)

popped = l.pop() #removes last element
print(popped) #returns the last element
print(l)

l.reverse()
print(l)

l.sort(reverse=True)
print(l)
sorted_l = sorted(l) #doesn't alter the original list, returns another list

print(l[2])
print(l[2:])
print(l[:-1])
for each_element in l:
    print(each_element)

if 'd' in l:
    print(l.index('d'))
print('--------------------------------------------------------')

lst_numbers = [23, 45, 76, 89]
print('Min = ', min(lst_numbers))
print('Max = ', max(lst_numbers))
print('Sum = ', sum(lst_numbers))
print('Length = ', len(lst_numbers))
print('Average = ', sum(lst_numbers)/len(lst_numbers))

print('--------------------------------------------------------')
friends = ['Sanya', 'Divya', 'Rabeya']
print(friends)
comma_separated_friends = ", ".join(friends)
print(f'My friends are {comma_separated_friends}')

friends_ages = [("Rolf", 24), ("Adam", 30), ("Anne", 27)]
for name, age in friends_ages:
    print(f'Friend {name} is {age} years old')

friend_name = input('Enter the fiend name')
friends = ["Rolf", "Adam", "Bob"]
friends_lower = [friend.lower() for friend in friends]

if friend_name.lower() in friends_lower:
    print(f'{friend_name.title()} is in your friend list')
else :
    print(f'{friend_name.title()} is not in your friend list')

lst_double = [i * 2 for i in range(5)]
print(lst_double)

##########################################################
# List Comprehension
# Find who among the friend were there in the guest list
# Approach 1
friends = ['Sam', 'bob', 'Jenny', 'divya', 'Sunil']
guests = ['Sampath', 'bob', 'Jenny', 'somak', 'Neil']

friends_lower = [f.lower() for f in friends]

friends_in_guest_list = [
    g.title()
    for g in guests
    if g.lower() in friends_lower
]

print(friends_in_guest_list)

# Approach 2
friends = ['Sam', 'bob', 'Jenny', 'divya', 'Sunil']
guests = ['Sampath', 'bob', 'Jenny', 'somak', 'Neil']

friends_lower = set([f.lower() for f in friends])
guests_lower = set([g.lower() for g in guests])

print(guests_lower.intersection(friends_lower))

################################################################
# Enumerate Function, create list of tupple with index number for each element
friends = ['Sam', 'bob', 'Jenny', 'divya', 'Sunil']

for counter,friend in enumerate(friends, start=1):
    print(counter,friend)

print(list(enumerate(friends)))
print(dict(enumerate(friends)))
print(list(zip([1, 2, 3, 4, 5], friends)))

