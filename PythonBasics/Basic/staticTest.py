class Dummy:
    count = 100  # static data

    def __init__(self, a, b):
        self.__x = a
        self.__y = b
        print(id(self), id(self.__x), id(self.__y), '*', id(self.count))

    @staticmethod  # decorator
    def getcount():
        return Dummy.count

    @staticmethod  # decorator
    def setcount(v):
        Dummy.count = v


def test_Dummy():
    d1 = Dummy(100, 200)
    d2 = Dummy(300, 400)

    print(Dummy.getcount())
    print(Dummy.getcount())
    Dummy.setcount(1000)
    print(Dummy.getcount())

test_Dummy()