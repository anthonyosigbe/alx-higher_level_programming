#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
comparison_result = ''

if last_digit > 5:
    comparison_result = 'greater than 5'
elif last_digit < 6 and last_digit != 0:
    comparison_result = 'less than 6 and not 0'
else:
    comparison_result = '0'

print(f'Last digit of {number} is {"-" if number < 0 else ""}{last_digit} and is {comparison_result}')
