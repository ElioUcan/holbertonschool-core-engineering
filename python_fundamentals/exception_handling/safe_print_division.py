#!/usr/bin/env python3

def safe_print_division(a, b):
    try:
        result =  a / b 
    except Exception as e:
        print("Inside result: None")
        print("{0} / {1} = None".format(a, b))
        return None
    finally:
        print("Inside result: None")
        print("{0} / {1} = {2}".format(a, b, result))
        return result
