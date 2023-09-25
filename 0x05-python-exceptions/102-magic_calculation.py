#!/usr/bin/python3
def magic_calculation(a, b):
    output = 0

    for num in range(1, 4):
        try:
            if num > a:
                raise Exception("Too far")
            output += (a ** b) / num
        except Exception:
            output += a + b
            break

    return output
