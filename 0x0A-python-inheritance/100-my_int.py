#!/usr/bin/python3
""" This module defines a modified int class with
modified operators"""


class MyInt(int):
    """ over-ride gt and ne operators: """

    def __eq__(self, obj):
        """ reverse == operator"""

        return False

    def __ne__(self, obj):
        """ reverse != operator"""

        return False
