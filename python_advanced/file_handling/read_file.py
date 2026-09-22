#!/usr/bin/env python3
"""
File opening handeling only read option

"""

def read_file(filename=""):

    """Reads a file from a given path"""

    with open(filename, mode="r", encoding="utf-8") as file:
        print(file.read())
