#!/usr/bin/env python3

def safe_print_list_integers(my_list=[], x=0):
    # lo que falta es solo condicional para que el array no imprima 
    # mas que el valor de X y ya coneso estaria 
    i = 0
    for j in range(x):
        try:
            print("{:d}".format(my_list[j]), end="")
            i+=1
        except Exception as e:
            continue
    print()
    return i
