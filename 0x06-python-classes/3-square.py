#!/usr/bin/python3
"""Create a Square class."""


class Square:
    """Depict a square."""
    def __init__(self, size=0):
        """Instantiate a fresh Square.

        Args:
            size (int): The dimensions of the newly created square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Provide the current square's area."""
        return self.__size ** 2
