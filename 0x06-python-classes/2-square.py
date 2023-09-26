#!/usr/bin/python3
"""Declare a Square class."""


class Square:
    """Depict a square."""
    def __init__(self, size=0):
        """Instantiate a fresh Square.

        Args:
            size (int): The dimensions of the newly created square.

        Raises:
            TypeError: If the `size` is not of type `int`.

            ValueError: If the `size` is smaller than `0`.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
