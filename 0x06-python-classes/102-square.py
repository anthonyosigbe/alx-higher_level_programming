#!/usr/bin/python3
"""Create a Square class."""


class Square:
    """A class that represents a square."""

    def __init__(self, size=0):
        """Initialize a square.

        Args:
            size (float or int): The side length of the square.
        """
        self.size = size

    @property
    def size(self):
        """Get or set the side length of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Size must be a number")
        elif value < 0:
            raise ValueError("Size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Compare two squares based on area for equality."""
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """Compare two squares based on area for inequality."""
        return not self.__eq__(other)

    def __lt__(self, other):
        """Compare two squares based on area for less than."""
        if isinstance(other, Square):
            return self.area() < other.area()
        return False

    def __le__(self, other):
        """Compare two squares based on area for less than or equal to."""
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        """Compare two squares based on area for greater than."""
        if isinstance(other, Square):
            return self.area() > other.area()
        return False

    def __ge__(self, other):
        """Compare two squares based on area for greater than or equal to."""
        return self.__gt__(other) or self.__eq__(other)
