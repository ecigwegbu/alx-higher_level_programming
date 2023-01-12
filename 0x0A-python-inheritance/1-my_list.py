#!/usr/bin/python3
""" This module is for a class that
inherits from list"""


class MyList(list):
    """ This class inherits from list """

    def print_sorted(self):
        """ This function prints sorted list """
        print(sorted(self))
        return
