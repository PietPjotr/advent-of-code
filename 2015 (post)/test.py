import collections
import itertools
import timeit
import random
import math

def prime_factors(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            n /= i
            yield i
        else:
            i += 1

    if n > 1:
        yield n


def prod(iterable):
    result = 1
    for i in iterable:
        result *= i
    return result


def get_divisors_fast(n):
    pf = prime_factors(n)

    pf_with_multiplicity = collections.Counter(pf)

    powers = [
        [factor ** i for i in range(count + 1)]
        for factor, count in pf_with_multiplicity.items()
    ]

    for prime_power_combo in itertools.product(*powers):
        yield prod(prime_power_combo)


def get_divisors_slow(num):
    divs = []
    end = int(math.sqrt(num) + 1)
    for i in range(1, end):
        if num % i == 0:
            divs.append(i)
            divs.append(num // i)
    return divs


def get_divisors_test(num):
    divs = set()
    end = math.sqrt(num) + 1
    primes = list(prime_factors(num))
    # print(primes)
    for prime in primes:
        delta = prime
        while num % prime == 0 and prime < end:
            divs.add(prime)
            divs.add(num // prime)
            prime += delta

    divs.add(1)
    divs.add(num)
    return divs


def time_funcs():
    nums = [random.randint(1, 10**10) for _ in range(100000)]


    start = timeit.default_timer()
    for num in nums:
        get_divisors_fast(num)
    end = timeit.default_timer()
    print(end - start)


time_funcs()

