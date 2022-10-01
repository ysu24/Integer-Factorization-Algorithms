import gmpy2
import random
import time
import math
from numpy import average, median
from trial_division import trial_division_part


def fermat(n :int) -> int:         
    # if n is a perfect root, then both its square roots are its factors
    if(gmpy2.is_square(n)):
        k = gmpy2.isqrt(n)
        return k

    # if n is not a perfect root, find smallest k s.t. k**2 >= n
    k = gmpy2.isqrt(n) + 1

    while(not gmpy2.is_square(k**2-n)):
        k += 1

    y = gmpy2.isqrt(k**2-n)
    
    return k-y


def test_performance(test_digits=15, test_times=10, test_groups=5, odd=False, random_seed=0):
    random.seed(random_seed)
    runtimes = []
    for i in range(test_groups):
        test_integers = []
        for j in range(test_times):
            random_num = random.randint(10**(test_digits-1), 10**test_digits-1)
            if odd:
                while(random_num % 2 == 0):
                    random_num = random.randint(10**(test_digits-1), 10**test_digits-1)
            test_integers.append(random_num)

        # record runtime for each group
        start = time.time()
        for integer in test_integers:
            print(f"{integer}; factor: {fermat(integer)}")
            # fermat_factorization(integer)
        end = time.time()
        runtimes.append((end-start) / test_times)
        print(f"{(end-start) / test_times}")
    
    return average(runtimes), median(runtimes)

if __name__ == "__main__":
        print(fermat(4884483))
