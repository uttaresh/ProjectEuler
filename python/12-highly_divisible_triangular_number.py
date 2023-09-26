# Full context found on site: https://projecteuler.net/problem=12
# The sequence of triangle numbers is generated by adding the natural numbers.
# What is the value of the first triangle number to have over five hundred divisors?
import math


def num_divisors(n: int) -> int:
    # Optimization: Divisors are always paired on either side of the square root of the number.
    # For example, for 18 we have 3 and 6 on either side of 4.x, for 100 we have 5 and 20 on either side of 10.
    # There is a math proof for this, but intuitively this seems true because if you take the square root and square
    # it, you obviously get the number. So if one of the factors is greater than the square root, then the other one
    # MUST be less than the square root. Otherwise, we have one factor greater than the square root and the other
    # equal to or greater than the square root -- both of which lead the product to be greater than the number which is
    # not allowed.
    i = 1
    res = 0
    sqrt = math.sqrt(n)
    while i <= sqrt:
        if n % i == 0:
            res += 1
        i += 1
    return res * 2


def solution():
    natural_number = 0
    i = 1
    while True:
        natural_number += i
        if num_divisors(natural_number) > 500:
            return natural_number
        i += 1


print(solution())
