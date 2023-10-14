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

    def update(self, *args, **kwargs):
        """Modify the Square.

        Args:
            *args (ints): Fresh attribute values.
                - The first argument represents the 'id' attribute.
                - The second argument corresponds to the 'size' attribute.
                - The third argument represents the 'x' attribute.
                - The fourth argument corresponds to the 'y' attribute.
            **kwargs (dict): Fresh sets of key/value attribute pairs.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
