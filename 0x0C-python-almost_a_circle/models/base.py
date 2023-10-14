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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Provide the JSON serialization of a list of dictionaries.

        Args:
            list_dictionaries (list): An array of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save the JSON serialization of a list of objects to a file.

        Args:
            list_objs (list): A collection of Base instances inherited,
            from a parent class.
        """
        filename = cls.__name__ + '.json'

        with open(filename, mode='w', encoding='utf-8') as f:
            if list_objs is None:
                return f.write(cls.to_json_string(None))

            json_attrs = []

            for elements in list_objs:
                json_attrs.append(elements.to_dictionary())

            return f.write(cls.to_json_string(json_attrs))

    @staticmethod
    def from_json_string(json_string):
        """Provide the process of deserializing a JSON string.

        Args:
            json_string (str): A JSON string representation,
            of a list of dictionaries.
        Returns:
            If the `json_string` is None or empty, return an empty list.
            Otherwise - The Python list that corresponds to the `json_string`.
        """
        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an instance of a class from a dictionary of attributes.

        Args:
            **dictionary (dict): Pairs of keys and values for,
            attribute initialization.
        """
        if cls.__name__ == 'Square':
            substitute = cls(3)

        if cls.__name__ == 'Rectangle':
            substitute = cls(3, 3)

        substitute.update(**dictionary)
        return substitute
