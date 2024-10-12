#!/usr/bin/python3
"""Module to perform matrix multiplication using NumPy
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """Multiplies m_a and m_b using matmul, and returns the result.

        Args:
            m_a (lists of lists): first matrix
            m_b (lists of lists): second matrix

        Returns:
            Returns matrix multiplication of m_a and m_b
    """
    return numpy.matmul(m_a, m_b)
