from trial_division import trial_division
from fermat_factorization import fermat
from pollard import pollard
from wheel_factorization import wheel_factorization
from fermat_kraitchik_factorization import fermat_kraitchik
import random
from numpy import median, average
import time
import matplotlib.pyplot as plt
import gmpy2

def test_integer(integer):
    start = time.time()
    n = trial_division(integer)
    end = time.time()
    print(f'Trial division--factor: {n}; runtime: {end-start}')

    start = time.time()
    n = wheel_factorization(integer)
    end = time.time()
    print(f'Wheel factorization--factor: {n}; runtime: {end-start}')

    start = time.time()
    n = fermat(integer)
    end = time.time()
    print(f'Fermat--factor: {n}; runtime: {end-start}')

    start = time.time()
    n = fermat_kraitchik(integer)
    end = time.time()
    print(f'Fermat_Kraitchik--factor: {n}; runtime: {end-start}')

    start = time.time()
    n = pollard(integer)
    end = time.time()
    print(f'Pollard--factor: {n}; runtime: {end-start}')

def test_performance(method='trial_division', test_digits=15, test_times=10, test_groups=5, odd=False, random_seed=0):
    random.seed(random_seed)
    runtimes = []
    for i in range(test_groups):
        test_integers = []
        for j in range(test_times):
            random_num = random.randint(10**(test_digits-1), 10**test_digits-1)
            if odd:
                while(random_num % 2 == 0): # if the number is not odd, randomly generate another number until it is odd
                    random_num = random.randint(10**(test_digits-1), 10**test_digits-1)
            test_integers.append(random_num)

        # record runtime for each group
        start = time.time()

        for integer in test_integers:
            if method == 'trial_division':
                trial_division(integer)
            elif method == 'fermat':
                fermat(integer)
            elif method == 'pollard':
                pollard(integer)

        end = time.time()
        runtimes.append((end-start) / test_times)
        print(f"{(end-start) / test_times}")
    
    return average(runtimes), median(runtimes)

def test_runtime_t_w():
    """Use trial division and wheel factorization to factor integers with different number
    of digits
    
    Return: list of number of digits
    list of runtimes for trial division
    list of runtims for wheel factorization"""
    random.seed(6)
    runtime_trial = []
    runtime_wheel = []
    x = []
    for test_digit in range(2, 16):
        x.append(test_digit)
        test_numbers = []
        for i in range(50):
            random_num = random.randint(10**(test_digit-1), 10**test_digit-1)
            while(random_num % 2 == 0 or gmpy2.is_prime(random_num)): # if the number is not odd, randomly generate another number until it is odd
                random_num = random.randint(10**(test_digit-1), 10**test_digit-1)
            test_numbers.append(random_num)
        
        start = time.time()
        for number in test_numbers:
            trial_division(number)
        end = time.time()
        runtime_trial.append((end-start) / 50)

        start = time.time()
        for number in test_numbers:
            wheel_factorization(number)
        end = time.time()
        runtime_wheel.append((end-start) / 50)

    return x, runtime_trial, runtime_wheel

def test_runtime_f_k():
    """Use Fermat's and Fermat-Kraitchik factorization to factor integers with different number
    of digits
    
    Return: list of number of digits
    list of runtimes for Fermat's factorization
    list of runtims for  factorization"""
    random.seed(5)
    runtime_f = []
    runtime_k = []
    x = []
    for test_digit in range(2, 6):
        x.append(test_digit)
        test_numbers = []
        for i in range(50):
            random_num = random.randint(10**(test_digit-1), 10**test_digit-1)
            while(random_num % 2 == 0 or gmpy2.is_prime(random_num)): # if the number is not odd, randomly generate another number until it is odd
                random_num = random.randint(10**(test_digit-1), 10**test_digit-1)
            test_numbers.append(random_num)

        print(test_numbers)
        for number in test_numbers:
            start = time.time()
            fermat(number)
            end = time.time()
        runtime_f.append((end-start)/50)

        start = time.time()
        for number in test_numbers:
            fermat_kraitchik(number)
        end = time.time()
        runtime_k.append((end-start)/50)

    return x, runtime_f, runtime_k

def draw_trial_wheel():
    x, trial, wheel = test_runtime_t_w()
    plt.plot(x,trial, label="Trial Division")
    plt.plot(x,wheel, label="Wheel Factorization")
    plt.title('Runtime: Trial Division vs. Wheel Factorization')
    plt.xlabel('Nmuber of digits')
    plt.ylabel('Runtimes in second')
    plt.legend()
    plt.show()

def draw_fermat_kraitchik():
    x, trial, wheel = test_runtime_f_k()
    plt.plot(x,trial, label="Fermat's Factorization")
    plt.plot(x,wheel, label=" Fermat-Kraitchik Factorization")
    plt.title("Runtime: Fermat's Factorization vs. Fermat-Kraitchik Factorization")
    plt.xlabel('Nmuber of digits')
    plt.ylabel('Runtimes in second')
    plt.xticks(x)
    plt.legend()
    plt.show()

def test_semiprime_close():
    random.seed(0)
    semiprimes = []
    t_runtimes = []
    w_runtimes = []
    f_runtimes = []
    p_runtimes = []
    for test_digit in range(2,8):
        for i in range(30):
            random_num1 = random.randint(10**(test_digit-1), 10**test_digit-1)
            random_num2 = random.randint(10**(test_digit-1), 10**test_digit-1)
            semiprime = gmpy2.next_prime(random_num1) * gmpy2.next_prime(random_num2)
            semiprimes.append(semiprime)
    
    for num in semiprimes:
        start = time.time()
        trial_division(num)
        end = time.time()
        t_runtimes.append(end-start)

        start = time.time()
        wheel_factorization(num)
        end = time.time()
        w_runtimes.append(end-start)

        start = time.time()
        fermat(num)
        end = time.time()
        f_runtimes.append(end-start)

        start = time.time()
        pollard(num)
        end = time.time()
        p_runtimes.append(end-start)

    return t_runtimes, w_runtimes, f_runtimes, p_runtimes, semiprimes

def draw_semiprime_close():
    t_runtimes, w_runtimes, f_runtimes, p_runtimes, semi = test_semiprime_close()
    plt.scatter(semi, t_runtimes, label='Trial Division', alpha=0.5)
    plt.scatter(semi, w_runtimes, label='Wheel Factorization', alpha=0.5)
    plt.scatter(semi, f_runtimes, label="Fermat's Factorization", alpha=0.5)
    plt.scatter(semi, p_runtimes, label='Pollard p-1 Factorization', alpha=0.5)
    plt.legend(loc='best')
    plt.xlabel("Input integer")
    plt.ylabel("Runtimes in second")
    plt.title("Runtimes of Factoring Semiprimes")
    plt.show()

def test_semiprime():
    random.seed(0)
    semiprimes = []
    t_runtimes = []
    w_runtimes = []
    f_runtimes = []
    p_runtimes = []

    for test_digit in range(2,8):
        for i in range(30):
            random_num1 = random.randint(10, 10**test_digit)
            random_num2 = random.randint(10, 10**(test_digit-1))
            semiprime = gmpy2.next_prime(random_num1) * gmpy2.next_prime(random_num2)
            semiprimes.append(semiprime)
    # print(semiprimes)
    
    for num in semiprimes:
        start = time.time()
        trial_division(num)
        end = time.time()
        t_runtimes.append(end-start)

        start = time.time()
        wheel_factorization(num)
        end = time.time()
        w_runtimes.append(end-start)

        start = time.time()
        fermat(num)
        end = time.time()
        f_runtimes.append(end-start)

        start = time.time()
        pollard(num)
        end = time.time()
        p_runtimes.append(end-start)

    return t_runtimes, w_runtimes, f_runtimes, p_runtimes, semiprimes

def draw_semiprime():
    t_runtimes, w_runtimes, f_runtimes, p_runtimes, semi = test_semiprime()
    plt.scatter(semi, t_runtimes, label='Trial Division', alpha=0.5)
    plt.scatter(semi, w_runtimes, label='Wheel Factorization', alpha=0.5)
    plt.scatter(semi, f_runtimes, label="Fermat's Factorization", alpha=0.5)
    plt.scatter(semi, p_runtimes, label='Pollard p-1 Factorization', alpha=0.5)
    plt.legend(loc='best')
    plt.xlabel("Input integer")
    plt.ylabel("Runtimes in second")
    plt.title("Runtimes of Factoring Semiprimes")
    plt.show()

if __name__ == "__main__":
    # test_integer(396687)
    draw_trial_wheel()
    # draw_fermat_kraitchik()
    # draw_semiprime_close()
    # draw_semiprime()



    