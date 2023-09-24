# The sum of the squares of the first ten natural numbers is:
#               1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is:
#               (1 + 2 + ... + 10) = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
# 3025 - 385 = 2640
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def solution(n):
    # Strategy: We could solve this by brute force since 100 is not a large number, but we will use summation formulae
    # from high school for sum of 1..n and sum of 1^2..n^2
    sum = (n * (n + 1)) // 2
    square_of_sum = sum * sum
    sum_of_squares = (n * (2*n + 1) * (n + 1)) // 6
    return square_of_sum - sum_of_squares


print(solution(100))
