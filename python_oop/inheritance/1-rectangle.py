#!/usr/bin/env python3
BaseGeometry = __import__('base_geometry').BaseGeometry


"""Rectangle module"""
class BaseGeometry:

    """Raises an error if the area method is not implemented"""
    def area(self):
        raise Exception("area() is not implemented")

    """Checks for the value to be an int or greater than 0"""

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

"""Rectangle class"""

class Rectangle(BaseGeometry):
    
    """Init of the class"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self._width = width
        self._height = height
