#!/usr/bin/python3
""" This module contains a function that
appends a line after a given line"""


def append_after(filename="", search_string="", new_string=""):
    """ Append a line after a line containing a given string """

    lines = []
    with open(filename, "a+") as f:
        lines = f.readlines()
        for i in range(len(lines)):
            if search_string in lines[i]:
                lines.insert(i, new_string)
                break
    with open(filename, "w") as f:
        f.writelines(lines)
