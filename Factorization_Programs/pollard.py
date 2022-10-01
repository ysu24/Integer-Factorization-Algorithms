import math
import random
import time
from numpy import average, median
   
def pollard(n :int) -> int:
    # test whether n is divisible by 2
    if n % 2 == 0:
        return 2

    # pick a coprime to n (for odd number, we pick n=2)
    a = 2
    a_record = a
    k = 2
    B = 100000
    i = 0
    # steps = 0

    # iterate till a prime factor is obtained
    while(True):
        # steps += 1
        a = pow(a, k, n)
        d = math.gcd((a-1), n)
   
        if (1 < d < n):
            # print(steps)
            return d

        if i >= B:
            if d == n:
                i = 0
                k = 2
                a_record += 1
                a = a_record
                
                d = math.gcd(a, n)
                if d != 1:
                    return d
                continue;
        k += 1
        i += 1


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
            print(f"{integer}; factor: {pollard(integer)}")
            # fermat_factorization(integer)
        end = time.time()
        runtimes.append((end-start) / test_times)
        print(f"{(end-start) / test_times}")
    
    return average(runtimes), median(runtimes)
  
if __name__ == "__main__":
    print(pollard(1196382318334999))
