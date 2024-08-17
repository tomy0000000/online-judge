# Let m be the number of rows and n be the number of columns.
#
# Time: O(m * n)
# Space: O(m * n)


class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        m, n = len(points), len(points[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0] = points[0]

        for i in range(1, m):
            # left to right
            prev_row_maxi = 0
            for j in range(n):
                prev_row_maxi -= 1
                prev_row_maxi = max(prev_row_maxi, dp[i - 1][j])
                dp[i][j] = points[i][j] + prev_row_maxi

            # right to left
            prev_row_maxi = 0
            for j in range(n - 1, -1, -1):
                prev_row_maxi -= 1
                prev_row_maxi = max(prev_row_maxi, dp[i - 1][j])
                dp[i][j] = max(dp[i][j], points[i][j] + prev_row_maxi)

        return max(dp[-1])
