class Time:
  def __init__(self,h=0,m=0,s=0):
     self.__h = h
     self.__m = m
     self.__s = s
  def __repr__(self):
     return 'Time(%d:%d:%d)' % (self.__h, self.__m, self.__s)
  def __add__(self, rhs):
      t = Time()
      t.__h = self.__h + rhs.__h
      t.__m = self.__m + rhs.__m
      t.__s = self.__s + rhs.__s
      return t

  def __eq__(self, rhs):
      return (self.__h == rhs.__h) and (self.__m == rhs.__m) and (self.__s == rhs.__s)

  def __ne__(self, rhs):
      return not self.__eq__(rhs)

def test_Time():
    t1 = Time(9, 15, 30)
    t2 = Time(5, 20, 50)

    t3 = t1 + t2
    print(t3)

    print(t1==t2)

test_Time()