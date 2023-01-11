#!/usr/bin/python3
""" This module contains a function that
appends a line after a given line"""


def append_after(filename="", search_string="", new_string=""):
    """ Append a line after a line containing a given string """

    if filename == "" or search_string == "":
        return
    if filename is None or search_string is None:
        return
    lines = []
    with open(filename, "r") as f:
        lines = f.readlines()
        for i in range(len(lines)):
            if search_string in lines[i]:
                lines.insert(i + 1, new_string)
    with open(filename, "w") as f2:
        f2.writelines(lines)
    return
