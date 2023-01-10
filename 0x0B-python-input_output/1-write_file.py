#!/usr/bin/python3
""" This module is for a function
That writes data to a file and
"""

def write_file(filename="", text=""):
    """ This function writes data to a file.
    """

    if filename == "" or text == "":
        return

    with open(filename, 'w') as f:
            return f.write(text)
