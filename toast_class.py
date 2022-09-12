from class_data import Data


class ToastClass:
    #  __slots__ = ["name", "surname", "new_attr"]  # Restrict our attrs list from external changes
    name = Data()
    surname = Data()

    @staticmethod
    def concat_fullname(name, surname):
        print(name + " " + surname)
        return name + " " + surname


textfile = ToastClass()

textfile.new_attr = "Bahodirovich"
print(textfile.name)
textfile.name = "Alex"
textfile.surname = "Morph"
ToastClass.concat_fullname(textfile.name, textfile.surname)
print(textfile.name)
print(type(textfile.name))
