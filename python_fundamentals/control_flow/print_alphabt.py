#!/usr/bin/env python3

letter = "abcdefghijklmnqoprstuvwxyz"
noletter = ""
for h in letter:
    if h != "e" and h != "q":
        noletter += h
print("{}".format(noletter), end="")
