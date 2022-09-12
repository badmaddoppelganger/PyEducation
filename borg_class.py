class ThreadData:
    __shared_attrs = {
        'name': 'thread_1',
        'data': {},
        'id': 1,
    }

    def __init__(self):
        self.__dict__ = self.__shared_attrs


ts1 = ThreadData()
# print(ts1.__dict__)
ts2 = ThreadData()
# print(ts2.__dict__)

ts2.name = 5

print(ts1.__dict__)

print(ts2.__dict__)

b = [1, "2", ts1, 4, 5]

for i in b:
    
    i = 2
