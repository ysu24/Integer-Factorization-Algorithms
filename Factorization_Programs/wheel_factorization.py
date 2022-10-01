import time
import random
import math
from numpy import average, median

def wheel_factorization(n: int) -> int:
    # test whether n is divisible by 2
    if n % 2 == 0:
        return 2
    # test whether n is divisible by 3
    if n % 3 == 0:
        return 3

    # the first possible prime factor is 5
    f = 5
    # instead of increasing f by 1 each time, we increase f by 2 or 4 each time
    increments = [2,4]
    i = 0
    while f * f < n:
        if n % f == 0:
            return f
        f += increments[i%2]
        i += 1
    return n

if __name__ == "__main__":
    print(wheel_factorization(12312413413))