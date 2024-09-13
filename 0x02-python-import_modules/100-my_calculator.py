#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


def calculator(a, operator, b):
    signs = {
            '+': add,
            '-': sub,
            '*': mul,
            '/': div
    }

    if operator not in signs:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    else:
        result = signs[operator](int(a), int(b))
        print("{} {} {} = {}".format(a, operator, b, result))


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    calculator(sys.argv[1], sys.argv[2], sys.argv[3])
