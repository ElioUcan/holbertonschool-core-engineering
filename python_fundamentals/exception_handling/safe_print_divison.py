#!/usr/bin/env python3

def safe_print_division(a, b):
    try:
        result =  a / b 
    except Exception as e:
        print("Inside result: None")
        return None
    finally:
        print("Inside result: {}".format(result))
        return result
