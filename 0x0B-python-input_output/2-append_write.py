#!/usr/bin/python3
""" This module is for a function
that appends data to a file and
"""

def append_write(filename="", text=""):
    """ This function appends data to a file.
    """

    if filename == "" or text == "":
        return

    with open(filename, 'a') as f:
            return f.write(text)
