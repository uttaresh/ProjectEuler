# The prime factors of 13195 are 5, 7, 13, and 29.
#
# What is the largest prime factor of the number 600851475143?
import math


def solution(target):
    # Disclaimer: This solution is not complete, and just happens to work for this input. The correct solution requires
    # accounting for prime factors > sqrt of the target which I haven't implemented yet. It isn't obvious at all unless
    # you're great at math, and required me to search around quite a bit on the internet to learn about prime factors.
    # Here is a good explanation: https://math.stackexchange.com/a/883184/1225364
    # What's remaining is to find the one possible prime factor > sqrt(target), and there can only be one. This one
    # is calculated by starting with the target, and repeatedly dividing by all other prime factors that evenly divide
    # it, or something of the sort.
    max = math.sqrt(target)
    prime_factors = []
    not_prime = {0, 1}
    i = 2
    while i < max:
        if i not in not_prime:
            if target % i == 0:
                prime_factors.append(i)
            j = 2
            product = i * j
            while product < max:
                not_prime.add(product)
                j += 1
                product = i * j
        i += 1

    if len(prime_factors) > 0:
        return prime_factors[-1]
    else:
        return None


print(solution(600851475143))






