#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    print(len(argv) - 1, end="")
    if len(argv) == 2:
        print(" argument:")
    elif len(argv) == 1:
        print(" arguments.")
    else:
        print(" arguments:")
    for i in range(1, len(argv)):
        print("{0}: {1}".format(i, argv[i]))
