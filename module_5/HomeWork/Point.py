class Point:

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def get_point(self):
        return self.__x, self.__y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def setx(self, x):
        self.__x = x

    def sety(self, y):
        self.__y = y

    def addx(self, x):
        self.__x += x

    def addy(self, y):
        self.__y += y


point1 = Point()

print(point1.get_point())
print(point1.getx())
print(point1.gety())

point1.setx(5)
point1.addy(-2)
print(point1.get_point())
