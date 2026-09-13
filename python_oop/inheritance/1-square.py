#!/usr/bin/env python3

"""Class of a square"""

Rectangle = __import__("2-rectangle").Rectangle


class Square(Rectangle):
    """Class of a square"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self._size = size

    def area(self):
        return self._size**2
