# Covariance tells us if 2 vlaues are Moving in the same Direction
# AND Correlation Coefficient
# COV = sum((xi-meanx)*(yi-meany)) / n-1
# >0: Moving Together 
# <0: Moving Opposite
# =0: Moving Independent

# x and y : Market capital and Earnings : 1532 and 45.2
# so if >0 than as MC grows earnings grow and so on

import math
from mean0 import *
from standardDeviation0 import *

def covariance(*args):
    # Use a list comprehension to get all values
    # stored in the 1st & 2nd list
    list_1 = [i[0] for i in args]
    list_2 = [i[1] for i in args]
    print(f"This is list1: {list_1} and list2 {list_2}")
    # Pass those lists to get their means
    list_1_mean = mean(*list_1[0])
    list_2_mean = mean(*list_2[0])
    numerator = 0

    # We must have the same number of elements
    # in both lists
    if len(list_1[0]) == len(list_2[0]):
        for i in range(len(list_1[0])):
            # FInd xi - x mean * yi - y mean
            numerator += (list_1[0][i] - list_1_mean) * (list_2[0][i] - list_2_mean)
        denominator = len(list_1[0]) - 1
        return numerator / denominator
    else:
        print("Error : You must have the same number of values in both lists")


def correlation_coefficient(*args):
    list_1 = [i[0] for i in args]
    list_2 = [i[1] for i in args]
    # Pass those lists to get their standard deviations
    list_1_sd = standard_deviation(*list_1[0])
    list_2_sd = standard_deviation(*list_2[0])
    print(f"L1 SD : {list_1_sd}")
    print(f"L2 SD : {list_2_sd}")
    denominator = list_1_sd * list_2_sd
    # Get the covariance
    numerator = covariance(*args)
    return numerator / denominator


# List that contains market cap in 1st list
# and earnings in the 2nd list
m_d_list = [[1532, 1488, 1343, 928, 615], [58, 35, 75, 41, 17]]
print(f"Stock Covariance : {covariance(m_d_list)}")

# Get the Correlation Coefficient
print(f"Correlation Coefficient : {correlation_coefficient(m_d_list)}")
