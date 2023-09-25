# The four adjacent digits in the -digit number that have the greatest product are 9 x 9 x 8 x 9 = 5832. Find the 13
# adjacent digits in the 100-digit number that have the greatest product. What is the value of this product?

number = "73167176531330624919225119674426574742355349194934" \
        "96983520312774506326239578318016984801869478851843" \
        "85861560789112949495459501737958331952853208805511" \
        "12540698747158523863050715693290963295227443043557" \
        "66896648950445244523161731856403098711121722383113" \
        "62229893423380308135336276614282806444486645238749" \
        "30358907296290491560440772390713810515859307960866" \
        "70172427121883998797908792274921901699720888093776" \
        "65727333001053367881220235421809751254540594752243" \
        "52584907711670556013604839586446706324415722155397" \
        "53697817977846174064955149290862569321978468622482" \
        "83972241375657056057490261407972968652414535100474" \
        "82166370484403199890008895243450658541227588666881" \
        "16427171479924442928230863465674813919123162824586" \
        "17866458359124566529476545682848912883142607690042" \
        "24219022671055626321111109370544217506941658960408" \
        "07198403850962455444362981230987879927244284909188" \
        "84580156166097919133875499200524063689912560717606" \
        "05886116467109405077541002256983155200055935729725" \
        "71636269561882670428252483600823257530420752963450"


def calculate_window_product(start: int, end: int) -> int:
    prod = 1
    for i in range(start, end):
        prod *= int(number[i])
    return prod


def solution(window_size):
    # Strategy: I'll use a sliding window approach to solve this problem. There is the edge case of zero, however.
    # That is, if we encounter a zero, the product of the window becomes zero by multiplication. That's fine, but when
    # the window exits the zero, the default logic would lead to a divide by zero which is meaningless. Hence, when we
    # encounter a zero, we should have the entire window skip the zero, and recalculate the window at the next non-zero
    # opportunity.
    window_start = 0
    window_end = window_start + window_size

    # Calculate init window product
    window_product = calculate_window_product(window_start, window_end)
    largest_product = window_product

    while window_end < len(number):
        if window_product == 0:
            # fix zero product window
            removed = None
            while removed != 0 and window_end != len(number):
                removed = int(number[window_start])
                window_start += 1
                window_end += 1
            window_product = calculate_window_product(window_start, window_end)
        else:
            # shift window one place
            removed = int(number[window_start])
            added = int(number[window_end])
            window_product = window_product * added // removed
            window_end += 1
            window_start += 1
        if window_product > largest_product:
            largest_product = window_product
    return largest_product


print(solution(13))
