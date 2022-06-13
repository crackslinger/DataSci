#MODE returns values that occurs most often
#if all value occur at equal rate there's no MODE
#can have more than ONE

import math

def mode(*args):
    # creates dict of args and in place of values puts count of each item
    dict_vals = {i: args.count(i) for i in args}
    print(dict_vals)
    max_list = [k for k, v in dict_vals.items() if v == max(dict_vals.values())]
    return max_list

print(f"Mode : {mode(1, 9, 2, 3, 4, 5, 4, 3)}")
