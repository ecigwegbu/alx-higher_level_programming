#!/usr/bin/python3
lower = True
for i in range(26):
    if lower:
        print("{:c}".format(97 + (25-i)), end="")
        lower = False
    else:
        print("{:c}".format(65 + (25-i)), end="")
        lower = True
