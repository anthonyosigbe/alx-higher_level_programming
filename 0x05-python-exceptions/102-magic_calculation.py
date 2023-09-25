#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for item in range(1, 3):
        try:
            if item > a:
                raise Exception('Too far')
            else:
                result += a ** b / item
        except Exception:
            result = b + a
            break
    return (result)
