#!/usr/bin/python3
for i in range(ord('z'),ord('a') - 1,-1):
    if i % 2 == 1:
        i += ord('A') - ord('a')
    print("{0:c}".format(i), end="")
