# Time: O(n * k)
# Space: O(n * k)


class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        dp = [[0 for _ in range(n + 1)] for _ in range(k + 1)]
        dp[0][0] = 1

        for i in range(k + 1):
            for j in range(1, n + 1):
                if i == 0:
                    dp[i][j] = 1
                    continue
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                if i - j >= 0:
                    dp[i][j] -= dp[i - j][j - 1]
                dp[k][n] %= 10**9 + 7

        return dp[k][n]
