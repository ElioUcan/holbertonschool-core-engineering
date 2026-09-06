#!/usr/bin/env python3
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5
    print("{1} + {2} = {0}".format(add(a, b), a, b))
    print("{1} - {2} = {0}".format(subs(a, b), a, b))
    print("{1} * {2} = {0}".format(mul(a, b), a, b))
    print("{1} / {2} = {0}".format(div(a, b), a, b))
