#!/usr/bin/python3
"""Describes a function for lookup attributes of an object."""


def lookup(obj):
    """Returns a list of attributes accessible for an object."""
    return dir(obj)
