class StringVar:

    def __init__(self, data):
        self.__string = data

    def get(self):
        return self.__string

    def set(self, data):
        self.__string = data


a = StringVar('test1')
print(a.get())
a.set("test2")
print(a.get())


