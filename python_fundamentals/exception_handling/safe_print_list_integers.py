#!/usr/bin/env python3

def safe_print_list_integers(my_list=[], x=0):
    j = 0
    for i in range(my_list):
        try:
            print("{:d}".format(my_list[i]), end="")
            j+=1
        except Exception as e:
            continue
    print()
    return j
