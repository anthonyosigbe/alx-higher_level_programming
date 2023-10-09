#!/usr/bin/python3
"""Introduces an inherited class-checking function."""


def inherits_from(obj, a_class):
    """Check if an object is an instance of a class that inherits
    (directly or indirectly) from a specified class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare the object's type to.

    Returns:
        True if obj is an instance of a class that inherits from a_class;
        otherwise, False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
