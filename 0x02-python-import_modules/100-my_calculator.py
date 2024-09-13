#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    
    sign = ['+','-','*','/']
    ln = len(sys.argv)

    if (ln - 1) != 3:
        sys.stderr.write("Usage: ./100-my_calculator.py <a> <operator> <b>\n")
        sys.exit(1)
    else:
        if sys.argv[2] not in sign:
            sys.stderr.write("Unknown operator. Available operators: +, -, * and /\n")
            sys.exit(1)
        else:
            a = int(sys.argv[1])
            b = int(sys.argv[3])
            s = sys.argv[2]

            if s == '+':
                print("{} {} {} = {}".format(a, s, b, add(a, b)))
            elif s == '-':
                print("{} {} {} = {}".format(a, s, b, sub(a, b)))
            elif s == '*':
                print("{} {} {} = {}".format(a, s, b, mul(a, b)))
            elif s == '/':
                print("{} {} {} = {}".format(a, s, b, div(a, b)))
