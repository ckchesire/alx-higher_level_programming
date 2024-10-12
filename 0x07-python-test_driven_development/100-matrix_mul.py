#!/usr/bin/python3
"""Module to calculate dot matrix between matrices"""


def matrix_mul(m_a, m_b):
    """
    Function Multiplies two matrices m_a and m_b.

    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Returns:
        list of lists: returns the result of multiplying m_a by m_b.

    Raises:
        TypeError: If m_a or m_b is not a list, or not a list of lists,
                    or contains non-numeric data.
        ValueError: If m_a or m_b are empty or if the matrices cannot
                     be multiplied.
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(x, list) for x in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(x, list) for x in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for x in row:
            if type(x) is not int and type(x) is not float:
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for x in row:
            if type(x) is not int and type(x) is not float:
                raise TypeError("m_b should contain only integers or floats")

    row_len = []
    for row in m_a:
        row_len.append(len(row))
    if not all(elem == row_len[0] for elem in row_len):
        raise TypeError("each row of m_a must should be of the same size")
    row_len = []
    for row in m_b:
        row_len.append(len(row))
    if not all(elem == row_len[0] for elem in row_len):
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for i in range(len(m_a)):
        result_row = []
        for j in range(len(m_b[0])):
            sum_product = 0
            for k in range(len(m_b)):
                sum_product += m_a[i][k] * m_b[k][j]
            result_row.append(sum_product)
        result.append(result_row)

    return result
