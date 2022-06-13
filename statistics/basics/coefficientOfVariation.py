# Used to Compare Multiple Datasets
# Standard Deviation / Mean

import math
from standardDeviation0 import *
from mean0 import *

def coefficient_variation(*args):
    return standard_deviation(*args) / mean(*args)

if __name__ == '__main__':
    print(f"CV (miles) : {coefficient_variation(3, 4, 4.5, 3.5)}")
    print(f"CV (kms) : {coefficient_variation(4.828, 6.437, 7.242, 5.632)}")

