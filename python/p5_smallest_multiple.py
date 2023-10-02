# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def solution():
    # Strategy: Brute force check all numbers, but skip in increments of 20 since they have to be divisible by 20
    curr = 20
    while True:
        evenly_divisible = True
        for i in range(1, 21):
            if curr % i != 0:
                evenly_divisible = False
                break
        if evenly_divisible:
            return curr
        curr += 20


print(solution())
