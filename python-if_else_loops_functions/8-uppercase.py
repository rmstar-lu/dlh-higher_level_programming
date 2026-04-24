#!/usr/bin/python3
def uppercase(str):
    upper = ""
    for c in str:
        if "a" <= c <= "z":
            upper += chr(ord("A") + ord(c) - ord("a"))
        else:
            upper += c
    print("{0}".format(upper))
