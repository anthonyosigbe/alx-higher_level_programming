#!/usr/bin/python3
"""Specifies an algorithm for finding peaks."""


def find_peak(list_of_integers):
    """Retrieve a peak from an unsorted list of integers."""
    if list_of_integers is None or len(list_of_integers) == 0:
        return None

    if len(list_of_integers) == 1:
        return list_of_integers[0]

    middle = int(len(list_of_integers) / 2)

    if middle != len(list_of_integers) - 1:
        if list_of_integers[middle - 1] < list_of_integers[middle] and\
           list_of_integers[middle + 1] < list_of_integers[middle]:
            return list_of_integers[middle]
    else:
        if list_of_integers[middle - 1] < list_of_integers[middle]:
            return list_of_integers[middle]
        else:
            return list_of_integers[middle - 1]

    if list_of_integers[middle - 1] > list_of_integers[middle]:
        a_list = list_of_integers[0:middle]
    else:
        a_list = list_of_integers[middle + 1:]

    return find_peak(a_list)
