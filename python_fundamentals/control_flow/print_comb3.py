#!/usr/bin/env python3

for i in range(9):
    for j in range(10):
        if i == 0:
            print("{:02d}".format(j), end=", ")
        elif i < 8 and  j != 0: #aqui
            if i != j and i < j: #Esto elimina el problema de los 11,22,33
                print("{0}{1}".format(i, j), end=", ")
        
print("{}".format(89))
