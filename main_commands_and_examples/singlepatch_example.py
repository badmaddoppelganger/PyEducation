from functools import singledispatch


class User:
    @singledispatch
    def get_value(value):
        print("default: ", value)

    @get_value.register(int)
    def _value(value):
        print("int: ", value)

    @get_value.register(str)
    def _value(value):
        print("str: ", value)


User.get_value([1, 2])
User.get_value(True)
User.get_value(1)
User.get_value("a")
