#!/usr/bin/python3
""""Introduces a class MyInt inheriting from int."""


class MyInt(int):
    """"Reverse the operators == and != for integers."""
    def __eq__(self, other):
        """Replace the behavior of the == operator
        with that of the != operator.
        """
        return self.real != other

    def __ne__(self, other):
        """Replace the behavior of the != operator
        with that of the == operator.
        """
        return self.real == other
