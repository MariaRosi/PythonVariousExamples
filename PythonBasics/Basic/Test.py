class INT:
    def __init__(self, k):
        self.val = k

    def __repr__(self):
        return 'INT(%d)' % (self.val)

    def __add__(self, rhs):
        if isinstance(rhs, int):
            return INT(self.val + rhs)
        elif isinstance(rhs, INT):
            return INT(self.val + rhs.val)
        else:
            return None


def test_INT():
    x1 = INT(2)
    x2 = INT(4)

    print(x1)
    print(x2)

    x3 = x1 + x2
    print(x3)
    print(type(x3))

    x4 = x3 + INT(2)
    print(x4)

    x4 = x3 + x2
    print(x4)

    x5 = x3 + x2 + x1
    print(x5)

    x5 += x2
    print(x5)

test_INT()