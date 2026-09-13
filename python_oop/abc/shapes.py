#!/usr/bin/env python3

from abc import ABC, abstractmethod

"""Shape class abstract"""

class Shape(ABC):
    """Shape abstract class"""
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    """Circle concrete class"""

    def __init__(self, radius = 0,):
        self.pi = 3.14
        self.radius = radius

    def area(self):
        return self.pi * (self.radius**2)

    def perimeter(self):
        return 2 * self.pi * self.radius

class Rectangle(Shape):
    """Rectangle class"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (2 * self.width) + (2 * self.height)

def shape_info(single):
    single.area()
    single.perimeter()

circle = Circle()
rectangle = Rectangle()
print(shape_info(circle))
print(shape_info(rectangle))




