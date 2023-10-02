#!/usr/bin/python3
"""Specifies a function for adding integers."""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number,
    and returns a new matrix.

    Args:
        matrix (list of lists): The matrix to be divided.
        div (int or float): The number to divide all elements of the matrix by.

    Returns:
        list of lists: A new matrix with all elements divided by div.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats.
        TypeError: If rows of the matrix do not have the same size.
        TypeError: If div is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
