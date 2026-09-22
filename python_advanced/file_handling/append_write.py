#!/usr/bin/env python3

"""
append file

"""


def append_write(filename="", text=""):
    """Function that appends and returns the number of appended chars"""

    i = 0
    with open(filename, mode="a", encoding="utf-8") as f:
        for char in text:
            i += 1
        f.write(text)
        return i
