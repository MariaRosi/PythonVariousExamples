class Base(object):
   def f1(self):
      print("Base::f1")
   def f2(self):
      print("Base::f2")
   def f3(self):
      print("Base::f3")
class Derv(Base):
   def f1(self):
      print("Derv::f1")
   def f3(self):
      print("Derv::f3")
      super(Derv, self).f3()

def BaseTest():
    b = Base()
    d = Derv()

    b.f1()
    b.f2()
    b.f3()
    print("------")
    d.f1()
    d.f2()
    d.f3()

BaseTest()