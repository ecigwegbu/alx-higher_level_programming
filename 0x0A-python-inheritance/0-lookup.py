#!/usr/bin/python3
""" This module is for a function that returns the list
of available attributes and methods
of an object."""


def lookup(obj):
    """"Return list of available attributes and methods"""
    return dir(obj)
