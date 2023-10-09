#!/usr/bin/python3
"""Introduces a Rectangle class inheriting from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Symbolize a rectangle using BaseGeometry."""
    def __init__(self, width, height):
        """Initialize a new Rectangle.

        Arguments:
            width (int): Width of the new Rectangle.
            height (int): Height of the new Rectangle.
        """

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Provide the print() and str() representations of a Rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
