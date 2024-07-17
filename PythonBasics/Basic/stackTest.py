from pip._vendor.progress.counter import Stack

s2 = Stack()
s2.push(1000)
print(s2.pop())
s2.push('one')
s2.push('two')
s2.push('three')
print(s2.pop())
print(s2.pop())
print(s2.pop())