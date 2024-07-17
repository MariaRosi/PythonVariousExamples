# Set is unique unordered list
s1 = {10, 20, 30, 40}
s2 = {15, 20, 35, 45}

print(s1)
print(s2)

s1.add(40)
s2.add(60)

print(s1)
print(s2)

print(s1.difference(s2))
print(s2.difference(s1))

print(s1.symmetric_difference(s2))
print(s1.union(s2))

print(s1.intersection(s2))
##########################################################################
# Set Comprehension
# Find who among the friend were there in the guest list
friends = ['Sam', 'bob', 'Jenny', 'divya', 'Sunil']
guests = ['Sampath', 'bob', 'Jenny', 'somak', 'Neil']

friends_lower = {f.lower() for f in friends}
guests_lower = {g.lower() for g in guests}
friends_in_guest_list = {name.title() for name in friends_lower.intersection(guests_lower)}
print(friends_in_guest_list)