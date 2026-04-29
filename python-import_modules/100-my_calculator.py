#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a, op, b = argv[1:]
    if op == "+":
        result = add(int(a), int(b))
    elif op == "-":
        result = sub(int(a), int(b))
    elif op == "*":
        result = mul(int(a), int(b))
    elif op == "/":
        result = div(int(a), int(b))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{0} {1} {2} = {3}".format(a, op, b, result))
