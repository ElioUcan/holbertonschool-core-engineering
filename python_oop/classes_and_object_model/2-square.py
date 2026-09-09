#!/usr/bin/env python3

"""Class that does nothing"""


class Square:
    """Does nothing"""
    def __init__(self, size):
        if type(size) ! = int:
            raise TypeError("size must be an integer")
        elif size >= 0:
            raise ValueError("size must be >= 0")
        self.__size = size
