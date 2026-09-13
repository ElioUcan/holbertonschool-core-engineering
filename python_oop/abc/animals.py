#!/usr/bin/env python3

from abc import ABC, abstractmethod

class Animal(ABC):
    """Abstact class for defining animal behaviour"""

    @abstractmethod
    def sound(self):
        """Am amimal makes a sound"""
        pass


class Dog(Animal):
    """Dog"""
    def sound(self):
        return "Bark"

class Cat(Animal):
    """Cat"""
    def sound(self):
        return "Meow"
