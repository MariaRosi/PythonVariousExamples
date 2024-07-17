class Stack:
   def __init__(self):
     self.__stk=[ ]
   def push(self,v):
     self.__stk.append(v)
   def pop(self):
      if len(self.__stk) == 0:
          raise StackEmpty()
      else:
          return self.__stk.pop()

def SuperTest():
    try:
        s = Stack()
        s.push(10)
        s.push(20)
        print(s.pop())
        print(s.pop())
        print(s.pop())
    except StackEmpty as e:
        print(e)
SuperTest()