#!/usr/bin/env python3


"""Base geometry class template made for other classes"""

class BaseGeometry:

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self,name,value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

