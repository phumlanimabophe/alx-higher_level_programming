#!/usr/bin/python3
"""Module 2-matrix_divided.

This module contains the function matrix_divided that divides all the
elements of a matrix by a divisor.

"""


def matrix_divided(matrix, div):
    """Divide all the elements of a matrix by a divisor.

    Args:
        matrix (list of lists): The matrix to divide.
        div (int or float): The divisor.

    Returns:
        list of lists: A new matrix with the quotients rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats, or if div is not a number.
        ZeroDivisionError: If div is 0.

    """
    if not isinstance(matrix, list) or any(not isinstance(row, list) for row in matrix):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

    num_columns = len(matrix[0])
    if any(len(row) != num_columns for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    new_matrix = []
    for row in matrix:
        new_row = [round(value / div, 2) for value in row]
        new_matrix.append(new_row)

    return new_matrix




