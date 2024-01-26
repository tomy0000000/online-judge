# Let n be the length of text1 and m be the length of text2.
#
# Time: O(n * m)
# Space: O(n * m)


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                dp[i + 1][j + 1] = (
                    dp[i][j] + 1
                    if text1[i] == text2[j]
                    else max(dp[i][j + 1], dp[i + 1][j])
                )

        return dp[-1][-1]
