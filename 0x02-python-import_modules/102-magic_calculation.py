#!/usr/bin/python3
from magic_calculation_102 import add, sub
def magic_calculation(a, b):
    if (a < b):
        c = add(a, b)
    for func in range(4, 6):
        c = add(c, func)
        return (c)
    else:
        return (sub(a, b))
