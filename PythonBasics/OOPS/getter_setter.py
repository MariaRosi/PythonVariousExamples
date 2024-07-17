class Fruit:
    def __init__(self, name: str):
        self._name = name

    @property
    def fruit_name(self):
        print('Inside fruit_name getter')
        return self._name

    @fruit_name.setter
    def fruit_name(self,value: str):
        print('Inside fruit_name setter ')
        self._name = value


f = Fruit('Banana')
print(f.fruit_name)
f.fruit_name == 'Orange'
print(f.fruit_name)
