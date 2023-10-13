#!/usr/bin/python3
"""Specifies a class for rectangles."""
from models.base import Base


class Rectangle(Base):
    """Depict a rectangle."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Create a new instance of a Rectangle.

        Args:
            width (int): The width of the newly created Rectangle.
            height (int): The height of the newly created Rectangle.
            x (int): The horizontal coordinate (x) of the newly
            created Rectangle.
            y (int): The vertical coordinate (y) of the newly
            created Rectangle.
            id (int): The unique identifier of the newly created Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Modify or retrieve the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Adjust or obtain the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Adjust or retrieve the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Adjust or obtain the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Retrieve the area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """Display the Rectangle using the `#` character."""
        if self.width == 0 or self.height == 0:
            print("")
            return
        [print("") for y in range(self.y)]
        for i in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")
