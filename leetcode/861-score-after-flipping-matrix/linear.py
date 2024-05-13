# Let n be the number of cells in the grid.
#
# Time: O(n)
# Space: O(1)


class Solution:
    def matrixScore(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        for row_i, row in enumerate(grid):
            if row[0] == 0:
                grid[row_i] = [int(not bool(i)) for i in row]

        ans = sum(row[0] for row in grid) * (2 ** (n - 1))
        for col in range(1, n):
            cnt = sum(row[col] for row in grid)
            cnt = max(cnt, m - cnt)
            ans += cnt * (2 ** (n - col - 1))

        return ans
