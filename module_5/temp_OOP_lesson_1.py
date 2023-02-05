

class Student:

    tired = 0
    progress = 0

    def __init__(self, name):
        self.name = name

    def study(self):
        self.progress += 10
        self.tired += 15

    def relax(self):
        if self.tired > 5:
            self.tired -= 5
        else:
            self.tired = 0

    def is_done(self):
        if self.progress == 100:
            print("DONE")
        else:
            print("Not yet :(")


class Stack:

    def __init__(self, data):
        self.data = data

    def push(self, x):
        self.data.append(x)

    def pop(self):
        if self.data:
            element = self.data[-1]
            del self.data[-1]
            return element


class Matrix:

    def __init__(self, data):
        self.data = data
        self.n = len(data)
        self.m = len(data[0])

    def __add__(self, other):
        if self.m == other.m and self.n == other.n:
            data1 = []
            for i in range(self.n):
                current_data = []
                for j in range(self.m):
                    current_data.append(self.data[i][j] + other.data[i][j])
                data1.append(current_data)
            return Matrix(data1)
        else:
            return "Wrong dimension"


m1 = Matrix([[1, 5], [2, 6]])
m2 = Matrix([[3, 2], [4, 1]])

m3 = m1 + m2

print(m3.data)

#
# s = Student('MAX')
#
# print(s.name, ":", s.tired, s.progress)
#
# massive = Stack([1, 4, 8])
#
# massive.push(3)
#
# for i in range(7):
#     print(massive.pop())
#
