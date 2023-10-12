#!/usr/bin/python3
"""Establishes the foundation for a model class."""
import json


class Base:
    """Depict the foundational model.

    Serves as the fundamental building block for all other
    classes in Python - Almost a circle project.

    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Create a new instance of a Base.

        Args:
            id (int): The unique identifier of the newly created Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects