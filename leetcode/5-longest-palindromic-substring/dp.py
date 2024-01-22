# Let n be the length of s
#
# Time: O(n ^ 2)
# Space: O(n ^ 2)


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[None for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        maxi, maxi_len = s[0], 1
        all_falses = 0
        for d in range(1, n):
            all_false = True
            for i in range(n - d):
                if s[i] == s[i + d] and (i + 1 == i + d or dp[i + 1][i + d - 1]):
                    dp[i][i + d] = True
                    all_false = False
                    length = d + 1
                    if length > maxi_len:
                        maxi, maxi_len = s[i : i + d + 1], length

            all_falses = all_falses + 1 if all_false else 0
            if all_falses == 2:
                break

        return maxi
