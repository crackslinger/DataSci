import math

def median(*args):
    if len(args) % 2 == 0:
        i = round((len(args)) / 2)
        j = i - 1
        return (args[i] + args[j]) / 2
    else:
        k = round(len(args) / 2)
        return args[k]

print(f"Median: {median(1, 2, 3, 4, 5)}")
print(f"Median: {median(1, 2, 3, 4, 5, 6)}")
print(f"Median: {median(1, 3, 5, 6, 7, 9, 12, 33, 35, 50)}")
