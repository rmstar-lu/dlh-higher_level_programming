#!/usr/bin/python3
for i in range(ord("a"), ord("a") + 26):
    if not (i == ord("q") or i == ord("e")):
        print("{letter:c}".format(letter=i), end="")
