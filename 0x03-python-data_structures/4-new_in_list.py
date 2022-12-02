#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list.copy()
    if idx >= len(my_list):
        return my_list.copy()
    else:
        my_list_copy = my_list.copy()
        my_list_copy.pop(idx)
        my_list_copy.insert(idx, element)
        return my_list_copy
