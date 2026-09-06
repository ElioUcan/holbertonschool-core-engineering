#!/usr/bin/env python3
def pow(a, b):
    x = 1
    y = b
    if b == 0:
        return 1
    if b < 0:
        y = -b
    for i in range(y):
        x *= a
    if b < 0:
        return 1 / x
    return x
