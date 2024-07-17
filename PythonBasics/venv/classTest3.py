class Msg:
   def __init__(self):
       print('in __init__() for ', self)
   def __del__(self):
       print('in __del__() for', self)

def test_del_fn():
    m1 = Msg()
    m2 = Msg()

#test_del_fn()

def test4_del_fn():
    m1 = Msg()
    m2 = m1
    m3 = m2
    print('------1-------')
    del m1
    print('------2-------')
    del m2
    print('------3-------')
    del m3
    print('-------------')

test4_del_fn()