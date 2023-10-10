#!/usr/bin/python3
"""Declares a function for Pascal's Triangle."""


def pascal_triangle(n):
    """Display Pascal's Triangle with a size of 'n'.

    Produces a list of lists containing integers that,
    represent the triangle.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle[:n]
