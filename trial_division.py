import time
import random
import math
from numpy import average, median


# def trial_division(n: int) -> list[int]:
#     """Return a list of the prime factors for a natural number."""
#     return trial_division_recursion(n, 2, [])

# def trial_division_recursion(n, f, factors):
#     if n <= 1:
#         return factors
#     else:
#         # if n = 0 mod f, f is a factor of n.
#         if n % f == 0:
#             factors.append(f)
#             n = n / f
#         else:
#             f += 1
#         return trial_division_recursion(n, f, factors)

def trial_division_all(n: int) -> list[int]:
    """Return a list of the prime factors for a natural number."""
    factors = []
    f = 2
    while n > 1:
        if n % f == 0:
            factors.append(f)
            n = n // f
        else:
            if f * f < n:
                f += 1
            else:
                factors.append(n)
                break
    return factors


def trial_division(n: int) -> int:
    """Return a factor or itself."""
    f = 2
    while f * f < n:
        if n % f == 0:
            return f
        f += 1
    return n

def trial_division_part(n, upper_bound=100):
    f = 2
    while f * f < n and f < 100:
        if n % f == 0:
            return f
        f += 1
    

def test_Mersenne(num_test):
    start = time.time()
    prime = []
    for i in range(2, num_test+1):
        number = 2**i-1
        factors = trial_division_all(number)
        print(f'2^{i}-1={number}; factors: {factors}')
        if len(factors) == 1:
            prime.append(i)
    print(prime)
    print(f"time: {time.time()-start}")


def test_Repunit(num_test):
    for i in range(2, num_test+1):
        test_number = int((10**i-1) // 9)
        factors = trial_division_all(test_number)
        print(f'k={i}: {test_number}; factors: {factors}')


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
            # print(f"{integer}; factor: {trial_division(integer)}")
            trial_division(integer)
        end = time.time()
        runtimes.append((end-start) / test_times)
        print(f"{(end-start) / test_times}")
    
    return average(runtimes), median(runtimes)

if __name__ == "__main__":
    # print(test_performance())
    print(trial_division_part(15))

    # test_Mersenne(100)
    # test_Repunit(10)
   
