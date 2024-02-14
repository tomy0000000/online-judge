# Let n be the length of s
#
# Time: O(n ^ 2)
# Space: O(n)


class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        ans = 0

        for i in range(n):
            dp[i][i] = True
            ans += 1

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                ans += 1

        for length in range(2, n):
            for i in range(n - length):
                if s[i] == s[i + length] and dp[i + 1][i + length - 1]:
                    dp[i][i + length] = True
                    ans += 1

        return ans
