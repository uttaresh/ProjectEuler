# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?

def solution(n):
    # This can be done in 1 line in Python, but the spirit of this question is to do it with the assumption that
    # operations with such large numbers cannot be handled by the native language or system on its own. So we will
    # use arrays to implement our own doubling operation for large numbers.
    digits = [0 for _ in range(n)]
    digits[0] = 1
    for i in range(n):
        carry = 0
        for j in range(len(digits)):
            digits[j] = (digits[j] * 2) + carry
            if digits[j] > 9:
                digits[j] %= 10
                carry = 1
            else:
                carry = 0
    return sum(digits)


print(solution(1000))


