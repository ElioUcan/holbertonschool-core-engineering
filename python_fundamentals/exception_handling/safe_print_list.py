#!/usr/bin/env python3

def safe_print_list(my_list=[], x=0):
    if x == 0:
        print(x)
        return 
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except Exception as e:
            return i+1
    print()
    return i+1
