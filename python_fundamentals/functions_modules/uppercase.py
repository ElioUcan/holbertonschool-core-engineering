#!/usr/bin/env python3
def uppercase(str):
    upper = ""
    for char in str:
        letter = ord(char)
        if letter >= 97:
            upper += chr(letter - 32)
        else:
            upper += char
    print("{}".format(upper))
