#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    l1 = len(tuple_a)
    if l1 == 0:
        a0 = 0
        a1 = 0
    elif l1 == 1:
        a0 = tuple_a[0]
        a1 = 0
    else:
        a0 = tuple_a[0]
        a1 = tuple_a[1]

    l2 = len(tuple_b)
    if l2 == 0:
        b0 = 0
        b1 = 0
    elif l2 == 1:
        b0 = tuple_b[0]
        b1 = 0
    else:
        b0 = tuple_b[0]
        b1 = tuple_b[1]

    return (a0 + b0, a1 + b1)
