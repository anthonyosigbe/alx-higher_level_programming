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

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
