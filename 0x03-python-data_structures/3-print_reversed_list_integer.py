#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list == []:
        return
    list_len = len(my_list)
    for i in range(list_len - 1, -1, -1):
        print("{}".format(my_list[i]))
