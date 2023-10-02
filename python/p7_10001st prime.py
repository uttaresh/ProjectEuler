# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10001st prime number?

def solution(chunk_size: int, n: int):
    # Note: This is a bit harder of a challenge, since I'm assuming I don't know a ceiling for the 10,001st prime
    # number. I can easily find a ceiling by trial and error, and build a much simpler solution. See my Java
    # solution to this problem for this approach. In this Python solution, I am imposing the rule that I may not use a
    # ceiling to make this problem easier, forcing me to use a different approach since the simpler approach requires
    # using the ceiling value as part of the solution.
    #
    # Strategy: Start by assuming all numbers >1 are prime. Then starting from the lowest prime number (2) and mark
    # all its multiples as non-prime. Of course, we can't do it all the way till infinity so we will perform this task
    # in chunks. That is to say, we will assume the 10,001st prime is in the first N natural numbers, then the next
    # N, and so on. N will of course be large, say 10K or more.

    chunk_start = 0
    not_prime = {0, 1}
    primes = []
    while True:
        chunk_end = chunk_start + chunk_size
        # for all primes found before this chunk, mark their multiples in this chunk as not prime
        for prime in primes:
            first_multiple = chunk_start // prime
            if chunk_start % prime != 0:
                first_multiple += 1
            prod = prime * first_multiple
            while prod < chunk_end:
                not_prime.add(prod)
                prod += prime
        curr = chunk_start
        while curr < chunk_end:
            if curr not in not_prime:
                primes.append(curr)
                if len(primes) == n:
                    return primes[-1]
                # Mark all multiples of this prime as not prime
                first_multiple = 2
                prod = curr * first_multiple
                while prod < chunk_end:
                    not_prime.add(prod)
                    prod += curr
            curr += 1
        chunk_start += chunk_size


print(solution(10_000, 10_001))
# print(solution(10, 6))
