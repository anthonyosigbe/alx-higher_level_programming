#!/usr/bin/python3
"""Introduces a derived list class called MyList."""


class MyList(list):
    """Introduces sorted printing functionality for the standard list class."""
    def print_sorted(self):
        """Display a list in ascending sorted order."""
        sorted_list = sorted(self)
        print(sorted_list)
