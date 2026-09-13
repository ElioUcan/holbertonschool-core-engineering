#!/usr/bin/env python3



class Fish:

    """Class defining a Fish"""

    def swim(self):
        print("The Fish is swimming")
    def habitat(self):
        print("The fish lives in water")


class Bird:

    """Class defining a bird"""

    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")

class FlyingFish(Bird, Fish):

    """The flying fish class"""

    def fly(self):
        print("The flying fish is soaring")
    def swim(self):
        print("The flying fish is swimming")
    def habitat(self):
        print("The flying fish lives both in water and the sky!")

flyingfish = FlyingFish()

flyingfish.fly()
flyingfish.swim()
flyingfish.habitat()

mro(flyingfish)
