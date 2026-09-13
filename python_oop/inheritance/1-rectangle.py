#!/usr/bin/env python3

"""Rectangle class"""

BaseGeometry = __import__('base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    
    """Init of the class"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self._width = width
        self._height = height
