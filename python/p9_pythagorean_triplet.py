# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#        a^2 + b^2 + c^2
# For example, 3^2 + 4^2 = 5^2
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000
# Find the product abc.


def solution():
    # Strategy: I can't think of a better algo than brute force right now, so I will use that but try to bound the
    # required computations using some of the statements in this question. Namely that a < b < c, and the relations
    # implied between a, b, c by the equations

    # a cannot exceed 333 since b and c must be greater than a and still add to 1000
    for a in range(1, 333):
        # b must be greater than a, AND b cannot exceed 500 since c must be greater, and the sum must not exceed 1000
        for b in range(a + 1, 500):
            c = 1000 - a - b
            # We can skip the relatively more expensive squares calculation when a < b < c doesn't hold
            if a < b < c:
                if (a * a) + (b * b) == (c * c):
                    return a*b*c


print(solution())
