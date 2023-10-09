#!/usr/bin/python3
"""Specifies a function for checking the class type."""


def is_same_class(obj, a_class):
    """Check whether an object is precisely an instance of a specific class.

    Args:
        obj (any): The object being examined.
        a_class (type): The class to which the type of obj is compared.

    Returns:
        True if obj is a direct instance of a_class; otherwise, False.
    """
    return type(obj) is a_class
