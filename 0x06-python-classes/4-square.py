#!/usr/bin/python3
"""Create a Square class."""


class Square:
    """Depict a square."""
    def __init__(self, size=0):
        """Instantiate a fresh Square.

        Args:
            size (int): The dimensions of the newly created square.
        """
        self.__size = size

    @property
    def size(self):
        """Retrieve or modify the current square size."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Provide the current square's area."""
        return self.__size ** 2
