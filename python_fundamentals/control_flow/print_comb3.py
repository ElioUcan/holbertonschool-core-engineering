#!/usr/bin/env python3

for i in range(9):
    for j in range(10):
        if i < 8 and  j != 0:
            if i != j and i < j: #Esto elimina el problema de los 11,21,32,etc.
                print("{0}{1}".format(i, j), end=", ")
        
print("{}".format(89))
