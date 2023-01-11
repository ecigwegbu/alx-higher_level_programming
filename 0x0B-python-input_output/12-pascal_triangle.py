#!/usr/bin/python3
""" This module contains a function: for technical Interview
It returns the Paschal's triangle."""


def pascal_triangle(n):
    """ This function returns the Paschal triangle of order n"""

    if n <= 0:
        return []
    if n == 1:
        return [1]
    if n == 2:
        return [[1], [1, 1]]

    pt = [[1], [1, 1]]
    for i in range(3, n):
        j = i - 1
        # make new list

        # append it to pt
