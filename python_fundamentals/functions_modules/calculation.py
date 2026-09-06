#!/usr/bin/env python3
from calculator_1 import addition, substraction, multiplication, division

if __name__ == "__main__":
    a = 10
    b = 5
    print("{1} + {2} = {0}".format(addition(a, b), a, b))
    print("{1} - {2} = {0}".format(substraction(a, b), a, b))
    print("{1} * {2} = {0}".format(multiplication(a, b), a, b))
    print("{1} / {2} = {0}".format(division(a, b), a, b))
