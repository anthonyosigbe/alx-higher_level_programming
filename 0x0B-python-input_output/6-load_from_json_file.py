#!/usr/bin/python3
"Describes a function for reading JSON data from a file."
import json


def load_from_json_file(filename):
    """Generate a Python object from a JSON file."""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
