#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list == []:
        return
    my_list_rev = list(reversed(my_list))
    for i in my_list_rev:
        print("{:d}".format(my_list_rev))
