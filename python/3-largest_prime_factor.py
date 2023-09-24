# The prime factors of 13195 are 5, 7, 13, and 29.
#
# What is the largest prime factor of the number 600851475143?
import math


def solution(target):
    primes = []

    # find prime numbers until the square root of target

    # note: this is my hacky solution because I haven't figured out how to compute the correct solution for prime
    # factors > sqrt(target)
    max: int
    if (target > 100):
        max = int(math.sqrt(target)) + 1
    else:
        max = target
    is_prime = [True] * max
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, max):
        if is_prime[i]:
            primes.append(i)
            j = 2
            product = i * j
            while product < max:
                is_prime[product] = False
                j += 1
                product = i * j

    # find all largest prime that is a factor:
    while len(primes) > 0:
        largest = primes.pop()
        if target % largest == 0:
            return largest

    return None


print(solution(600851475143))






