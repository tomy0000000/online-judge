# Let m, n be the number of rows and columns in the grid
#
# Time: O(m * n)
# Space: O(m * n)

from math import inf


class Solution:
    def access(self, grid: list[list[int]], m: int, n: int, i: int, j: int) -> int:
        if 0 <= i < m and 0 <= j < n:
            return grid[i][j]
        return inf

    def maxMoves(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        valid_moves = [[0 for _ in range(n)] for _ in range(m)]
        max_moves = 0
        for col in range(1, n):
            col_max = 0
            for row in range(m):
                val = grid[row][col]
                valid_moves[row][col] = (
                    int(self.access(grid, m, n, row - 1, col - 1) < val)
                    + int(self.access(grid, m, n, row, col - 1) < val)
                    + int(self.access(grid, m, n, row + 1, col - 1) < val)
                )
                if valid_moves[row][col] == 0:
                    grid[row][col] = inf
                col_max = max(col_max, valid_moves[row][col])
            if col_max == 0:
                break
            max_moves += 1
        return max_moves
