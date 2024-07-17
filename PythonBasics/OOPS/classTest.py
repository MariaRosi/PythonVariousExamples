class Msg:
    def set(self, s):  # define member method set
        self.txt = s  # introduce attribute named "txt"

    def get(self):
        return self.txt

    def clear(self):
        self.txt = None


def test1_Msg():
    m = Msg()
    m.set("hello")  # set(m, "hello")
    print(m.get())

    m.set("HELLO")
    print(m.get())

    m2 = Msg()
    m2.set("python")

    print(m2.get())

    m2.clear()
    print(m2.get())


test1_Msg()