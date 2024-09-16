#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for row in range(len(matrix)):
            for column in range(len(matrix[row])):
                if column == (len(matrix[row]) - 1):
                    space = ""
                else:
                    space = " "
                print("{}".format(matrix[row][column]), end=space)
            print()
