#!/usr/bin/python3
"""Establishes a function for printing squares."""


def print_square(size):
    """
    Prints a square of '#' characters with the given size.

    Args:
        size (int): The size (length) of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
