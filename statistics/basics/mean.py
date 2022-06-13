import math

def mean(*args):
    val_sum = sum(args)
    return val_sum / len(args)

if __name__ == '__main__':
    print(f"Mean : {mean(1, 2, 3, 4, 5)}")
    
