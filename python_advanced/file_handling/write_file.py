#!/usr/bin/env python3
"""
File opening handeling write option

"""


def write_file(filename="", text=""):
    """Writes something a file from a given path"""

    i = 0
    with open(filename, mode="w", encoding="utf-8") as file:
        for char in text:
            i += 1
        file.write(text)
        return i
