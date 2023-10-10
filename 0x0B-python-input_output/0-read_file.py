#!/usr/bin/python3
"""Describes a function for reading text files."""


def read_file(filename=""):
    """Display the contents of a UTF-8 text file on the standard output."""
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end="")
