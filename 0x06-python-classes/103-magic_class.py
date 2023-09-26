#!/usr/bin/python3
"""Create a MagicClass that mimics the functionality of a given bytecode."""


import math
"""Import the math module, which provides mathematical,
functions and constants.
"""


class MagicClass:
    """Define a Python class called MagicClass."""
    def __init__(self, radius=0):
        """
        Initialize a MagicClass object with a radius.

        Args:
            radius (int or float): The radius of the circle.

        Raises:
            TypeError: If the provided radius is not a number (int or float).
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = float(radius)

    def area(self):
        """
        Calculate and return the area of the circle.

        Returns:
            float: The calculated area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculate and return the circumference of the circle.

        Returns:
            float: The calculated circumference of the circle.
        """
        return 2 * math.pi * self.__radius
