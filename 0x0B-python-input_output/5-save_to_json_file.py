#!/usr/bin/python3
"""Describes a function for writing JSON data to a file."""
import json


def save_to_json_file(my_obj, filename):
    """Store an object in a text file using its JSON representation."""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
