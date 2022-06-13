#in variance squared values give extra weight to outliers
#outliers are bad
#STANDARD DEVIATION = root(Variance)
#sigma: Standard Deviation of Population
#S: Standard Deviation of Sample
#Large Standard Deviation = Large Spread

import math
from variance0 import variance

def standard_deviation(*args):
    return math.sqrt(variance(*args))

if __name__ == '__main__':
    print(f"SD : {standard_deviation(4, 6, 3, 5, 2)}")
