#!/usr/bin/python3
def roman_to_int(roman_string):
    if not (type(roman_string) is str) or (roman_string is None):
        return 0
    romdict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    tot = 0
    for i in range(len(roman_string)):
        sign = 1
        value_i = romdict[roman_string[i]]
        if i < (len(roman_string) - 2):
            value_ip1 = romdict[roman_string[i + 1]]
            if value_ip1 > value_i:
                sign = -1
        tot += value_i * sign
    return tot
