#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for item in list(a_dictionary.items()):
        if (item[1]) == value:
            del a_dictionary[item[0]]
