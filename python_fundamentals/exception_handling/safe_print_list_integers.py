#!/usr/bin/env python3

def safe_print_list_integers(my_list=[], x=0):
    i = 0
    for value in range(my_list):
        try:
            print("{:d}".format(value), end="")
            i+=1
        except Exception as e:
            continue
    print()
    return i
