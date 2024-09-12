#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    ln = len(sys.argv)
    print("{} arguments:".format(ln - 1))

    for i in range(1, ln):
        print("{}: {}".format(i, sys.argv[i]))
