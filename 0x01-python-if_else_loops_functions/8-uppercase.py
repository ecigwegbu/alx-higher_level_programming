#!/usr/bin/python3
def uppercase(str):
    i = 0
    while i < len(str):
        ch = ord(str[i])
        if ch >= 97 and ch <= 122:
            ch = 64 + (ch - 96)
        print("{:c}".format(ch), end="")
        i += 1
    print("")
