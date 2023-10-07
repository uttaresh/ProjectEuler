# Find the sum of the digits of the number that is 100! (100 factorial)

# It's too easy in Python. Feels like cheating.
def ez_solution():
    n = 100
    prod = 1
    for i in range(2, n + 1):
        prod *= i
    sum = 0
    while prod > 0:
        sum += prod % 10
        prod //= 10
    return sum


def __multiply_it(arr, n, base) -> int:
    carry = 0
    for i in range(len(arr)):
        arr[i] = (arr[i] * n) + carry
        if arr[i] >= base:
            carry = arr[i] // base
            arr[i] = arr[i] % base
        else:
            carry = 0
    while carry > 0:
        arr.append(carry % base)
        carry //= base


# Slightly more difficult solution, by assuming the native system can't multiply numbers as large as 100 factorial
def medium_solution():
    base = 1_000_000_000  # any large multiple of 10
    n = 100
    prod = [1]
    for i in range(2, n + 1):
        __multiply_it(prod, i, base)
    sum = 0
    while len(prod) > 0:
        curr = prod.pop()
        while curr > 0:
            sum += curr % 10
            curr //= 10
    return sum


print(medium_solution())
