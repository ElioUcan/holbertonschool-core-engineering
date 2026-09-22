#!/usr/bin/env python3
"""
File opening handeling only read option

"""


def read_file(filename=""):
    """Reads a file from a given path"""

    i = 0
    with open(filename, mode="r", encoding="utf-8") as file:
        for line in file:
            for char in line:
                i += 1
        return i
