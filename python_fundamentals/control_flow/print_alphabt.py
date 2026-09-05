#!/usr/bin/env python3

letter = "abcdefghijklmnqoprstuvwxyz"
noletter = ""
for l in letter:
    if l != "e" or l != "q":
        noletter += l
print("{}".format(noletter))

