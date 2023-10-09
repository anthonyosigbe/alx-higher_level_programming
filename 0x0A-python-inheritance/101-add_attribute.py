#!/usr/bin/python3
"""Introduces a function for adding attributes to objects."""


def add_attribute(obj, attribute, value):
    """Add a new attribute to an object if possible;
        otherwise, raise a TypeError.

    Args:
        obj (object): The object to add the attribute to.
        attribute (str): The name of the attribute.
        value (any): The value to assign to the attribute.

    Raises:
        TypeError: If the object doesn't allow adding attributes.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
