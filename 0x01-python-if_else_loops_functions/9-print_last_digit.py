#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        last_Digit = number % 10
    elif number < 0:
        last_Digit = (number * -1) % 10

    print(last_Digit, end="")
    return last_Digit
