class User:
    def __init__(self, value=10):
        self.value = value

    def __call__(self, comment):
        print("Call: ", self.value)
        print("Comment: ", comment)


a = User()
a("test")
