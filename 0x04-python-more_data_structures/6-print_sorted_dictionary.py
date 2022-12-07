#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    newd = {sorted(a_dictionary)[i]: a_dictionary[sorted(a_dictionary)[i]]
            for i in range(len(sorted(a_dictionary)))}
    for i in range(len(newd)):
        print("{}: {}".format(list(newd)[i], newd[list(newd)[i]]))
