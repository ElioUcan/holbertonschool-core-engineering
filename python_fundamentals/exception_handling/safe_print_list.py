#!/usr/bin/env python3

def safe_print_list(my_list=[], x=0):
    if x == 0:
        print()
        return 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except Exception as e:
            print()
            return i
    print()
    return i+1
