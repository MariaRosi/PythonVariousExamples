class Msg:
    def set(self, s):  # define member method set
        self.txt = s  # introduce attribute named "txt"

    def get(self):
        return self.txt

    def concat(self,s):
        self.txt = self.txt + s


m1=Msg("TS: ")
m1.concat(1,'-Jan-',2017)
print(m1.txt)
m2=Msg('')
m2.concat(m, ' ', 10,':', 15, ':', 25, ' AM')
print(m2.txt)