#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5
    calc = [add, sub, mul, div]
    sign = ['+', '-', '*', '/']

    for i in range(0, 4):
        print("{} {} {} = {}".format(a, sign[i], b, calc[i](a, b)))