# A palindromic number reads the same both ways. The largest palindrome made from the product of two -digit numbers is
# 9009 = 91 x 99
#
# Find the largest palindrome made from the product of two 3-digit numbers.
import queue


def solution():
    largest = -1
    for i in reversed(range(100, 1000)):
        for j in reversed(range(100, 1000)):
            prod = i*j
            if __is_palindrome(prod) and prod > largest:
                largest = prod

    return largest


def __is_palindrome(n: int) -> bool:
    stack = []
    q = queue.Queue()
    rem = n
    while rem > 0:
        lsb = rem % 10
        stack.append(lsb)
        q.put(lsb)
        rem //= 10
    while len(stack) > 0:
        if stack.pop() != q.get():
            return False
    return True


print(solution())
