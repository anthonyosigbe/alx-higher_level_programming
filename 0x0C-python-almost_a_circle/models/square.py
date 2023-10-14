#!/usr/bin/python3
"""Specifies a class for squares."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Depict a square."""
    def __init__(self, size, x=0, y=0, id=None):
        """Create a new instance of a Square.

        Args:
            size (int): The size of the newly created Square.
            x (int): The horizontal coordinate (x) of the newly,
            created Square.
            y (int): The vertical coordinate (y) of the newly,
            created Square.
            id (int): The unique identifier of the newly created Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Retrieve or modify the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
