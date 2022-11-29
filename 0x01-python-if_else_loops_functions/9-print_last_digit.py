#!/usr/bin/python3
def print_last_digit(number):
    ld = int(str(number)[-1])
    print("{:d}".format(ld), end="")
    return ld
