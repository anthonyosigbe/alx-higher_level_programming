#!/usr/bin/python3
for Digit in range(10):
    for digit in range(10):
        if (Digit != digit and Digit < digit) and Digit < 9:
            if (Digit == 8 and digit == 9):
                print("{}{}".format(Digit, digit))
            else:
                print("{}{}, ".format(Digit, digit), end="")
