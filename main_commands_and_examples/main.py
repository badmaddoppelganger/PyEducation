class TestClass:
    __slots__ = ["_name"]  # Restrict our attrs list from external changes

    def __init__(self):
        self._name = 'Alex'

    version = 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @name.deleter
    def name(self):
        del self._name
        print('Name deleted')


a = TestClass()
print(a.name)
a.name = 12
print(a.name)
#del a.name
print(a.name)
a.new_attr = 'Meow'
print(a.new_attr)
