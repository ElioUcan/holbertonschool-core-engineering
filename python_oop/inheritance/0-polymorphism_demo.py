#!/usr/bin/env python3

class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"


dog = Dog()
print(isinstance(dog,Dog))
print(isinstance(dog,Animal))
print(issubclass(Dog, Animal))
