# Let m, n be the number of rows and columns of the grid.
#
# Time: O(m * n ^ 2)
# Space: O(m * n ^ 2)


class Solution:
    def cherryPickup(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(m)]

        for i in range(m - 1, -1, -1):
            for j in range(n):
                for k in range(j, n):
                    dp[i][j][k] = grid[i][j]

                    if j != k:
                        dp[i][j][k] += grid[i][k]

                    if i == m - 1:
                        continue

                    dp[i][j][k] += max(
                        dp[i + 1][jj][kk]
                        for jj in range(max(j - 1, 0), min(j + 2, n))
                        for kk in range(max(k - 1, 0), min(k + 2, n))
                    )

        return dp[0][0][-1]
