#!/usr/bin/env python3
def pow(a,b):
    x = 1
    if b == 0:
        return 1
    for i in range(b):
        x *= a
    return(x)
