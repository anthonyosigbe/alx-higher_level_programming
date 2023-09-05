#!/usr/bin/python3
for ASCII in range(97, 123):
    if (ASCII != 101 and ASCII != 113):
        print("{:c}".format(ASCII), end="")
