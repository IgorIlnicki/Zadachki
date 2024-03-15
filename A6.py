from collections import UserDict
from functools import reduce
import pickle
import datetime as dt
import re
from datetime import datetime as dtdt
import os

class Point:
    def __init__(self, x, y):
        # self.__x = None
        # self.__y = None
        self.x = x
        self.y = y

    # @property
    # def x(self):
    #     return self.__x

    # @x.setter
    # def x(self, x):
    #     if (type(x) == int) or (type(x) == float):
    #         self.__x = x

    # @property
    # def y(self):
    #     return self.__y

    # @y.setter
    # def y(self, y):
    #     if (type(y) == int) or (type(y) == float):
    #         self.__y = y


class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

    def __setitem__(self, key, value):
        if  key == 0:
            self.coordinates.x = value
        else:
            self.coordinates.y = value
        

    def __getitem__(self, index):
        if  index == 0:
            return self.coordinates.x
        else:
            return self.coordinates.y
            

if __name__ == "__main__":
    v: Vector = Vector(1,2)
    print(str(v[0]) + ' ' + str(v[1] ))

    

        
            