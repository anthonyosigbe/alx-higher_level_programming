#!/usr/bin/python3
"""Creates a class named BaseGeometry with no attributes or methods."""


class BaseGeometry:
    """Symbolizes base geometry."""

    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Verify that a parameter is an integer.

        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """

        if type(value) is not int:
            raise TypeError(name + ' must be an integer')
        if value <= 0:
            raise ValueError(name + ' must be greater than 0')
