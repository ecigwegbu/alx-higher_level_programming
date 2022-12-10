#!/usr/bin/python3
def weight_average(my_list=[]):
    weights = [w[1] for w in my_list]
    scores_times_weights = [y[0] * y[1] for y in my_list]
    return sum(scores_times_weights) / sum(weights)
