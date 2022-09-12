"""Data class for set/get methods"""


class Data:
    """Replace the props of method"""

    def __init__(self):
        self.value: str = ""
        print("activated")

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = value
