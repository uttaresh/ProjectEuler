# If all the numbers from 1 to 1000 (inclusive) were written out in words, how many letters would be used?

numbers_in_words = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred",
    1000: "thousand"
}


def size_in_words(n: int) -> int:
    size = 0
    rem = n
    if rem >= 1000:
        thousands = rem//1000
        size += len(numbers_in_words[thousands]) + len(numbers_in_words[1000])
        rem = rem % 1000
    if rem >= 100:
        hundreds = rem//100
        size += len(numbers_in_words[hundreds]) + len(numbers_in_words[100])
        rem = rem % 100
        if rem > 0:
            size += len("and")
    if rem >= 20:
        tens = rem // 10 * 10
        size += len(numbers_in_words[tens])
        rem = rem % 10
    if rem > 0:
        size += len(numbers_in_words[rem])
    return size


def solution(limit: int):
    size = 0
    for i in range(1, limit + 1):
        size += size_in_words(i)
    return size


print(solution(1000))
