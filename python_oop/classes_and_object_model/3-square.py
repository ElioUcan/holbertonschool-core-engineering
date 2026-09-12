#!/usr/bin/env python3

"""Class that does nothing"""

class Square:
    """Does nothing"""

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self, side = 0):
        self.side = side
        return self.__size * self.side
