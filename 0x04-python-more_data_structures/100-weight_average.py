#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    weights = [w[1] for w in my_list]
    scores_times_weights = [y[0] * y[1] for y in my_list]
    return sum(scores_times_weights) / sum(weights)
