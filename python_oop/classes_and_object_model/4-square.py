#!/usr/bin/env python3

"""Class that does nothing"""


class Square:
    """Does nothing"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """The  property size"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    def area(self):
        return self.__size * self.__size
