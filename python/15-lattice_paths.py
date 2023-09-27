# Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6
# routes to the bottom right corner.
#
# Notice the diagram with routes along the edges of the cell, rather than through the cells:
#       https://projecteuler.net/problem=15
#
# How many such routes are there through a 20x20 grid?


def solution(grid_height, grid_width):
    # Note: Pay careful attention to the drawing in this problem. The routes/ways are along the edges of the cell, not
    # inside the cells. So a 2x2 grid essentially has 3x3 "nodes", a 3x3 grid has 4x4 nodes, and so on. We therefore
    # take the size of the grid as input, and then work with converted rows and cols representing the nodes.
    rows = grid_height + 1
    cols = grid_width + 1
    # Strategy: The ideal solution requires working with permutations, combinations, or something of the sort in
    # mathematics which I don't remember and can probably solve this problem either in constant time or in O(n) or O(m)
    # if the solution is a series. On the other hand, the recursive solution (with caching) is quite easy enough to do.
    # You can find the recursive solution with caching in my Java solution to this problem from 2014. To make this
    # slightly more challenging, I'll try to solve this problem iteratively here.
    ways = [[-1 for i in range(cols)] for j in range(rows)]
    # For all nodes in the bottom row and all nodes in the rightmost column, there is only one way to the exit
    for col in range(0, cols):
        ways[rows-1][col] = 1
    for row in range(0, rows):
        ways[row][cols-1] = 1
    # Next, from the bottom-rightmost unsolved cell, move left and repeat moving up each row
    for row in reversed(range(0, rows - 1)):
        for col in reversed(range(0, cols - 1)):
            ways[row][col] = ways[row][col+1] + ways[row+1][col]
    return ways[0][0]


print(solution(20, 20))
