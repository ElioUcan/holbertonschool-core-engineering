#!/usr/bin/env python3
number = __import__('random').randint(-10,10)
if number > 0:
    print(f"98 is positive")
elif number < 0:
    print(f"-98 is negative")
else:
    print(f"0 is zero")
