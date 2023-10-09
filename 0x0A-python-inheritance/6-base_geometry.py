#!/usr/bin/python3
"""Creates a class named BaseGeometry with no attributes or methods."""


class BaseGeometry:
    """Symbolizes base geometry."""

    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")
