#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
if last_digit > 5:
    result_str = "Last digit of {0} is {1} and is greater than 5"
elif last_digit < 6 and last_digit != 0:
    result_str = "Last digit of {0} is {1} and is less than 6 and not 0"
else:
    result_str = "Last digit of {0} is {1} and is 0"
print(result_str.format(number, last_digit))
