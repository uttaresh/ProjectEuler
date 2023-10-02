# This is a solution for problems both versions of Maximum Path Sum:
# Problem 18: https://projecteuler.net/problem=18
# Problem 67: https://projecteuler.net/problem=67


easy_input = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
]


def solution(tree):
    # Strategy: Treat it like a tree. From each node, we can go either to the left child or the right child. A greedy
    # approach will not work since there may be a better route underneath the immediately worse choice. So we will need
    # to traverse all possible paths. To avoid re-computation, we need to use a caching based solution to solve it
    # recursively. There is probably a 2D dynamic programming solution that can do it faster, but I haven't practiced
    # DP in a while to be good enough to find it right now.
    # Update: I've used the iterative (possibly DP soln) in Prob 67.
    depth = len(tree)
    cache = [[None for i in range(depth)] for j in range(depth)]

    def left_child(r, c, depth) -> (int, int):
        if r == depth - 1:
            return None
        else:
            return r + 1, c

    def right_child(r, c, depth) -> (int, int):
        if r == depth - 1:
            return None
        else:
            return r + 1, c + 1

    def get_max_path(r, c, depth) -> int:
        if cache[r][c] is None:
            val = tree[r][c]
            if left_child(r, c, depth) is None:
                cache[r][c] = val
            else:
                lc = left_child(r, c, depth)
                left_max = get_max_path(lc[0], lc[1], depth)
                rc = right_child(r, c, depth)
                right_max = get_max_path(rc[0], rc[1], depth)
                cache[r][c] = val + max(left_max, right_max)
        return cache[r][c]

    return get_max_path(0, 0, depth)


if __name__ == '__main__':
    print(solution(easy_input))
