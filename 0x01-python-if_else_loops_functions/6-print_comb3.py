#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if (i < j and not(i == 8 and j == 9)):
            print("{:d}{:d}, ".format(i, j), end="")
print("89")
