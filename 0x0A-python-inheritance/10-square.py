#!/usr/bin/python3
"""Introduces a Square subclass of Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Symbolize a square."""

    def __init__(self, size):
        """Initiate a new square.

        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
