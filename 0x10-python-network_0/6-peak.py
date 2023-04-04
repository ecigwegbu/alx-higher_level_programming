#!/usr/bin/python3
""" Find a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """ find peak in a list of unsorted integers"""

    if len(list_of_integers) == 0:
        return None
    maxi = list_of_integers[0]
    for i in range(0, len(list_of_integers)):
        if list_of_integers[i] < maxi:
            return maxi
        maxi = list_of_integers[i]
    return maxi
