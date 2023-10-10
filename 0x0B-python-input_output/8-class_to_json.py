#!/usr/bin/python3
"""Describes a function for converting a Python class to JSON format."""


def class_to_json(obj):
    """Provide the dictionary representation of a basic data structure."""
    return obj.__dict__
