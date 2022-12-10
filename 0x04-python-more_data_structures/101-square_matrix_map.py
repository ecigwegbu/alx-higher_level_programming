#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda l: [x * x for x in l], matrix))
