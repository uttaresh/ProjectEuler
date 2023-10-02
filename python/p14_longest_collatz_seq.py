# The following iterative sequence is defined for the set of positive integers:
#
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1.
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been
# proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.


def solution(limit: int):
    # Strategy: We will use a cache to memoize chain lengths once computed. This way, if a chain is a subset of another
    # chain, we don't have to recompute it. Doing it recursively may have been a bit easier on the eyes, but it would
    # have overflowed the stack so I have provided an iterative solution with caching.
    cache = {1: 1}
    longest_chain_length = -1
    longest_chain_start = None
    i = 1
    while i < limit:
        chain_length = 1
        n = i
        while n != 1:
            if n in cache:
                chain_length += cache[n]
                break
            else:
                if n % 2 == 0:
                    n //= 2
                else:
                    n = 3*n + 1
                chain_length += 1
        cache[i] = chain_length
        if chain_length > longest_chain_length:
            longest_chain_length = chain_length
            longest_chain_start = i
        i += 1
    return longest_chain_start


print(solution(1_000_000))
