#!/usr/bin/python3
"""Declares a class named Student."""


class Student:
    "Depicting a student."
    def __init__(self, first_name, last_name, age):
        """Create a new instance of the Student class.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Obtain a dictionary that represents the Student.

        If 'attrs' is a list of strings, it represents only those attributes
        that are contained within the list.

        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr
                    in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """Update all of the Student's attribute.

        Args:
            json (dict): The key/value pairs to replace attributes with.
        """
        for key, value in json.items():
            setattr(self, key, value)
