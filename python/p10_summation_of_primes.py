# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
import math


def solution(limit: int):
    # Strategy: Use the sieve of Eros... whatever algorithm. Basically, assume all numbers greater than 2 are prime,
    # and then for each number that is prime in increasing order, mark out all its multiples as not prime.
    #
    # An optimization is to mark multiples starting at the square of the factor, since multiples before would have been
    # taken care of another number. For example, 7's contribution should begin with 49, since 7x2,x3...x6 will have
    # been taken care of by 2, 3...6
    not_prime = {1}
    sum = 0
    i = 2
    max_factor = int(math.sqrt(limit))
    while i < max_factor + 1:
        if i not in not_prime:
            sum += i
            for multiple in range(i * i, limit + 1, i):
                not_prime.add(multiple)
        i += 1
    for i in range(max_factor, limit + 1):
        if i not in not_prime:
            sum += i
    return sum


print(solution(2_000_000))
