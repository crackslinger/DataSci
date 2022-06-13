# how is Data Spread around Mean
# sigma squared: Variance of Population
# S squared: Variance of Sample
# S squared = Sum(xi - x)squared / n-1
# for ex: SAMPLE[4, 3, 6, 5, 2]
# MEAN = 20/5 = 4
# S^2 = ((4-4)^2 + (3-4)^2 + (6-4)^2 + (5-4)^2 + (2-4)^2) / 4 = 2.5

import math
from mean0 import *

def variance(*args):
    mean_val = mean(*args)
    numerator = 0
    for i in args:
        numerator += (i - mean_val) ** 2
    denominator = len(args) - 1
    return numerator / denominator

if __name__ == '__main__':
    print(f"Variance : {variance(1000, 2032, 99, 96, 84, 92, 100, 88)}")
