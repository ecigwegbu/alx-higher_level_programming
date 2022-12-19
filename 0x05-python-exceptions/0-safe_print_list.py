#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    if x == 0:
        return 0
    for i in range(x):
        try:
            print(my_list[i], sep="", end="")
        except IndexError:
            break
        else:
            count += 1
    print("")
    return count