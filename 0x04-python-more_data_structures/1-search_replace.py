#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()

    while search in new_list:
        p = new_list.index(search)
        new_list.remove(search)
        new_list.insert(p, replace)
    return new_list
