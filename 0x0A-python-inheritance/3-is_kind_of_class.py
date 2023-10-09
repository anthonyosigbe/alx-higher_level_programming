#!/usr/bin/python3
"""Introduces a class and an inherited function for checking class types."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of, or inherited from, a given class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare the object's type to.

    Returns:
        True if obj is an instance of a_class or any class derived from it;
        otherwise, False.
    """
    return isinstance(obj, a_class)
