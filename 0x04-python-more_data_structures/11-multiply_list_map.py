#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
#    return [num * number for num in my_list]
    return list(map(lambda num: num * number, my_list))
