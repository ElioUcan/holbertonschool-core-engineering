#!/usr/bin/env python3
def pow(a,b):
    x = 1
    y = b
    if b == 0:
        return 1
    if b  < 0:
        y = (b * -1)
    for i in range(y):
        if b < 0:
            x /= a
        else:
            x *= a
    return(x)
