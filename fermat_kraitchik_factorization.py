import math
import gmpy2
from trial_division import trial_division


def fermat_kraitchik(n :int) -> int:       
    k = gmpy2.isqrt(n) + 1
    while True:
        t = 1
        y_2 = k*k - t*n
        while y_2 >= 0:
            y_2 = k*k - t*n
            if gmpy2.is_square(y_2):
                y = gmpy2.isqrt(y_2)
                if (k+y)%n != 0 and (k-y)%n != 0:
                    return math.gcd(k-y, n)
            t += 1
        k += 1

if __name__ == "__main__":
    i = 4884483
    print(fermat_kraitchik(i))