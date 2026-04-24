#!/usr/bin/python3
def uppercase(str):
    for c in str[:-1]:
        if "a" <= c <= "z":
            letter = ord("A") + ord(c) - ord("a")
        else:
            letter = ord(c)
        print("{0:c}".format(letter), end="")
    c = str[-1]
    if "a" <= c <= "z":
        letter = ord("A") + ord(c) - ord("a")
    else:
        letter = ord(c)
    print("{0:c}".format(letter))
