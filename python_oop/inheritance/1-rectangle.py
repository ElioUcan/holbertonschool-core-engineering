#!/usr/bin/env python3

from base_geometry import BaseGeometry


"""Rectangle class"""


class Rectangle(BaseGeometry):
    
    """Init of the class"""

    def __init__(self, width, height):
        self.integer_validator(width)
        self.integer_validator(height)
        self._width = width
        self._height = height
