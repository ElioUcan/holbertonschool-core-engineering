#!/usr/bin/env python3
"""
File opening handeling only read option

"""

def read_file(filename=""):
    with open(filename, mode="r", encoding="utf-8") as file:
        print(file.read())
