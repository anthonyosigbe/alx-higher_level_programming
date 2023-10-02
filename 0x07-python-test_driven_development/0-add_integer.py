#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two integers or floats and returns the result as an integer.

    Args:
        a (int, float): The first number to be added.
        b (int, float, optional): The second number to be added.
        Defaults to 98.

        Returns:
        int: The integer result of adding a and b.

        Raises:
            TypeError: If a or b is not an integer or float.
    """

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
