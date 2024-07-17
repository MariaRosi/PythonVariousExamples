class Point:
    def __init__(self, tx, ty):
        self.x = tx
        self.y = ty

    def getx(self): return self.x

    def gety(self): return self.y

    def setx(self, tx): self.x = tx

    def sety(self, ty): self.y = ty

    def __repr__(self):
        return f"Point({self.x},{self.y})"

def test_point():
    p1 = Point(1,5)
    print( 'p1 -', p1)
    p2 = Point(3,10)
    print( 'p2 -', p2)
    p1.setx(10)
    p1.sety(20)
    print( 'p1 -', p1)
    print( 'p1.x =', p1.getx())
    print( 'p1.y =', p1.gety())

test_point()