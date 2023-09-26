#!/usr/bin/ppython3
"""Create classes for a singly-linked list."""


class Square:
    """A class that represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square.

        Args:
            size (int): The side length of the square.
            position (tuple): The position of the square as (x, y).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get or set the side length of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("Size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get or set the position of the square as (x, y)."""
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using '#' characters and spaces."""
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Return a string representation of the square."""
        result = ""
        if self.__size != 0:
            for _ in range(self.__position[1]):
                result += "\n"
            for _ in range(self.__size):
                result += " " * self.__position[0] + "#" * self.__size
                if _ != self.__size - 1:
                    result += "\n"
        return result
