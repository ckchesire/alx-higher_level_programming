#!/usr/bin/python3
""" Module for matrix division """


def matrix_divided(matrix, div):
    """Function divides a matrix by a number

        Args:
            matrix (list): list of integers or floats
            div (int, float): number to divide matrix with

        Raises:
            TypeError: matrix must be a matrix (list of lists) of
                        integers/floats
            TypeError: Each row of the matrix must have the same size
            TypeError: div must be a number
            ZeroDivisionError: division by zero

        Returns:
            Returns a new matrix list divided by the number rounder to 2
            decimal places
    """
    error_str = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or \
            not all(isinstance(row, list)for row in matrix):
        raise TypeError(error_str)

    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        if not all(isinstance(elem, (int, float)) for elem in row):
            raise TypeError(error_str)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for i in range(len(matrix)):
        temp = []
        for j in range(len(matrix[i])):
            if not isinstance(matrix[i][j], (int, float)):
                raise TypeError(error_str)
            res = matrix[i][j] / div
            res = round(res, 2)
            temp.append(res)
        new_matrix.append(temp)

    return new_matrix
