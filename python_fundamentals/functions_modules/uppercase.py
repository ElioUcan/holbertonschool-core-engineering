#!/usr/bin/env python3
def uppercase(str):
    upper = ""
    for char in str:
        upper += chr(ord(char) + 25)
    print(upper)
