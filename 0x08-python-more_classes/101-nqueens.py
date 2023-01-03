#!/usr/bin/python3
""" THis module solves the N Queens puzzle """


import sys
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)
if sys.argv[1].isdigit != True:
    print("N must be a number")
    exit(1)
if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)
