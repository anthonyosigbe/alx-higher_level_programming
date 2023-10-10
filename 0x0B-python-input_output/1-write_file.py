#!/usr/bin/python3
"""Describes a function for writing to files."""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        nb_characters = file.write(text)
    return nb_characters
