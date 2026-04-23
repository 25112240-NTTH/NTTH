import math
class Point:
    def __init__(self, x=0, y=1):
        self.__x = x
        self.__y = y
    def read(self):
        data = input().split()
        self.__x = int(data[0])
        self.__y = int(data[1])
    def print(self):
        print(f'({self.__x}, {self.__y})')
    def move(self, dx, dy):
        self.__x = self.__x + dx
        self.__y = self.__y + dy
    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y
    def distance(self):
        return math.sqrt(self.__x**2 + self.__y**2)
    def distance_point(self, p):
        return math.sqrt((self.__x - p.get_x())**2 + (self.__y - p.get_y())**2)
